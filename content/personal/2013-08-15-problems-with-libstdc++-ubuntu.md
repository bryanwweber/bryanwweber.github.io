---
title:  Problems with libstdc++ on Ubuntu when using Intel Fortran Compiler 11.1
date:   2013-08-15 10:11:53
category: personal
original_url: writing/personal/2013/08/15/problems-with-libstdc++-ubuntu/index.html
---

Lately, we've had a problem on our computational server in the lab when trying
to link custom solvers to the CHEMKIN-Pro libraries. When the compiler runs, it
complains about undefined references to a symbol.
<!--more-->
The actual error code is:

```bash
undefined reference to symbol '__cxa_pure_virtual@@CXXABI_1.3'
ld: note: '__cxa_pure_virtual@@CXXABI_1.3' is defined in DSO
/usr/lib64/libstdc++.so.6 so try adding it to the linker command line
/usr/lib64/libstdc++.so.6: could not read symbols: Invalid operation
```

The solution is to tell the compiler which libraries to link. In the case of
CHEMKIN-Pro version 15113, this meant changing two files:

```bash
/home/user/$(CHEMKINROOT)/include/chemkin_make_unix.inc
/home/user/$(CHEMKINROOT)/include/arch/linuxx8664.inc
```

In the first file, on the line that starts `SAX_LIBFLAGS=...` add `-lstdc++` to
the end of the line. In the second file, on the line that starts `LDFLAGS=...`
add `-L/usr/lib64` to the end of the line.
