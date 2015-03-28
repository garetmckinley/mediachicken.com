---
layout: post
title:  "Check internet connection In Corona SDK"
date:   2013-10-03 15:09:00
category: app review
tags: check, corona sdk, internet connection, varify, validate, lua, library, network, test, tutorial, code
---

## Why Check The User's Internet Connection?
There are many reasons why you'd want to check your user's internet connection status in Corona SDK. The most obvious reason would be if you were going to perform an action such as loading a web page or an advertisement. It would have a negative impact on the user to display a blank webpage in your app because the user had no internet connectivity, wouldn't you agree? It's much more professional to check for a connection first, then either alert the user that internet connectivity is required or simply enable offline mode in your app.

So today we're going to fix that! I've written a simple function in the form of an external library that you can add to your project to quickly check your user's internet connection!

## The library
Put the following code inside `testconnection.lua
{% highlight lua %}
---------------------------------------
-- Test connection to the internet
---------------------------------------
module(..., package.seeall)
local socket = require("socket")

function test()
    local connection = socket.tcp()
    connection:settimeout(1000)
    local result = connection:connect("www.google.com", 80)
    connection:close()
    if (result) then return true end
    return false
end
{% endhighlight %}

## Usage Tutorial
1. Include the library in your project by placing`connection = require("testconnection")` in the file you wish you test the connection in.
2. Simply use `if (connection.test()) then` to test for internet connection!
3. You can then add an `else then` statement to do something when it fails the internect connection test.

## In Conclusion
I hope this can help you speed up your development in Corona SDK! I know it's a simple function, but it's very useful if your project requires internet connectivity! Leave me a comment below if you have any problems or need help using it in your project.
