#!/bin/bash

set title "Communication topology using IPM mapdata.txt" 
set xlabel "from a rank here..."
set ylabel "... to a rank here"
unset key

set grid
set pal color 
# for colors, see http://t16web.lanl.gov/Kawano/gnuplot/plotpm3d2-e.html
#set palette rgbformulae 3,11,6
set palette defined (0 "white", 50 "grey", 100 "black") 
set view map

set xrange [-1:64] ; set xtics 10
set yrange [-1:64] ; set ytics 10

splot "ipm/map_data.txt" using 2:3:4 with points palette ps 9 pt 5
#splot "matrix.dat"  with points palette ps 9 pt 5
pause -1

# TODO : run http://www2.fz-juelich.de/jsc/linktest/ !!!!
