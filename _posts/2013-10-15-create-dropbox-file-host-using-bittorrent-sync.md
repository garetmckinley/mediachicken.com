---
layout: post
title:  "Create a private \"Dropbox\" file host using BitTorrent Sync"
date:   2013-10-15 15:55:00
category: tutorial
tags BitTorrent Sync, BTSync, Cloud, Cloud File Host, DigitalOcean, Dropbox, File Host, File Sync, Google Drive, linux, NSA, PRISM, Private Cloud, Private Server, Private Sync, Secure, Sync, Sync Hacks, Torrent, ubuntu
---

## Why create your own cloud host when there are services like Dropbox that already exist?
This is a very valid question; however, if you really think about it, I think it'll be pretty obvious. On a daily basis, many people are constantly backing up files on their personal Dropbox drive. While there's really nothing wrong with this, what would happen if Dropbox were to get hacked? I'm sure nobody saw it coming when [PlayStation Network got hacked](http://en.wikipedia.org/wiki/PlayStation_Network_outage), yet, around 77 million people had their personal information stolen. What would happen if that same thing happened to Dropbox, where millions of people store sensitive data?

Sure this is probably an extreme case, but one that hits closer to home would be the recent unveiling of project PRISM. Do you really want the National Security Agency (NSA) to have access to your data? Of course there's still risk of your own personal servers getting hacked or monitored by the NSA, but a data archiving company such as Dropbox would be a higher target than John Smith's personal file server.

## So what's the solution?
No doubt we're in the mobile age of computing. We want all our data with us all the time, so canceling our cloud syncing service isn't really an option. But what if we could create our own syncing service? That's precisely what we're going to be doing today, and to make our lives a lot easier, the awesome developers over at [BitTorrent, Inc.](http://bittorrent.com) have created a [pretty awesome] file syncing protocol called, [BitTorrent Sync](http://labs.bittorrent.com/experiments/sync.html).

## What is BitTorrent Sync?
Don't get discouraged after seeing the word "Torrent" included in it. There's nothing illegal about this protocol. Torrents gained popularity as being an excellent method of [P2P](http://en.wikipedia.org/wiki/Peer-to-peer) file sharing utilizing the BitTorrent protocol. Recently, the folks as BitTorrent decided to create a similar protocol for a P2P file syncing service. So BitTorrent Sync was born. This service lives on all your machines and can keep whatever folders you select in sync. Even more amazingly, you can have a folder shared on as many (or few) devices as you want! Being a Peer-To-Peer protocol, there's no need for a remote server. So it can live in your local area network and never reach out to external servers!

There is however one drawback to this method of file syncing. If your home computers (which are running BitTorrent Sync) are turned off, you won't be able to download your files on the go using your iPhone or Android device. You'll have similar results if you're on the go and your home network just happens to go down. At this point, I'm sure staying on Dropbox is looking like a real possibility...

## The solution
The solution to this problem is to create a remote "Dropbox" like service, housed on your own server! Unfortunately, this method will not be free, but it's still cheaper than Dropbox! Plus it'll be much more reliable for keeping your devices always in sync! To start off, you need to buy a server to host your files on (if you don't own one already). This guide will be for Linux based servers (I'm using Ubuntu). I highly recommend [DigitalOcean](https://www.digitalocean.com/?refcode=160ceb9f7d71) as a host. They use SSD and are extremely reasonably priced. Did I mention they're blazing fast too? Okay, enough of the sales pitch.

Once you have your server ready to go, I recommend taking a few moments to configure your server's security. There's a quick and painless guide on securing a Ubuntu server [here](http://plusbryan.com/my-first-5-minutes-on-a-server-or-essential-security-for-linux-servers).

## Once your server is secured, let's install BitTorrent Sync!
We'll need to know whether our system is 32 or 64 bit. If you're not sure which to install, SSH into your server and run `file /sbin/init`.

### If the output contains `32-bit`
Then SSH into your server and run: `curl -L http://download-lb.utorrent.com/endpoint/btsync/os/linux-i386/track/stable > btsync.tar`

### If the output contains `64-bit`
Then SSH into your server and run: `curl -L http://download-lb.utorrent.com/endpoint/btsync/os/linux-x64/track/stable > btsync.tar`


Now let's go ahead and extract the files from the tar by running `tar -xvf btsync.tar`. This should leave you with two files: `btsync` and `LICENSE.TXT`. You can go ahead and remove the license file if you'd like (`sudo rm LICENSE.TXT`). To keep things clean, I'm going to place the btsync executable in `/BTSync/` and put the folders I want to sync inside `/BTSync/folders/`.

To create this file structure, just run `sudo mkdir -p /BTSync/folders/`, which will create both directories. Then we can move the btsync executable to the folder by running `sudo mv btsync /BTSync/`.

Next, we're going to make the btsync process auto-start when our server boots. So run `sudo nano /etc/rc.local` and add in `/BTSync/btsync` on any line before `exit 0`.

At this point we're almost done! You can startup BTSync by running `sudo /BTSync/btsync`. Once it starts running, navigate to http://yourserver:8888. After creating your username and password, you can begin adding your BTSync folders!

## A BTSync usage guide for the newcomers
If I left you a little confused after the last section, no worries! I'm here to hold your hand and guide you through the wonderful world of BitTorrent Sync! If you haven't already, download and install [BitTorrent Sync](http://labs.bittorrent.com/experiments/sync.html) on your local computer. Once you launch the program, you'll see a window where you can add in folders to sync. It will look like this, only blank

{% include image.html url="/media/2013-10-15-create-dropbox-file-host-using-bittorrent-sync/btsync-folderwindow.png" description="BitTorrent Sync Mac Folder Menu" %}


Click the + button in the bottom left to add a new folder to sync.

{% include image.html url="/media/2013-10-15-create-dropbox-file-host-using-bittorrent-sync/btsync-add-folder.png" description="BitTorrent Sync Mac Add Folder" %}

You're going to want to generate a new shared secret and then choose the folder you want to sync to your server. In this example, I'm going to sync a folder for a project I'm working on.

{% include image.html url="/media/2013-10-15-create-dropbox-file-host-using-bittorrent-sync/btsync-add-folder-8bit.png" description="BitTorrent Sync Mac Add Folder Complete" %}

Once the folder is added, it'll show up inside your folder list.

{% include image.html url="/media/2013-10-15-create-dropbox-file-host-using-bittorrent-sync/btsync-folder-list-new.png" description="BitTorrent Sync Mac Updated Folder List" %}

Now right-click on the folder from this list and choose "Copy Secret". Before we can add this to our server, we need to create the folder it'll sync to! So SSH into your server and run `sudo mkdir /BTSync/folders/my-folder-name/`. At this point we're going to navigate back to our server's BTSync interface, which is located at http://yourserver:8888 and click the "Add Folder" button. Paste in the secret you copied and select the folder you just created.

{% include image.html url="/media/2013-10-15-create-dropbox-file-host-using-bittorrent-sync/btsync-add-remote-folder.png" description="BitTorrent Sync Mac Add Remote Folder" %}

It'll immediately add the folder and start syncing with your computer. Congratulations, you've now created a remote cloud that syncs with your home computer! You can now add this folder on any computer or mobile phone by downloading the app and using the secret key!

## So what's next?
This is usually the part where I say, "Thanks for reading" and blah blah blah. But this guide isn't just for creating a cloud server that's always on and constantly syncing (even though it's pretty awesome!), this guide is for replacing Dropbox! So what does Dropbox have that our cloud server doesn't? A public folder! People love that you can just drag and drop a file into your Dropbox's public folder to quickly share files with co-workers, friends, family, or colleagues.

Before continuing, I recommend setting up a public domain that you can access the server from. There's a good guide for setting that up [here](https://www.digitalocean.com/community/articles/how-to-set-up-apache-virtual-hosts-on-ubuntu-12-04-lts).

Once you have that setup, we're going to add a folder just like before! Only now, from the BitTorrent Sync web interface, you're going to select a directory that's located inside your `public_html` folder! Now when you add files into your local directory, your friends can download them by going to http://yourdomain.com/public_sync_folder/file.zip


## I think I can call this guide complete now
So now I'm at the boring end segment of my guide. I hope you guys learned something from this guide, and I hope that you enjoy your brand new private Dropbox service! If you need more help setting it up or you ran into a problem/error, just leave a comment below and I'll help you as soon as possible!


#### Thanks for reading.
