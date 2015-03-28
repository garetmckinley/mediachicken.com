---
layout: post
title:  "Using MovieClipX with your Corona SDK projects"
date:   2012-07-06 16:52:00
category: app review
tags: corona sdk, library, lua, movieclip, movieclipx
---

As an aspiring (for now) game developer, I spend a lot of time researching and experimenting with various engines. As many of you can probably tell from my site, a tool I use often is Corona SDK. It's an <strong>amazing</strong> game engine for both the iOS &amp;  Android platforms. It's getting fairly large now, however its still relatively new compared to other engines. That being said, there's a few features missing. The great news is, the community is completely awesome at filling in the gaps via external libraries and/or 3rd party tools.

My contribution to the community is the MovieClipX library (aka: mcx). If you've ever used the movieclip library for Corona SDK you should have a good idea what movie clips are. If not, let me take a moment to explain.

There's two ways you can animate an object in Corona SDK: you can use what's called a sprite sheet, which is basically a large tiled image used for storing all animations on a single image; or you can use separate images for each frame.

Now, movieclips are generally a little slower to load; mostly because you're loading a file for every frame. However after it loops once, the images should all be cached in the ram and load fast. The reason you'd use these over sprites, is if you have a ton of animations and they can't fit on a single image.

The shortcoming of the generic movieclip library however, is the fact that you can only store one animation per movieclip object, you can't control the speed of the animation, and it doesn't work with resolution independence (à la iPhone retina screen and iPhone non-retina).

That's why I essentially "filled in the gaps" with my MovieClipX library. And now I've given you the ability to use my library for free. But first, let me teach you how to use the library to its full potential.
<h2>First off, get the library</h2>
The first and probably most logical step would be to download the library, heh. So go ahead and download it here, from github: <a title="MovieClipX Library" href="https://github.com/mediachicken/MovieClipX">mediachicken/MovieClipX</a> (click the "zip" button with a cloud on it to download the library).
<h2>Oh boy, there's a lot of files! What now!?</h2>
Woah there, calm down. We've only just begun! The only <em>real</em> important file here is the <span style="text-decoration: underline;"><strong>mcx.lua</strong></span> file. So go ahead and copy that file over to your project folder before continuing. If you learn better by example, there's a few example projects in the MovieClipX folder. I try to keep examples always up to date with the latest functions in the library, so they're as good as a tutorial!
<h2>Time to roll up your sleeves, it's coding time!</h2>
The first step into using the MovieClipX library would be to include it into your project. Now there's a lot of different styles of setting up your project, but for the sake of simplicity in this tutorial I'm going to assume that your entire project takes place in your <span style="text-decoration: underline;"><strong>main.lua</strong></span> file. So when I reference your main.lua file, I'm referring to the file you're using my library in.

Including MovieClipX is the same as including any other library in Corona SDK.
{% highlight lua %}require("mcx"){% endhighlight %}
That was easy enough, right? Now here's where I need to clear up some confusion. The original movieclip library creates a new object for every animation; and let me tell you, it gets messy. My library uses what I call <span style="text-decoration: underline;"><strong>mcx objects</strong></span>. So when you hear me mention mcx objects, I'm talking about the "container" that holds all the animations for a single object.

Some examples would be, for a player sprite you'd have a single mcx object with an animation inside for walking, jumping, crouching, and whatever other awesome animations you've conjured. It's a much cleaner method than movieclip's constant hide/show different objects based on the current animation.

So then, let's create a new mcx object for our character using the <span style="text-decoration: underline;"><strong>new()</strong></span> function.
{% highlight lua %}char = mcx.new(){% endhighlight %}
Now as you see, we named our character object <span style="text-decoration: underline;"><strong>char</strong></span>. You can name yours whatever you want, but for the sake of the tutorial we'll use that as the character's name. So now we have a new mcx object. This works exactly like any other Corona SDK object. You can add physics to it, move it, spawn it, destroy it, etc. But first, let's go ahead and add some animations to it.
{% highlight lua %}char:newAnim("walk_left", {"walk_left_001.png",
             "walk_left_002.png",
             "walk_left_003.png",
             "walk_left_004.png"}, 96, 96, 5){% endhighlight %}
Okay, let's take a moment to dissect exactly what we just did there. So the first argument in the newAnim() function is the name of the animation. This is very important as you'll be using this name to call the animation later on, so make sure it's a memorable and descriptive name. The next argument is a Lua table object which will store all of our frames for the animation. This is fairly self-explanatory, so knock yourself out. There's no limit to the amount of frames you have. The next two arguments are going to be the width and height for the animation. Remember, all frames <strong>must</strong> be the same size. Finally, the last argument is the speed of the animation. The lower the number, the slower the animation is. 5 is usually a good medium for most animations.

So if you have multiple animations, now is the time to go ahead and add them all in. Make sure each one has a unique name! Once you're done, go ahead and continue below.

So now that we have a character that has animations, let's make him walk!
{% highlight lua %}char:play("walk_left"){% endhighlight %}
Hopefully that's a pretty self-explanatory function! The only argument in play() is the name of the animation you want to play. Here's an extra tip, the argument inside the play function is only required the first time you're playing. If you call play() anywhere else in your code with no animation name, it'll simply resume the last played animation.

So you're now able to play an animation! If you want to change animations, just put the play function somewhere else with another animation name!

So what if we want him to stop animating when we touch him? No problem!
{% highlight lua %}function touchEvent(event)
    if event.phase == "ended" then
        char:togglePause()
    end
end
char:addEventListener( "touch", touchEvent ){% endhighlight %}
The togglePause() function does exactly what it sounds like, it toggle between the play state and the paused state.
<h2>In conclusion,</h2>
I really hope you were able to learn something from this tutorial, and I truly hope you find my MovieClipX library to be helpful with your Corona SDK projects! If you want to know more about the various functions, read about them on the GitHub ReadMe page <a href="https://github.com/mediachicken/MovieClipX/blob/master/README.md#movieclipx">here</a>. If you have any issues or bugs to report, do that <a href="https://github.com/mediachicken/MovieClipX/issues?state=open">here</a> (or leave a comment below, but the GitHub page is the more appropriate place to put issues).

Thanks for reading! If you found this tutorial useful; please, take the time to share the knowledge :)
