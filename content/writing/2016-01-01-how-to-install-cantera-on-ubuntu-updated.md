---
title:  Installing Cantera on Ubuntu with Intel Compilers UPDATED!
date:   2016-01-01 12:57
category: personal
original_url: writing/personal/2016/01/01/how-to-install-cantera-on-ubuntu-updated/index.html
---

Well, it is now 2 years since I wrote my original post on [how to install
Cantera with the Intel
compilers]({filename}2014-01-08-installing-cantera-on-ubuntu-12.04.3-from-scratch-source-with-Intel-compilers.md),
and things have changed. For one, Ubuntu has been upgraded (and will be upgraded
again this summer); for another, there is a new version of Cantera to work with.
Actually, there are two new versions, if you count the master branch stored at
GitHub.

This post is intended to be an update on how I install Cantera on Ubuntu using
the Intel compilers. Due to some handy features in the current developer's
version, I'm going to describe instructions for the master branch. If you want
the stable version, go back to the old post and use the instructions there. On
with the building!
<!--more-->

One of the major changes in the current master branch is that SUNDIALS is
included in the repository, and there is no need to build and install it
separately. Another big change is that Boost can be found automatically if it is
in a standard directory. Finally, the code has moved from Google Code (which
shut down) over to GitHub. With these big changes in mind, this is how I build
and install Cantera with Intel these days.

First, I prefer to use the Anaconda Python distribution nowadays. This makes
controlling environments for testing and such much easier. I also prefer to use
Python 3 as much as possible, but unfortunately, SCons is still Python 2 only.
First, install the pre-reqs into the `root` environment, then create the builder
environment

```bash
conda install numpy cython
conda create -n py2k python=2 scons cython numpy
source activate py2k
pip install 3to2
```

With that done, clone the Git repository from GitHub

```bash
git clone https://github.com/Cantera/cantera.git
```

Now change into that directory and create your `cantera.conf` file:

```python
CXX = 'icpc'
CC = 'icc'
prefix = '/home/username/.local'
python_package = 'new'
python_prefix = 'USER'
python3_cmd = '/path/to/anaconda3/bin/python'
python3_prefix = 'USER'
f90_interface = 'y'
FORTRAN = 'ifort'
FORTRANFLAGS = '-O3 -xHost'
system_sundials = 'n'
blas_lapack_libs = 'mkl_rt,mkl_intel_lp64,mkl_core,mkl_intel_thread,iomp5'
blas_lapack_dir = '/opt/intel/composerxe/mkl/lib/intel64/'
env_vars = 'all'
cc_flags = ''
optimize_flags = '-O3 -Wall -xHost -fp-model precise'
debug = False
```

Then it's as simple as

```bash
scons build -j4
scons install
```

This will put Cantera into your `~/.local` directory, including the Python 2 and
3 interface and the Fortran interface.
