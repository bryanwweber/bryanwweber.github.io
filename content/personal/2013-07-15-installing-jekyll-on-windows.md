---
title: Installing Jekyll on Windows
category: personal
date: 2013-07-15
---

Been trying to migrate this site to use Jekyll ([http://jekyllrb.com](http://jekyllrb.com)) today and finally got it working with Pygments for code highlighting.
<!--more-->

Following the tutorial here: [Running Jekyll on Windows](http://www.madhur.co.in/blog/2011/09/01/runningjekyllwindows.html)

<del>I installed Ruby and the dev kit as suggested.</del>

**Update:** How to install Ruby on Windows: Because Windows makes it a pain to manage dependencies, it is more difficult to install development
software on Windows. However, the nice folks at [Ruby Installer](http://rubyinstaller.org) have created the installers for Windows for us.
I downloaded the [Ruby-2.0.0-p353 (x64)](http://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-2.0.0-p353-x64.exe?direct) (EXE) installer
and the [Dev Kit mingw64](http://cdn.rubyinstaller.org/archives/devkits/DevKit-mingw64-64-4.7.2-20130224-1432-sfx.exe) (EXE) installer. Make sure
to check the box to add the Ruby executable to your PATH in the installer.

My installation directories were the default for Ruby and <code>C:\dev kit</code> for the dev kit. Then, the simple commands
{% highlight bat %}
cd "C:\dev kit"
ruby dk.rb init
ruby dk.rb install
gem install jekyll
{% endhighlight %}
built the dependencies and installed Jekyll. To get the code syntax highlighting working, we need [Python](http://www.python.org) and pip (the Python package manager). The directions in the previously listed tutorial provide a work-around to be able to use Python 3 <em>but this work-around no longer works!</em> Jekyll has switched to using the pygments.rb gem instead of the albino.rb gem. pygments.rb is only compatible with Python 2.x. Therefore, you must install [Python 2.x](http://www.python.org/download/) (I used 2.7.5). After Python is installed (the default directory `C:\Python27` is good), download setup_tools and pip from here:

* [`setup_tools`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools")
* [`pip`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip)

Make sure you download the version for the right Python! Then, the installers should automatically find the correct Python install. Credit for the simple solution goes to Colonel Panic at StackOverflow: [How to install pip on Windows](http://stackoverflow.com/a/12476379/2449192). Also, we don't need to worry about a C++ compiler for the package we'll be installing, but if you intend to make more general usage of pip, you may need a C++ compiler.

Once `setup_tools` and `pip` are installed, you need to add the directory where you installed `pip` to the `PATH` variable. To do this, right click on My Computer (either on the desktop or in the start menu), click Properties, then in the left column click Advanced System Settings, then at the bottom of the next window click Environment Variables. In this window, there are two variables we need to change. The first is in the User section, called `PATH` or `Path`. Click this variable, then edit, and add the directory to your `pip` install at the front of the text box. If you accepted all the defaults, this directory will be `C:\Python27\Scripts;` add it to the `PATH` and make sure the semicolon is in there to separate this entry from the next. Then, we need to add the Python directory itself to the System PATH, so go to the System box below the User box and same procedure, except the path to be added is `C:\Python27;`. If you already have Python 3 installed, make sure that the Python 2 entry appears to the left of the Python 3 entry; otherwise, Jekyll will try to use Python 3 by default because it searches the directories from left to right to find the file it is looking for.

Now, restart the Windows command line, and type `pip install Pygments`

Finally, Jekyll is installed with support for code highlighting. To test, in your command line type
{% highlight bat %}
cd "C:\Users\_User_\Documents" & ::Where _User_ is your user name
jekyll new myblog
cd myblog
jekyll serve -w
{% endhighlight %}

You can now open a browser window to `localhost:4000` and your (default) Jekyll webpage should open! Feel free to make changes to the markdown and css, and Jekyll should automagically update the site if you refresh your browser.

Update: If the command `jekyll serve -w` isn't working with the error `Liquid Exception: No such file or directory...` you may need to downgrade the pygments.rb gem. First, edit your `_config.yml` file for the site and set the Pygments option to false, then try to start the server again. If everything works, you need to downgrade. Following the SO question [here](http://stackoverflow.com/questions/17364028/jekyll-on-windows-pygments-not-working), type
{% highlight bat %}
gem uninstall pygments.rb --version "=0.5.1"
gem install pygments.rb --version "=0.5.0"
{% endhighlight %}
and reset the Pygments option in `_config.yml` to true to get it working.
