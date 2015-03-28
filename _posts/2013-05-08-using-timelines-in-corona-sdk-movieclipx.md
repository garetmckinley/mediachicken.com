---
layout: post
title:  "Using Timelines in Corona SDK (MovieClipX)"
date:   2013-05-08 12:08:00
category: app review
tags: animations, corona sdk, image sequence, movieclip, movieclipx, sprite sheets, timelines
---

A little over a year ago I released a tool that extended Corona SDK's MovieClip library, in a sense it originally was just adding another layer of manipulability. Allow me to illustrate in flowcharts.
<h2>The original library</h2>
Here was how the original MovieClip library worked,

{% include image.html url="/media/2013-05-08-using-timelines-in-corona-sdk-movieclipx/Timeline-flowchart.001.jpg" description="Timeline flowchart" %}

As you can see, every animation was it's own object. That means that if you wanted to make a walk animation and a run animation for your character, MovieClip would force you to create two separate objects and handle the toggling of visibility yourself.
<h2>MovieClipX was born...</h2>
I knew that wasn't a good solution. It makes for messy and repetitive code, and I'm a stickler for clean code. So that spawned my idea for MovieClipX

{% include image.html url="/media/2013-05-08-using-timelines-in-corona-sdk-movieclipx/Timeline-flowchart.0021.jpg" description="Timeline flowchart" %}

&nbsp;

This already appears to be a better solution! With my library you can house <strong>unlimited</strong> animations inside a single MovieClipX object and switch animations with one line of code! It also adds one more level of control, you can edit your animation parameters on a per-animation basis or manipulate the parameters for an entire MovieClipX object!
<h2>Then came Timeline!</h2>
But then last week, I had one more epiphany on how to make this library better...

{% include image.html url="/media/2013-05-08-using-timelines-in-corona-sdk-movieclipx/Timeline-flowchart.0031.jpg" description="Timeline flowchart" %}

&nbsp;

Now we have a final level of manipulability, the timeline object. Timelines work sort of like MovieClipX objects; you create them, add MovieClipX objects inside them, then can manipulate time for multiple MovieClipX objects at once! This is useful for pausing multiple animations at once, fast forwarding time, or slow-motion!

Now that you've gotten a little rundown on how timelines work, time to roll up your sleeves and start coding!
<h2>The tutorial</h2>
If you're familiar with MovieClipX already, feel free to skim through this tutorial while making notes of the changes with Timeline. This tutorial is assuming you have no knowledge of MovieClipX, but knowledge of using Corona SDK.

Make sure you're running MovieClipX build 2013.215 or higher. If not, download from <a title="Download MovieClipX" href="http://igaret.com/movieclipx/download" target="_blank">here</a>.

In this tutorial I'm going to refer to the MovieClipX library as mcx and MovieClipX Object as mcxObject.
<h2>Setting up MovieClipX</h2>
First off, you're going to want to include the library

{% highlight lua %}
require("mcx")
{% endhighlight %}

<h2>Creating your animations</h2>
Then you'll need to create a few mcxObjects, for this tutorial I'm going to create <strong>john</strong> and <strong>tom</strong>.

{% highlight lua %}
john = mcx.new()
tom = mcx.new()
{% endhighlight %}

To continue, there's a few different options; if your animation is stored in an image sequence (frame1.png, frame2.png,etc) then you can do the following

{% highlight lua %}
walk_left = mcx.sequence({name = "walk_left_", extension = "png", endFrame = 4, zeros = 3})
{% endhighlight %}

This is for a sequence of files named: walk_left_001.png, walk_left_002.png, etc. However, you can customize the parameters to meet your needs.
<ul>
    <li><span style="line-height: 13px;">Name = (Required) The prefix for the file</span></li>
    <li>Extension = (Required) The file extension</li>
    <li>startFrame = (Optional, default = 1) The start frame</li>
    <li>endFrame = (Required) The last frame</li>
    <li>zeros = (Optional, default = 0) The amount of leading zeros in the frame number.</li>
</ul>
However, if your animation files aren't saved sequentially, then you have to create your frames list in a table:

{% highlight lua %}
animation = {"frame1.png", "frame7.png", "pic39.png", "lastframe.gif"}
{% endhighlight %}

Now you can attach the frame table to an animation, like so:

{% highlight lua %}
john:newAnim("animation_name", frame_table, width, height)
tom:newAnim("animation_name", frame_table, width, height)
{% endhighlight %}

The animation name is important, that's how you call the animation when you want to play or switch animations. You can add as many animations to <strong>John</strong> and <strong>Tom</strong> as you'd like, but for this tutorial I'm just giving them each one animation. If you want to know more about setting up your animations, <a title="Using MovieClipX with your Corona SDK projects" href="http://igaret.com/tutorials/using-movieclipx-with-your-corona-sdk-projects" target="_blank">you can find an article about it here</a>.

Finally, to make them animate:

{% highlight lua %}
john:play({name = "animation_name"})
tom:play({name = "animation_name"})
{% endhighlight %}

Now if you run your project in the Corona Simulator, you should have two animating characters!
<h2>Creating and using Timelines</h2>
For this tutorial I'm only going to be using one timeline object, but it's important to note that you can have as many timelines in your project as you desire!

Using timeline is easy, let's create a timeline and add our friends <strong>John</strong> and <strong>Tom</strong>!

{% highlight lua %}
timeline = mcx.newTimeline()
timeline:addObject(john)
timeline:addObject(tom)
{% endhighlight %}

And we're ready to use it! Let's go ahead and make <strong>John</strong> and <strong>Tom</strong> move in slow-motion by using alterTime()

{% highlight lua %}
timeline:alterTime(mcx.halfSpeed())
{% endhighlight %}

alterTime() is a pretty slick function, it takes one argument which is a float value. You can either insert a float value or you can use the built-in speed controls, which are:
<ul>
    <li><span style="line-height: 13px;">mcx.normalSpeed()</span></li>
    <li>mcx.halfSpeed()</li>
    <li>mcx.doubleSpeed()</li>
</ul>
You can read about some of the other timeline functions on the <a title="MovieClipX Documentation" href="http://igaret.com/movieclipx/docs" target="_blank">docs page</a>.
<h2>In conclusion</h2>
I hope you learned something from this brief rundown on the new timeline functions! Most of all, I hope that MovieClipX can boost your productivity in Corona SDK!
