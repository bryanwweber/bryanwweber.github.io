---
layout: post
title: How to build SUNDIALS 2.6.2 with Intel compilers and CMake
date: 2016-01-01 12:04
categories:
- Personal
---
The removal of the old `configure` build system for SUNDIALS means that CMake must be used. This requires a few different settings than my previous posts. The commands below worked for me on Ubuntu 14.04.1 with the Intel version 15 compilers.
<!--more-->

First, download SUNDIALS from <https://computation.llnl.gov/casc/sundials/main.html> and untar the tarball.
Then, ensure that your version of CMake is new enough by downloading and installing a recent version of CMake from <https://cmake.org/download/>

Then, build and install SUNDIALS

{% highlight bash %}
cd sundials-2.6.2 && mkdir build && cd build
cmake .. -DBUILD_SHARED_LIBS=ON -DCMAKE_C_COMPILER=icc -DCMAKE_Fortran_COMPILER=ifort \
-DCMAKE_C_FLAGS="-xhost -O3 -m64 -I${MKLROOT}/include/intel64/lp64 -I${MKLROOT}/include -fPIC -fp-model precise" \
-DCMAKE_Fortran_FLAGS="-xhost -O3 -m64 -I${MKLROOT}/include/intel64/lp64 -I${MKLROOT}/include -fPIC -fp-model precise" \
-DEXAMPLES_ENABLE=OFF -DLAPACK_ENABLE=ON  -DPTHREAD_ENABLE=ON -DOPENMP_ENABLE=ON \
-DLAPACK_LIBRARIES="libmkl_blas95_lp64.a;libmkl_lapack95_lp64.a;libmkl_intel_lp64.so;libmkl_core.so;libmkl_intel_thread.so;libpthread.so;libm.so;libiomp5.so"
make -j12
sudo -s
. /opt/intel/bin/compilervars.sh intel64
make install
exit
{% endhighlight %}

Rather than using the variables in the `configure` script, this sets all the same variables in CMake. Happy solving!
