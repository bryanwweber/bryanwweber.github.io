---
layout: post
title: How to install new Python wheels on Windows 7
date: 2015-03-20 10:39
categories:
- Personal
---
Christopher Gohlke's website for Python packages for Windows (he hosts many, but the most popular are probably numpy and scipy) now distributes wheels instead of exe files.
This means we need the most recent version of pip and a new procedure to install them.
Here's a procedure I use to simplify installing dependencies.
<!--more-->

First, create a new folder to store all of the files in; I put mine in `C:\Users\user\Documents\python-upgrades`.
Then, go to Christopher's site and download all of the packages you need and put them in the folder you just created.
Now, open any text editor and create a file called `requirements.txt`.
The contents of that file should be a list of all the packages you downloaded; for instance, mine looks like:

    Cython
    scipy
    numpy
    tornado
    matplotlib
    requests
    pyparsing
    lxml
    Pillow

Then, pop open a command window and change to the directory you created.
Finally, run the command

    pip install --upgrade -r requirements.txt --no-index -f . --no-deps

This should look up all the wheel files in the current directory while ignoring PyPI.
