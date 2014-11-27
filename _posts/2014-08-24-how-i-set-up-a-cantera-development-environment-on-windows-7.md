---
layout: post
title: How I set up a Cantera development environment on Windows 7
date: 2014-08-24 09:46
categories:
- Personal
---
Setting up a development environment for Cantera on Windows 7 can be a little
trickier than on [Linux]({% post_url 2014-01-08-installing-cantera-on-ubuntu-12.04.3-from-scratch-source-with-Intel-compilers %}).
This post contains instructions for how I set up my development environment on Windows 7.
<!--more-->

The first step is to download the [SDK 7.1 compiler][1] and its [SP1 update][2].
Installation should be a "Next->Next" affair, but if the install fails,
[The Mathworks recommends][3] the following steps:

1. Uninstall any Visual C++ 2010 Redistributable packages
2. Install the SDK again, but uncheck the options for the compiler and the Visual C++ Redistributable
3. Install the compiler update, which will install the compilers
4. Reinstall the Visual C++ Redistributable from [this link](http://www.microsoft.com/en-us/download/details.aspx?id=14632)

If you would like to have Visual Studio installed in addition to the SDK, the instructions
[here](http://blogs.msdn.com/b/vcblog/archive/2011/03/31/10148110.aspx) give the proper
order to install everything.

If you only have the SDK and its update installed, Microsoft has not-so-helpfully
removed a file that is necessary to build Cantera, called `ammintrin.h`. There is a
post [at The Mathworks][4] forum with a link to the file, and I'll also post it
[here][5] for reference. Add this file to the `C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\include`
directory, and it should be all set. If you have Visual Studio installed,
this will not be a problem.

Next, install [SUNDIALS](http://computation.llnl.gov/casc/sundials/main.html) (I've helpfully
posted some instructions [here]({% post_url 2014-08-21-how-to-install-sundials-on-windows-7 %})).
Then, download and unzip the Boost libraries: <http://www.boost.org/>
I recommend unzipping into the root of the `C:\` drive, so there will be a folder called
`boost_1_56_0` (for the most recent version as of this writing) with all the required files inside.
Note that if you're not careful, you'll get a folder `C:\boost_1_56_0\boost_1_56_0`, which
is not what we want, it should be just `C:\boost_1_56_0\<files go here>`.

Now we need other components of the development environment, particularly Python
and all its packages. The most recent versions of Python are 2.7.8 and 3.4.1, which
can be downloaded respectively [here][py278] and [here][py341]. Make sure to get the
proper version for your operating system (32-bit or 64-bit).
Installation into the default directories is preferable, and make sure
to have the python.exe added to your path.

If you forget to add python.exe to your path
in the installer, open the System control panel (<kbd>Win</kbd>+<kbd>Pause</kbd>), choose
"Advanced System Settings" in the left panel, then choose the "Advanced" tab, and at the
bottom click "Environment Variables". In the "System variables" box, find "Path" and add
`C:\Python34;C:\Python34\Scripts;C:\Python27;C:\Python27\Scripts;` to the front of the
text box.

While we're here, we need to add one environment variable. Click "New", and in the
first text box add `VS90COMNTOOLS` and in the second box add `%VS100COMNTOOLS%`. This
sets the variable called `VS90COMNTOOLS` to be equal to the value of the variable called
`VS100COMNTOOLS`. `VS100COMNTOOLS` is set by the SDK when it is installed, but Python 2
depends on `VS90COMNTOOLS` being installed. This allows us to install certain packages
with `pip` in Python 2. Note that not all packages will work with this trick (in particular,
`matplotlib` can't be installed with `pip` this way).

Python 3.4 comes with `pip` installed, but 2.7 does not, plus we need some other packages anyways.
Head to [Christopher Gohlke's page](http://www.lfd.uci.edu/~gohlke/pythonlibs/) and download
the following packages. Make sure to get the correct bitness for your Python versions.

2.7:

-   [`setuptools`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools)
-   [`pip`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip)
-   [`numpy`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)
-   [`cython`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#cython)
-   [`scons`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scons)

3.4:

-   [`numpy`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)
-   [`cython`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#cython)

Install these after you install Python.
Now, open the "Windows SDK 7.1 Command Prompt" (searching for 7.1 in the Start Menu search
box usually brings it up) and install some additional packages for Python with the following command:

    pip2 install sphinxcontrib-matlabdomain sphinxcontrib-doxylink 3to2

This will fetch all the Python packages required to build the documentation and the package (3to2) to
convert the examples from Python 3 syntax to Python 2 syntax.

You should also install Doxygen at this point, so that the C++ documentation can be built.
The Windows installer for the most recent version of Doxygen (at the time of this writing, 1.8.8)
is available on [SourceForge](http://sourceforge.net/projects/doxygen/files/rel-1.8.8/doxygen-1.8.8-setup.exe).
Finally, install the [WiX Toolset](http://wixtoolset.org/) so that MSI installers for Cantera
can be built.

That should (finally) be all the software needed to get up and running in developing Cantera.
The last thing to do is actually get the Cantera source code.
There are several ways to get the code; my preferred way is to use GitHub.
Ray Speth has a clone of the main Cantera repository on GitHub: <https://github.com/Cantera/cantera>.
What you should do is create a fork of this project into your own personal GitHub account.
This way, you can add branches, do all your work, push them to your forked repository,
and create a pull request so that Ray can see the code and help you improve it.
Then, either use the [GitHub for Windows](http://windows.github.com) client, or clone
the repository yourself.

Once in the main Cantera directory, we need to tell SCons how to build Cantera.
Create a file called `cantera.conf` and put as its contents:

    msvc_version = '10.0'
    python_cmd = 'C:/Python27/python.exe'
    python3_cmd = 'C:/Python34/python.exe'
    matlab_path = 'C:/Program Files/MATLAB/R2014a'
    sundials_include = 'C:/sundials-2.5.0-install/include'
    sundials_libdir = 'C:/sundials-2.5.0-install/lib'
    env_vars = 'all'
    boost_inc_dir = 'C:/boost_1_56_0/'

Now, `scons build` and `scons msi` should work. If you get errors, read on.

<s>The first warning you might see is that 3to2 is not installed properly, even
though we installed it earlier. This is because the SConstruct file calls <code>3to2</code>
as an executable, which doesn't work on Windows. The fix for this is to edit
two lines, one in the root <code>SConstruct</code> file, one in the <code>interfaces/cython/SConscript</code>
file. First, in <code>SConstruct</code> change:

<pre><code>ret = getCommandOutput('3to2','-l')</code></pre>

to

<pre><code>ret = getCommandOutput(env['python_cmd'], 'C:/Python27/Scripts/3to2','-l')</code></pre>

Then, in <code>interfaces/cython/SConscript</code>, change:

<pre><code>subprocess.call(['3to2', '--no-diff', '-n', '-w','-x', 'str',</code></pre>

to

<pre><code>subprocess.call([env['python_cmd'], 'C:/Python27/Scripts/3to2', '--no-diff', '-n', '-w','-x', 'str',</code></pre>

Note that these are basically hacks until the problem can be fixed in the source.</s>

As of [revision 3113](https://code.google.com/p/cantera/source/detail?r=3113), this problem has been fixed.

Second, you may get actual errors when trying to build the MATLAB interface
(if you aren't building this interface, you might not see this error).
In case you get an error in the MATLAB interface about redefining `_char16t`,
open `scr/matlab/ctmatutils.h` and comment out lines 12-14. These lines
were introduced to fix some problems in MATLAB R2010a, and aren't required
for at least R2013a and R2014a.

[1]: http://www.microsoft.com/en-us/download/details.aspx?id=8279
[2]: http://www.microsoft.com/en-us/download/details.aspx?id=4422
[3]: http://www.mathworks.com/matlabcentral/answers/95039-why-does-the-sdk-7-1-installation-fail-with-an-installation-failed-message-on-my-windows-system
[4]: http://www.mathworks.com/matlabcentral/answers/90383-fix-problem-when-mex-cpp-file
[5]: {{ site.baseurl }}/files/2014/08/ammintrin.h
[py278]: https://www.python.org/download/releases/2.7.8/
[py341]: https://www.python.org/downloads/release/python-341/
