# ESCHA

e=`for i in 1 2 3;do 
    echo -n eschaln-000$i 
    ssh eschaln-000$i uptime 2> /dev/null 
done |sort -nk 11 |head -1|awk '{print $1}'`
ssh -Xt piccinal@ela.cscs.ch ssh -X $e

