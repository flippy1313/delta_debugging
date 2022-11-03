#!/bin/bash
status=0
for var in $*;
do 
	patch="patch."$var
	patch wireworld-original.c < $patch	
done

if gcc -c wireworld-original.c; then
	status=0;
else
	status=1;
fi

for var in $*; do
	patch="patch."$var
	patch -R wireworld-original.c < $patch
done

if [ $status -eq 1 ]; then
	exit 1;
elif [ $status -eq 0 ]; then
	exit 0;
fi
