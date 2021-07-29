---
title:  Installing NumPy/SciPy on Ubuntu 12.04.3 from scratch/source with Intel compilers
date:   2014-01-11 16:53
category: personal
slug: installing-numpy-scipy-on-ubuntu-12.04.3-from-scratch-source-with-intel-compilers
original_url: writing/personal/2014/01/11/installing-numpy-scipy-on-ubuntu-12.04.3-from-scratch-source-with-intel-compilers/index.html
---

**Update: The following procedure will work on Ubuntu 14.04.1 as well.**

This post will explain how to install Numpy and Scipy on Ubuntu 12.04.3 with the
most recent Intel compilers as of this writing (2013 SP1 Update 1).
<!--more-->
These instructions are based heavily on the excellent blog post by Son Hua, at
<http://songuke.blogspot.com/2012/02/compile-numpy-and-scipy-with-intel-math.html>.

The procedure to install the Intel compilers can be found at [this
page]({filename}2014-01-08-installing-cantera-on-ubuntu-12.04.3-from-scratch-source-with-Intel-compilers.md/#InstallIntelCompilers).

The dependencies for NumPy and SciPy can be installed with the following, if
they haven't been already:

```bash
sudo apt-get install git swig libsuitesparse-dev python3 \
python3-dev python-dev
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py \
-O - | sudo python3.2
sudo easy_install-3.2 pip
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py \
-O - | sudo python2.7
sudo easy_install pip
sudo pip2 install cython nose
sudo pip3 install cython nose
```

First, download the source from the git repositories.

```bash
git clone git://github.com/numpy/numpy.git
git clone git://github.com/scipy/scipy.git
```

To checkout the most recent stable version, type

```bash
git tag
```

and pick the highest one that is just numbers. As of today, for `numpy` that is
`v1.8.2`, and for `scipy` it is `v0.14.0`, so

```bash
cd numpy && git checkout v1.8.2
cd scipy && git checkout v0.14.0
```

This step is optional. The next step is to compile and install `numpy`; `scipy`
depends on `numpy`, so `numpy` goes first. From the folder where you ran the git
commands, change into the `numpy` directory (there should be a file called
`setup.py` if you're in the correct directory), create a file called `site.cfg`,
and copy the following contents into it:

```ini
[DEFAULT]
library_dirs = /usr/local/lib:/usr/lib
include_dirs = /usr/local/include:/usr/include

[mkl]
library_dirs = /opt/intel/composerxe/lib/intel64:/opt/intel/composerxe/mkl/lib/intel64
include_dirs = /opt/intel/composerxe/mkl/include/intel64/lp64
mkl_libs = mkl_def, mkl_intel_lp64, mkl_intel_thread, mkl_core, iomp5
lapack_libs = mkl_lapack95_lp64

[umfpack]
library_dirs = /usr/lib
include_dirs = /usr/include/suitesparse
umfpack_libs = umfpack

[amd]
library_dirs = /usr/lib
include_dirs = /usr/include/suitesparse
amd_libs = amd
```

Note that the `umfpack` and `amd` sections are optional. If you choose not to
install with support for them, `libsuitesparse-dev` in the dependencies can be
eliminated. The directories you specify for the libraries and the include
**must** be the directories where the Intel compilers are actually installed,
and this directory might be different than listed above.

The `distutils` setup options for using the Intel C compiler aren't quite right
by default, so we have to edit one file to ensure all the right flags are used.
In your favorite text editor, open `numpy/distutils/intelccompiler.py`. Make
sure to open the `intelccompiler.py` not `intelccompiler.pyc`. We need to change
the `IntelEM64TCComiler` class to have the right flags. Initially, the class
will look like:

```python
#BEFORE
class IntelEM64TCCompiler(UnixCCompiler):
    """ A modified Intel x86_64 compiler compatible with a 64bit gcc built Python.
    """
    compiler_type = 'intelem'
    cc_exe = 'icc -m64 -fPIC'
    cc_args = "-fPIC"
    def __init__ (self, verbose=0, dry_run=0, force=0):
        UnixCCompiler.__init__ (self, verbose, dry_run, force)
        self.cc_exe = 'icc -m64 -fPIC'
        compiler = self.cc_exe
        self.set_executables(compiler=compiler,
                             compiler_so=compiler,
                             compiler_cxx=compiler,
                             linker_exe=compiler,
                             linker_so=compiler + ' -shared')
```

We need to change the `self.cc_exe` line (line 10) to include all the proper
flags. Edit the string on that line to include `-openmp`, `-g`, `-O3`, and
`-xhost`. You can also comment out the `cc_exe` and `cc_args` lines (6 and 7),
but this is probably optional. After the changes, the code will look like:

```python
#AFTER
class IntelEM64TCCompiler(UnixCCompiler):
    """ A modified Intel x86_64 compiler compatible with a 64bit gcc built Python.
    """
    compiler_type = 'intelem'
#    cc_exe = 'icc -m64 -fPIC'
#    cc_args = "-fPIC"
    def __init__ (self, verbose=0, dry_run=0, force=0):
        UnixCCompiler.__init__ (self, verbose, dry_run, force)
        self.cc_exe = 'icc -m64 -fPIC -O3 -g -openmp -xhost'
        compiler = self.cc_exe
        self.set_executables(compiler=compiler,
                             compiler_so=compiler,
                             compiler_cxx=compiler,
                             linker_exe=compiler,
                             linker_so=compiler + ' -shared')
```

These compiler flags will give us all of the benefits of the Intel compilers
running on Intel chips.

Then, we will build and install for Python 2 & 3.

```bash
python setup.py config --compiler=intelem --fcompiler=intelem build_clib \
--compiler=intelem --fcompiler=intelem build_ext --compiler=intelem --fcompiler=intelem \
build
sudo -s
source /opt/intel/bin/compilervars.sh intel64
python setup.py install
rm -rf build
exit
python3 setup.py config --compiler=intelem --fcompiler=intelem build_clib \
--compiler=intelem --fcompiler=intelem build_ext --compiler=intelem --fcompiler=intelem \
build
sudo -s
source /opt/intel/bin/compilervars.sh intel64
python3 setup.py install
exit
```

Awesome, `numpy` is installed. Check that everything went properly by changing
out of the `numpy` directory, then run the following, in both a Python 2 and
Python 3 shell (the lines with `>>>` indicate text to be typed at the Python
prompt).

```python
>>> import numpy
>>> numpy.show_config()
lapack_opt_info:
    libraries = ['mkl_lapack95_lp64', 'iomp5', 'mkl_def', 'mkl_intel_lp64',
    'mkl_intel_thread', 'mkl_core', 'pthread']
    library_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64',
    '/opt/intel/composer_xe_2013_sp1.1.106/mkl/lib/intel64']
    define_macros = [('SCIPY_MKL_H', None)]
    include_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/mkl/include/intel64/lp64']
blas_opt_info:
    libraries = ['iomp5', 'mkl_def', 'mkl_intel_lp64', 'mkl_intel_thread',
    'mkl_core', 'pthread']
    library_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64',
    '/opt/intel/composer_xe_2013_sp1.1.106/mkl/lib/intel64']
    define_macros = [('SCIPY_MKL_H', None)]
    include_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/mkl/include/intel64/lp64']
openblas_info:
  NOT AVAILABLE
lapack_mkl_info:
    libraries = ['mkl_lapack95_lp64', 'iomp5', 'mkl_def', 'mkl_intel_lp64',
    'mkl_intel_thread', 'mkl_core', 'pthread']
    library_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64',
    '/opt/intel/composer_xe_2013_sp1.1.106/mkl/lib/intel64']
    define_macros = [('SCIPY_MKL_H', None)]
    include_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/mkl/include/intel64/lp64']
blas_mkl_info:
    libraries = ['iomp5', 'mkl_def', 'mkl_intel_lp64', 'mkl_intel_thread',
    'mkl_core', 'pthread']
    library_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64',
    '/opt/intel/composer_xe_2013_sp1.1.106/mkl/lib/intel64']
    define_macros = [('SCIPY_MKL_H', None)]
    include_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/mkl/include/intel64/lp64']
mkl_info:
    libraries = ['iomp5', 'mkl_def', 'mkl_intel_lp64', 'mkl_intel_thread',
    'mkl_core', 'pthread']
    library_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64',
    '/opt/intel/composer_xe_2013_sp1.1.106/mkl/lib/intel64']
    define_macros = [('SCIPY_MKL_H', None)]
    include_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/mkl/include/intel64/lp64']
>>> numpy.test()
Running unit tests for numpy
NumPy version 1.9.0.dev-0b85f91
NumPy is installed in /usr/local/lib/pythonX.Y/dist-packages/numpy
Python version X.Y.Z (default, Sep 26 2013, 20:03:06) [GCC 4.6.3]
nose version 1.3.0
...
----------------------------------------------------------------------
Ran 5231 tests in 47.481s

OK (KNOWNFAIL=5, SKIP=7)
<nose.result.TextTestResult run=5231 errors=0 failures=0>
```

During the test, a number of dots will be printed to the screen, along with the
letters `S` and `K`. If any tests fail, `F` will be printed. All of the tests
passed for me on 15-JUL-2014.

Now we can install `scipy`. First, change to the `scipy` directory. Just like
for `numpy`, we need a configuration file so that `scipy` knows where to find
all of the information it needs. It turns out that the `site.cfg` we created for
`numpy` will work just fine for `scipy`. Type

```bash
cp ../numpy/site.cfg site.cfg
```

Then, the build and install commands are the same as before:

```bash
python setup.py config --compiler=intelem --fcompiler=intelem build_clib \
--compiler=intelem --fcompiler=intelem build_ext --compiler=intelem --fcompiler=intelem \
build
sudo -s
source /opt/intel/bin/compilervars.sh intel64
python setup.py install
rm -rf build
exit
python3 setup.py config --compiler=intelem --fcompiler=intelem build_clib \
--compiler=intelem --fcompiler=intelem build_ext --compiler=intelem --fcompiler=intelem \
build
sudo -s
source /opt/intel/bin/compilervars.sh intel64
python3 setup.py install
exit
```

After `scipy` is installed, we need to test it as well. Change out of the
`scipy` directory, and run the following in a Python 2 and 3 shell:

```python
>>> import scipy
>>> scipy.show_config()
amd_info:
    libraries = ['amd']
    library_dirs = ['/usr/lib']
    define_macros = [('SCIPY_AMD_H', None)]
    swig_opts = ['-I/usr/include/suitesparse']
    include_dirs = ['/usr/include/suitesparse']
umfpack_info:
    libraries = ['umfpack', 'amd']
    library_dirs = ['/usr/lib']
    define_macros = [('SCIPY_UMFPACK_H', None), ('SCIPY_AMD_H', None)]
    swig_opts = ['-I/usr/include/suitesparse', '-I/usr/include/suitesparse']
    include_dirs = ['/usr/include/suitesparse']
lapack_opt_info:
    libraries = ['mkl_lapack95_lp64', 'iomp5', 'mkl_def',
    'mkl_intel_lp64', 'mkl_intel_thread', 'mkl_core', 'pthread']
    library_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64',
    '/opt/intel/composer_xe_2013_sp1.1.106/mkl/lib/intel64']
    define_macros = [('SCIPY_MKL_H', None)]
    include_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/mkl/include/intel64/lp64']
blas_opt_info:
    libraries = ['iomp5', 'mkl_def', 'mkl_intel_lp64', 'mkl_intel_thread',
    'mkl_core', 'pthread']
    library_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64',
    '/opt/intel/composer_xe_2013_sp1.1.106/mkl/lib/intel64']
    define_macros = [('SCIPY_MKL_H', None)]
    include_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/mkl/include/intel64/lp64']
openblas_info:
  NOT AVAILABLE
lapack_mkl_info:
    libraries = ['mkl_lapack95_lp64', 'iomp5', 'mkl_def', 'mkl_intel_lp64',
    'mkl_intel_thread', 'mkl_core', 'pthread']
    library_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64',
    '/opt/intel/composer_xe_2013_sp1.1.106/mkl/lib/intel64']
    define_macros = [('SCIPY_MKL_H', None)]
    include_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/mkl/include/intel64/lp64']
blas_mkl_info:
    libraries = ['iomp5', 'mkl_def', 'mkl_intel_lp64', 'mkl_intel_thread',
    'mkl_core', 'pthread']
    library_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64',
    '/opt/intel/composer_xe_2013_sp1.1.106/mkl/lib/intel64']
    define_macros = [('SCIPY_MKL_H', None)]
    include_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/mkl/include/intel64/lp64']
mkl_info:
    libraries = ['iomp5', 'mkl_def', 'mkl_intel_lp64', 'mkl_intel_thread',
    'mkl_core', 'pthread']
    library_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/compiler/lib/intel64',
    '/opt/intel/composer_xe_2013_sp1.1.106/mkl/lib/intel64']
    define_macros = [('SCIPY_MKL_H', None)]
    include_dirs = ['/opt/intel/composer_xe_2013_sp1.1.106/mkl/include/intel64/lp64']
>>> scipy.test()
Running unit tests for scipy
NumPy version 1.9.0.dev-0b85f91
NumPy is installed in /usr/local/lib/pythonX.Y/dist-packages/numpy
SciPy version 0.14.0.dev-e6f1eeb
SciPy is installed in /usr/local/lib/pythonX.Y/dist-packages/scipy
Python version X.Y.Z (default, Sep 26 2013, 20:03:06) [GCC 4.6.3]
nose version 1.3.0
...
Ran 9944 tests in 159.327s

FAILED (KNOWNFAIL=118, SKIP=449, errors=20, failures=13)
<nose.result.TextTestResult run=9944 errors=20 failures=13>
```

As you can see, `scipy` has a number of errors and failures. The text of these
errors will be printed prior to the `Ran 9944...` line. Nonetheless, everything
that I use seems to work.

And that should do it. NumPy and SciPy should now be installed for both Python 2
& 3.
