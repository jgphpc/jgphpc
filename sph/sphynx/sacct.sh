
#for i in effo_evrard.0* ;do 
for i in "$@" ;do 
    j=`grep JOBID $i|cut -d= -f2` 
    echo $j |awk -v f=$i '{print "sacc "$0" >> "f}'
done
