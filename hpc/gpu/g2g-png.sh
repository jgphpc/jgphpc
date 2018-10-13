#!/bin/sh

# cd ~/easybuild/daint/haswell/software/graphviz/2.40.1/share/graphviz/graphs/directed/jg/2gpu/

for i in *.gv;do 
    dot -Tjpg $i > $i.jpg 
done 
rm -f  template.gv.jpg eff.jpg all.jpg
montage *.jpg all.jpg 
eog all.jpg 
