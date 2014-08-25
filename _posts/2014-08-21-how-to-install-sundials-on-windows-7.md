---
layout: post
title: How to build Sundials on Windows 7
date: 2014-08-21 15:33
categories:
- Personal
---

[SUNDIALS](http://computation.llnl.gov/casc/sundials/main.html) is a SUite
of Nonlinear and DIfferential/ALgebraic equation Solvers. It is useful for
many problems, and is needed to perform sensitivity analysis in Cantera.
It can be a pain to install on Windows, so here is my procedure for installing
on Windows 7 x64.
<!--more-->

First, download the [Windows SDK 7.1][1] and the [SP1 compiler update][2].
Installation should be a "Next->Next" affair, but if the install fails,
[The Mathworks recommends][3] the following steps:

1. Uninstall any Visual C++ 2010 Redistributable packages
2. Install the SDK again, but uncheck the options for the compiler and the Visual C++ Redistributable
3. Install the compiler update, which will install the compilers
4. Reinstall the Visual C++ Redistributable from [this link](http://www.microsoft.com/en-us/download/details.aspx?id=14632)

If you would like to have Visual Studio installed in addition to the SDK, the instructions
[here](http://blogs.msdn.com/b/vcblog/archive/2011/03/31/10148110.aspx) give the proper
order to install everything.

Next, download and install CMake from http://cmake.org/cmake/resources/software.html
To properly install SUNDIALS, CMake 2.8.12.2 is required.
Then, download SUNDIALS from http://computation.llnl.gov/casc/sundials/main.html
You will need 7zip to extract the tarball on Windows, which can be found here: http://www.7-zip.org/

Extract the tarball to the root of the `C:\` drive, so you have a folder `C:\sundials-2.5.0`.
Create new folders called `C:\sundials-2.5.0-build` and `C:\sundials-2.5.0-install`.
In the `C:\sundials-2.5.0` folder is a file called `CMakeLists.txt`. Open that file,
and change `SET(PACKAGE_STRING "SUNDIALS 2.4.0")` to `SET(PACKAGE_STRING "SUNDIALS 2.5.0")`.
Do the same for the line `SET(PACKAGE_VERSION "2.4.0")` to `SET(PACKAGE_VERSION "2.5.0")`.
Open the Windows SDK 7.1 command line interface and build and install SUNDIALS:

    cd C:\sundials-2.5.0-build
    cmake ..\sundials-2.5.0 -G "NMake Makefiles" -DCMAKE_INSTALL_PREFIX=C:\sundials-2.5.0-install
    nmake install
    
That should be it - SUNDIALS is now installed in the `install` directory. Happy solving!

[1]: http://www.microsoft.com/en-us/download/details.aspx?id=8279
[2]: http://www.microsoft.com/en-us/download/details.aspx?id=4422
[3]: http://www.mathworks.com/matlabcentral/answers/95039-why-does-the-sdk-7-1-installation-fail-with-an-installation-failed-message-on-my-windows-system
