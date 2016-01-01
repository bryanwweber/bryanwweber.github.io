---
layout: post
title:  How to build a package installer on OS X for the Cantera MATLAB interface
date:   2016-01-01 13:27
categories: Personal
---
To make it easier to install certain portions of Cantera onto Macs, rather than having to install XCode and build from the source, it is possible to create an installer package.
These instructions document how to do so for the MATLAB interface portion only.
The user who wishes to actually build the installer will, of course, require XCode.
However, downstream users shouldn't need it.
<!--more-->


First, build Cantera including the MATLAB interface using the standard Cantera building instructions.
The only changes should be that a prefix should be set, for example, into a directory called `~/testing`, and the layout option should be specified as `compact`.
Then, run the builder and installer.

Next, create a build directory, change into it, and build the sub-packages to contain the data files for Cantera and the MATLAB interface files

    $ pkgbuild --install-location cantera/data --root ~/testing/data --identifier org.cantera.pkg.cantera-data ./cantera-data.pkg
    $ pkgbuild --install-location cantera/matlab --root ~/testing/matlab --identifier org.cantera.pkg.cantera-matlab-interface ./cantera-matlab-interface.pkg

The command line switches here are

- `--install-location`: Specify the relative install directory, relative to the root directory given when the user installs the package
- `--root`: Specify the root folder containing the files to be packaged up
- `--identifier`: A unique identifier for the package

Then, to make sure that the interface is automatically added to MATLAB's path, we need to create a script to modify `startup.m`.
This script should be called `postinstall` and placed in `testing/startupupdate/scripts/`

    #!/bin/sh

    # $2 is the install location, which is ~ by default, but which the user can
    # change.
    PREFIX=$2

    # This directory should be created when MATLAB is installed
    MATLAB_STARTUP="${HOME}/Documents/MATLAB/startup.m"

    cp -fp $MATLAB_STARTUP ${MATLAB_STARTUP}-cantera.bak

    echo "
    Adding Cantera to MATLAB Path in ${MATLAB_STARTUP}

    For this change to become active, you have to restart MATLAB.
    "
    echo "
    % added by Cantera installer
    path('${PREFIX}/cantera/matlab/toolbox', path)
    path('${PREFIX}/cantera/matlab/toolbox/1D', path)
    adddir('${PREFIX}/cantera/data)'" >> $MATLAB_STARTUP

    exit 0

Then, build the package to contain the postinstall script

    $ pkgbuild --nopayload --scripts ~/testing/startupupdate/scripts/ --identifier org.cantera.pkg.startupupdate ./cantera-startupupdate.pkg

The extra options here are:

- `--nopayload`: There are no files that will be installed with this package
- `--scripts`: The location of any scripts that should be run by this package when it is installed

OS X installer packages require a Distribution file, which is basically an XML file that specifies the options for the installer.
Documentation for this file can be found at [Apple's Developer website](https://developer.apple.com/library/mac/documentation/DeveloperTools/Reference/DistributionDefinitionRef/Chapters/Introduction.html).
The contents of this file for my purposes are

    <?xml version="1.0" encoding="utf-8" standalone="no"?>
    <installer-gui-script minSpecVersion="1">
        <pkg-ref id="org.cantera.pkg.cantera-data"/>
        <pkg-ref id="org.cantera.pkg.cantera-matlab-interface"/>
        <pkg-ref id="org.cantera.pkg.startupupdate"/>
        <options customize="allow" require-scripts="false"/>
        <choices-outline>
            <line choice="default">
                <line choice="org.cantera.pkg.cantera-data"/>
                <line choice="org.cantera.pkg.cantera-matlab-interface"/>
                <line choice="org.cantera.pkg.startupupdate"/>
            </line>
        </choices-outline>
        <choice id="default" title="Cantera Matlab Interface"/>
        <choice id="org.cantera.pkg.cantera-data" visible="false">
            <pkg-ref id="org.cantera.pkg.cantera-data"/>
        </choice>
        <pkg-ref id="org.cantera.pkg.cantera-data" version="0" onConclusion="none">cantera-data.pkg</pkg-ref>
        <choice id="org.cantera.pkg.cantera-matlab-interface" visible="false">
            <pkg-ref id="org.cantera.pkg.cantera-matlab-interface"/>
        </choice>
        <pkg-ref id="org.cantera.pkg.cantera-matlab-interface" version="0" onConclusion="none">cantera-matlab-interface.pkg</pkg-ref>
        <choice id="org.cantera.pkg.startupupdate" visible="true" title="Modify startup.m" description="Modify or add a startup.m file for MATLAB. If you do not do this, you will have to create your own startup.m file">
            <pkg-ref id="org.cantera.pkg.startupupdate"/>
        </choice>
        <pkg-ref id="org.cantera.pkg.startupupdate" version="0" onConclusion="none">cantera-startupupdate.pkg</pkg-ref>
        <domains enable_anywhere="true" enable_currentUserHome="true" enable_localSystem="false"/>
        <title>Cantera Matlab Interface</title>
        <license file="license.txt"/>
        <product id="Cantera Matlab Interface"/>
    </installer-gui-script>

Finally, we need to put all the packages together into the total installer package

    $ productbuild --distribution ./Distribution --resources ./Resources/ ./Cantera.pkg

After this, it should be a double-click install procedure. Easy!
