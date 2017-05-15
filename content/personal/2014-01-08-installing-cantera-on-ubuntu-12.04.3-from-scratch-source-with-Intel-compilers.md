title:  Installing Cantera on Ubuntu 12.04.3 from scratch/source with Intel compilers
date:   2014-01-08 17:09
categories: personal

# Table of Contents:

[Update](#Update)  
[Introduction](#Introduction)  
[Install Intel Compilers](#InstallIntelCompilers)  
[Install Dependencies](#InstallDependencies)  
[Install NumPy/SciPy](#InstallNumpyScipy)  
[Install Boost](#InstallBoost)  
[Install Sundials](#InstallSundials)  
[Install Cantera](#InstallCantera)  


## UPDATE 01-01-2016 {#Update}

I have posted new instructions for how to build the developer's version of Cantera in a new post: [Installing Cantera on Ubuntu with Intel Compilers UPDATED!]({filename}2016-01-01-how-to-install-cantera-on-ubuntu-updated.md)

## Introduction {#Introduction}

My lab typically uses the CHEMKIN-Pro software from [Reaction Design](http://reactiondesign.com)
to perform simulations of our experiments. Unfortunately, CHEMKIN-Pro is closed
source and does not include a number of features I have found useful for my
research. Thus, my labmate and I have recently endeavored to install a separate
software package on our Ubuntu 12.04.3 server to perform these simulations.

This software is called [Cantera](http://cantera.github.io/docs/sphinx/html/index.html),
and is an open-source, C++-based "suite of object-oriented software tools" designed to
perform chemical and thermodynamic simulations. Although it was once rather difficult
to install, recent upgrades have improved the install and usage procedure drastically.
Cantera can be used from one of several interfaces - C++, Fortran, MATLAB, or Python.
Essentially, each of the interfaces allows the user to easily access the functions and
methods at the heart of Cantera and conduct their work without worrying about the details
of, say, how to calculate a reaction rate. On our server, we decided to install the C++,
Fortran, and Python interfaces. Unfortunately, the MATLAB interface is broken when using
the Intel compilers, due to problems with MATLAB itself. In fact, any MEX application
compiled with the Intel compilers will not work, so this is not Cantera's fault!

Despite the newly acquired ease of installation, we could not leave well enough alone
and decided to complicate things by using C, C++, and Fortran compilers distributed by
Intel, since our server has 24 Intel Xeon CPUs. Intel provides a number of options
with their compilers that enable Intel-compiled applications to run significantly faster
on Intel processors than applications compiled using other compilers (e.g. Gnu).

Note that in all the following steps, except where explicitly noted, I will assume that
you have `sudo` or root access. This is because some of the dependencies will be installed
in the `/usr/local/` folder, which requires root permissions to write to. If you do not
have root access, you will have to modify many of the below instructions, and I have tried
to note in a few places where the commands must be changed.

## Install Intel Compilers {#InstallIntelCompilers}

First we have to install some dependences for the Intel compilers. See
[here](http://software.intel.com/en-us/articles/using-intel-compilers-for-linux-with-ubuntu)
for more instructions.

```bash
sudo apt-get install build-essential gcc-multilib rpm openjdk-6-jre-headless
```

The next step is to install the Intel compilers themselves. My lab has a license to
the Intel Fortran and C/C++ compiler suites, which also include Intel's Math Kernal Library
(MKL). The MKL contains the LAPACK and BLAS implementations required by the solvers in
Cantera (and other software as well). If you are using the compilers for "non-
commercial software development", you can also download a copy of the Fortran and C/C++
compiler suites from [here](http://software.intel.com/en-us/non-commercial-software-development).
Included in the scripts are fairly standard installers - mostly you can go through them by
the "Next->Next->Next" method. If you get a warning that 32-bit dependencies are not
installed, go back to the step that lists all of the packages to be installed and choose
"Customize Installation" at the bottom-center of the window. Then, deselect "32-bit support"
since we will not be compiling any 32-bit applications.

Once the Intel compilers are installed, it is very important to add them to your PATH
environment variable. Intel helpfully provides a script to set all of the relevent variables
at once. You can source this script from your login script to allow easy access to the compilers.
On our server, this meant adding `source /opt/intel/bin/compilervars.sh intel64` to the `~/.profile`
file. On a desktop install, the better place to add this is in the `~/.bashrc` file

## Install Dependencies {#InstallDependencies}

Next, install (some) of the dependencies for Cantera and its dependecies. The server on which we
intended to install Cantera has a "well-loved" Ubuntu install, as in, many packages were already
installed. We were using the 4.4 versions of the GNU compilers but the default version of GCC for
Ubuntu 12.04 is 4.6. Despite that we will be using the Intel compilers for most of the stuff here,
in some cases the Intel compilers are little more than a wrapper around the GNU compilers. To easily
switch the entire system between compiler versions, use the built-in program
[`update-alternatives`](http://askubuntu.com/questions/233190/what-exactly-does-update-alternatives-do).

The following commands were tested on a fresh installation of Ubuntu 12.04.3 with GCC 4.6, with only package updates
and the Intel compilers installed (as shown above), so it should get anyone up and running.

A list of Cantera's dependencies can be found at the
[documentation site](http://cantera.org/docs/sphinx/html/compiling/dependencies.html).
The following dependencies from `apt-get` are required. This does not cover all of the dependencies
in the documentation, but we will be installing some others separately.

```bash
sudo apt-get install scons subversion python python-dev python3 python3-dev \
libsuitesparse-dev libbz2-dev libbz2-1.0 wget git git-svn swig
```
Not all of these dependencies are dependencies of Cantera itself; some of them are dependencies of
the dependencies.

With the `apt-get` installs out of the way, its time to move on to the Python dependencies. First up is
`pip`, which makes installing the other dependencies much easier. One note - if you do not have admin
access (i.e. `sudo` rights) on the particular machine you're using, be sure to specify the `--user` option
to all of the following `easy_install` commands (and you'll have to have gotten a sysadmin to do the previous steps).
The `--user` option will install the packages in the directory
`/home/username/.local/lib/pythonX.Y/site-packages`, which is editable by the user and thus doesn't require super-user rights.

```bash
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py \
-O - | sudo python3.2
sudo easy_install-3.2 pip
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py \
-O - | sudo python2.7
sudo easy_install pip
```

It is important to install for Python 3 first, because otherwise the executables of `easy_install` and `pip`
for Python 3 will overwrite those for Python 2, and forevermore you'll get unexpected behavior. Then, with
`pip` installed, we can do

    sudo pip install cython 3to2 nose ipython
    sudo pip3.2 install cython 3to2-py3k nose ipython
    #The following is only required if you want to build the Cantera documentation
    sudo pip install Sphinx pygments pyparsing sphinxcontrib-doxylink

## Install NumPy/SciPy {#InstallNumpyScipy}

A quick perusal of the list of dependencies shows that NumPy and SciPy are also required to use the
Python interface. If you would like to compile these with the Intel compilers, see
[here]({filename}2014-01-11-installing-numpy-scipy-on-ubuntu-12.04.3-from-scratch-source-with-intel-compilers.md).
If using GCC is OK with you, then `pip` should be good enough.

    sudo pip install numpy scipy
    sudo pip3.2 install numpy scipy

## Install Boost {#InstallBoost}

Now we come to the fun stuff. Its time to install some dependencies - from source! First up is
Boost. Ubuntu has a version of Boost in the repositories, but I found errors during the build
and/or test process of Cantera when I used the pre-compiled Boost libraries. This was apparently
due to the fact that they had been compiled with a different compiler. As of this writing, the
newest version of Boost is 1.55.0, but the absolute newest versions can be found at the
SourceForge download site: <http://sourceforge.net/projects/boost/files/boost/>

When you have downloaded the appropriate `.tar.gz` file, unzip it with the command

    tar -xzf boost_X_YY_Z.tar.gz

Then change to the appropriate directory (most likely `boost_X_YY_Z`), and run the following
commands

```bash
sudo -s
source /opt/intel/bin/compilervars.sh intel64
./bootstrap.sh --with-toolset=intel-linux
./b2 -a -q --link=shared --variant=release --address-model=64 \
    --compileflags="-xhost -fp-model precise -O3" -j2 \
    --threading=multi install
exit
```

Let's look at these commands.

1. Switch to the root terminal (if you don't have `sudo` permissions, see below)
2. Since the regular environment isn't passed to the root user, we have to setup the Intel compilers again.
3. Run the setup script `bootstrap.sh` to tell Boost which compiler we will use.
4. Run the install program that `bootstrap.sh` has created. The options (as far as I know them) are:
    - `-a`: Rebuild all targets, even if they're up-to-date
    - `-q`: Quit the build on the first error
    - `--link=shared`: Build shared libraries.
    - `--variant=release`: Build the release version. No idea if its required.
    - `--address-model=64`: Build 64 bit binaries. No idea if its required.
    - `--compileflags="..."`: Flags sent to the C and C++ compilers. These options are
        - `-xhost`: Add additional Intel specific optimizations
        - `-fp-model precise`: Use the `precise` floating point model
        - `-O3`: The optimization level to be used by the compiler
    - `-j2`: Specify the number of compile processes to run in parallel.
    - `install`: Install the libraries and headers
5. {:value=7} Exit root

If you don't have `sudo` privileges, you can use the option `--prefix=/path/to/install`. Make
sure that you have permissions to write to `/path/to/install`. The `--prefix` option should be
specified to `b2` I think - not sure about that, proceed at your own risk. If resources are tight,
you can add `--with-python --with-regex --with-system --with-thread` to install only the minimal
set of libraries that Cantera requires. Note also that these directions are somewhat different
than the ones provided at [the official documentation](http://www.boost.org/doc/libs/1_55_0/more/getting_started/unix-variants.html)
so proceed at your own risk.

## Install Sundials {#InstallSundials}

The next step is to install Sundials. Sundials is a suite of solvers and are used in Cantera
to enable sensitivity analysis. Technically, its optional, but we're going for all the bells
and whistles, so let's go for it. Download Sundials (as of this writing, the most recent
version is 2.5.0) from here: <http://computation.llnl.gov/casc/sundials/download/download.html>.
Similar to the Boost section, we untar the tarball

    tar -xzf sundials-X.Y.Z.tar.gz

Then change to the appropriate directory and run the following commands

```bash
mkdir build && cd build
../configure CXX=icpc CC=icc F77=ifort --with-blas="mkl_rt" \
    --with-lapack="mkl_rt" \
    --with-libs="-L$MKLROOT/lib/intel64 -lmkl_intel_lp64 -lmkl_core \
    -lmkl_intel_thread -lpthread -liomp5 -lm" \
    --with-cflags="-xhost -O3 -m64 -I$MKLROOT/include -fPIC -fp-model precise" \
    --with-cppflags="-xhost -O3 -m64 -I$MKLROOT/include -fPIC -fp-model precise" \
    --with-fflags="-xhost -O3 -m64 -I$MKLROOT/include -fPIC -fp-model precise" \
    --enable-shared
make
sudo -s
source /opt/intel/bin/compilervars.sh intel64
make install
exit
```

Let's take a look at these commands now too.

1. Create a build directory and change into it
2. Give Sundials all the options we're going to use
    - `../configure`: The configure script in the directory one up that creates a Makefile
    - `CXX=icpc`: Which C++ compiler to use (`icpc` is the name of the Intel C++ compiler)
    - `CC=icc`: Which C compiler to use (`icc` is the name of the Intel C compiler)
    - `F77=ifort`: Which Fortran compiler to use (`ifort` is the name of the Intel Fortran compiler)
    - `--with-blas="mkl_rt"`: This tells Sundials to use BLAS from the Intel MKL
    - `--with-lapack="mkl_rt"`: This tells Sundials to use LAPACK from the Intel MKL
    - `--with-libs="..."`: This line tells Sundials where it can find all of the fancy Intel MKL stuff.
      <del>The `mkl_intel_thread` and `iomp5` entries are particularly important, as these enable multi-threaded
      solving for the Cantera 1-D solvers.</del> Update: Further testing has shown that including these libraries
      in SUNDIALS is not important for the 1-D solver in Cantera. I think these libraries are only required if
      the Intel MKL will be used in a program that uses OpenMP threading.
    - `--with-cflags="..."`, `--with-cppflags="..."`, and `--with-fflags="..."`: These are compiler flags for
      Sundials.
        - `-xhost`: Intel specific optimizations for Intel processors
        - `-O3`: Optimization level
        - `-m64`: Build for 64 bits
        - `-I$MKLROOT/include`: `MKLROOT` is an environment variable defined by the Intel `compilervars.sh` script.
          This flag tells the compiler where it can find the include files the library needs.
        - `-fPIC`: Generate position independent code, <del>meaning the compiled file does not depend on being in a
          particular location in the filesystem.</del> meaning the library does not depend on being in a particular
          location in memory when it is compiled into a separate program.
        - `-fp-model precise`: Use the `precise` floating point model
    - `--enable-shared`: Build the shared libraries in addition to the static libraries.
3. Run `make` to compile and link all the files
4. Switch to root to install the libraries
5. Source the Intel variables as root
6. Install everythin with `make install`
7. Exit root

## Install Cantera {#InstallCantera}

Now we have finally finished installing the dependencies, and we can actually install Cantera itself.
You can either download the tarball of the most recent stable source from here:
<http://sourceforge.net/projects/cantera/files/cantera/> and unzip it by

    tar -xzf cantera-X.Y.Z.tar.gz

Alternatively, you can download the source code by Subversion or
[`git-svn`](https://www.kernel.org/pub/software/scm/git/docs/git-svn.html)

    svn checkout http://cantera.googlecode.com/svn/cantera/branches/2.1/ cantera
    #                                                                   ^The space here is
    #                                                                    important

or

    git svn clone --stdlayout http://cantera.googlecode.com/svn/cantera/ cantera
    #                                                                   ^The space here is
    #                                                                    important
    cd cantera
    git checkout 2.1

Either of these options will give you the most recent stable build of Cantera. If you want to live on
the bleeding edge, you can download the developer version of Cantera by either

    svn checkout http://cantera.googlecode.com/svn/cantera/trunk cantera
    #                                                           ^The space here is
    #                                                            important

or

    git svn clone --stdlayout http://cantera.googlecode.com/svn/cantera/ cantera
    #                                                                   ^The space here is
    #                                                                    important

and don't give the `git checkout 2.1` line. After that, change into the directory where Cantera was
downloaded or unzipped.

Now we need to configure the installation of Cantera. This configuration file will install the Cantera
files in a different directory per user. The reason for this is that we wanted to allow each user of
the server to have their own independent install of Cantera, rather than a global single version.
Create a file called `cantera.conf` and copy the following into it

```python
CXX = 'icpc'
CC = 'icc'
prefix = '/home/_username_/.local'
python_package = 'new'
python_prefix = 'USER'
python3_prefix = 'USER'
python_compiler = 'icpc'
f90_interface = 'y'
F90 = 'ifort'
F90FLAGS = '-O3 -xhost'
use_sundials = 'y'
sundials_include = '/usr/local/include'
sundials_libdir = '/usr/local/lib'
blas_lapack_libs = 'mkl_rt'
blas_lapack_dir = '/opt/intel/composerxe/mkl/lib/intel64/'
env_vars = 'all'
cc_flags = '-Wall -Wno-deprecated -xhost -fp-model precise'
debug_linker_flags = '-lmkl_intel_lp64 -lmkl_core -lmkl_intel_thread -lpthread -liomp5'
build_thread_safe = True
boost_inc_dir = '/usr/local/include'
boost_lib_dir = '/usr/local/lib'
boost_thread_lib = 'boost_system'
F77 = 'ifort'
F77FLAGS = '-O3 -xhost'
rpfont = 'helvetica'
```

`_username_` should be the username where Cantera should be installed. To see an explanation of
these options, type `scons install help`. Note that you may have to change the directory
of the Intel MKL. Briefly, they are:

- `CXX`, `CC`, `F90`, and `F77`: The compilers to use for the C++, C, and Fortran files respectively
- `prefix`: The directory in which Cantera should be installed. If using the Python interface,
   the `~/.local` directory is on Python's path by default, so it is a good choice if a per-user
   install is desired
- `python_prefix`,`python3_prefix`: The directories where the Python module should be installed. Specifying
  `'USER'` tells the installer to put the module in the default user directory, which is `~/.local` by
  default. This overrides any value of the prefix, so if you want the Python module installed in the
  prefix directory, delete these lines
- `python_compiler`: The compiler to use when compiling the Python module. Should be the same as `CXX`.
- `f90_interface`: Compile the Fortran 90 interface
- `F90FLAGS` and `F77FLAGS`: Flags to send to the Fortran compiler when compiling the Fortran 90 and
  Fortran 77 interfaces, respectively
- `use_sundials`: Specify whether or not to use SUNDIALS
- `sundials_include`,`sundials_libdir`: The directories where Cantera can find the header files and the
  Sundials libraries, respectively. Should be set to the directory where Sundials was installed
- `blas_lapack_libs`, `blas_lapack_dir`: The libraries and directory for BLAS and LAPACK. To use the
  Intel MKL, `mkl_rt` should be specified for the `libs`, and the full absolute path to the directory
  where the libraries are stored needs to be given. Note that in this configuration, shell variables
  such as `$MKLHOME` cannot be used because they won't be expanded properly (at least, I got an error
  when I tried that)
- `env_vars`: The environment variables that should be passed in from the shell. This should be set to
  `all` so that the installer can find the Intel compilers
- `cc_flags`: The C and C++ compiler flags
- `debug_linker_flags`: All the libraries Cantera should link to
- `build_thread_safe`: Allow Cantera to be used in multi-threaded applications
- `boost_inc_dir`, `boost_lib_dir`: Similar to Sundials, the include and libraries directories where
  Boost was installed
- `boost_thread_lib`: Libraries to include when building the Boost threaded components
- `rpfont`: The font to use when printing reaction paths.

After `cantera.conf` is set, its time to build and install Cantera. The following commands will
build, test, and install Cantera:

    export LD_LIBRARY_PATH=/usr/local/lib:/usr/lib:$LD_LIBRARY_PATH
    scons build -j2
    scons test
    scons install

As before, the `-jn` option specifies the number of build tasks to perform in parallel. Set `n`
less than or equal to the number of processors you wish to use to perform the build. Higher `n`
makes the build go muuuuuch faster as long as you don't exceed the number of processors on your
computer. After that, change out of the Cantera directory, and in Python 2 & 3 shells, type

```python
>>> import cantera
```

If no errors pop out, you've done it! Congratulations! Now just make some small
additions to your `~/.bashrc` file (at the bottom of the file) so that Cantera
is ready to go on each login:

    source /opt/intel/bin/compilervars.sh intel64
    export PATH=/home/username/.local/bin:$PATH
    export LD_LIBRARY_PATH=/home/_username_/.local/lib:/usr/local/lib:usr/lib:$LD_LIBRARY_PATH
    export MANPATH=/home/username/.local/man:$MANPATH
