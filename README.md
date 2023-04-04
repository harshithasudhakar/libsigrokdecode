# Libsigrokdecode C Library

The sigrok project aims at creating a portable, cross-platform, Free/Libre/Open-Source signal analysis software suite that supports various device types (such as logic analyzers, oscilloscopes, multimeters, and more).

Libsigrokdecode is a shared library written in C which provides the basic API for running sigrok protocol decoders. The protocol decoders themselves are written in Python 3 (>=3.2, <3.6).


## Status

Libsigrokdecode is in a usable state and has had official tarball releases.

While the API can change from release to release, this will always be properly documented and reflected in the package version number and in the shared library / libtool/.so-file version numbers.

However, there are _NO_ guarantees at all for stable APIs in git snapshots! Distro packagers should only use released tarballs (no git snapshots).


## Requirements

 - git (only needed when building from git)
 - gcc (>= 4.0) or clang
 - make
 - autoconf >= 2.63 (only needed when building from git)
 - automake >= 1.11 (only needed when building from git)
 - libtool (only needed when building from git)
 - pkg-config >= 0.22
 - libglib >= 2.34
 - Python >= 3.2
 - check >= 0.9.4 (optional, only needed to run unit tests)
 - doxygen (optional, only needed for the C API docs)
 - graphviz (optional, only needed for the C API docs)


## Building and installing

In order to get the libsigrokdecode source code and build it, run:
```
 $ git clone git://sigrok.org/libsigrokdecode
 $ cd libsigrokdecode
 $ ./autogen.sh
 $ ./configure
 $ make
```


## For installing libsigrokdecode:

```
 $make install
```

Make sure to read the following  page for more (OS-specific) [instructions](http://sigrok.org/wiki/Building)


## Copyright and license

Libsigrokdecode is licensed under the terms of the GNU General Public License (GPL), version 3 or later.

The protocol decoders (PDs) included in libsigrokdecode are an integral part of the shared library (they are not merely external "plugins", they are not external programs that libsigrokdecode calls via fork/exec, they cannot function standalone without libsigrokdecode at all, the PDs and the rest of the libsigrokdecode codebase share data structures and make function calls to each other). Thus, since the PDs are part of the library, they are also licensed under the terms of the GPLv3+.

While some individual source code files are licensed under the GPLv2+, and some files are licensed under the GPLv3+, this doesn't change the fact that the library as a whole is licensed under the terms of the GPLv3+.

Please see the individual source files for the full list of copyright holders.


## Mailing list

https://lists.sourceforge.net/lists/listinfo/sigrok-devel


## IRC

You can find the sigrok developers in the #sigrok IRC channel on Freenode.


## Website

http://sigrok.org/wiki/Libsigrokdecode
