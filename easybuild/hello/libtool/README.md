Start with hello-1.0.tar.gz => step 4

Steps:
* 1/: automake --add-missing
* 2/: autoreconf + automake --add-missing
* 3/: automake --add-missing
* 4/: configure; make

diff -q 1 2 
```
Only in 2: Makefile.in
Only in 2: aclocal.m4
Common subdirectories: 1/autom4te.cache and 2/autom4te.cache
Only in 2: config
Only in 2: configure
Common subdirectories: 1/src and 2/src
```

diff -q 2 3 
```
Files 2/Makefile.in and 3/Makefile.in differ
Common subdirectories: 2/autom4te.cache and 3/autom4te.cache
Common subdirectories: 2/config and 3/config
Common subdirectories: 2/src and 3/src
```

diff -q 3 4 
```
Only in 4: Makefile
Common subdirectories: 3/autom4te.cache and 4/autom4te.cache
Common subdirectories: 3/config and 4/config
Only in 4: config.status
Common subdirectories: 3/src and 4/src
```

diff -q 4 5 
```
Files 4/Makefile and 5/Makefile differ
Common subdirectories: 4/autom4te.cache and 5/autom4te.cache
Common subdirectories: 4/config and 5/config
Only in 5: config.log
Files 4/config.status and 5/config.status differ
Common subdirectories: 4/src and 5/src
```

* When looking for src code when debugging, use src from */apps/common/easybuild/sources*
