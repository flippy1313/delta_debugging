#!/bin/bash
cd libpng-1.6.34
sh ./configure CFLAGS="--coverage -static"
make clean ; make 
for file in large-png-suite;
do ./pngtest $file fi

don
gcov *.c
rm *.gcda pngout.png
