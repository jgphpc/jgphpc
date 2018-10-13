#!/bin/bash

out=o_loop
echo tt: `date +%Y/%m/%d-%H:%M:%S-%s.%N` > $out

for i in `seq 500000` ;do
    echo i=$i
done >> $out

echo tt: `date +%Y/%m/%d-%H:%M:%S-%s.%N` >> $out

