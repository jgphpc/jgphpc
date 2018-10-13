#!/bin/bash

cd /home/piccinal/keep/linux.git/crontab/events/
export MAILJG="/efface/apps/email/201603/bin/email -tls"

######   #####  #    #  ######
#          #    #    #      #
#####      #    ######     #
#          #    #    #    #
#          #    #    #   #
######     #    #    #  ######
# --------------------------------------------------------
url='https://apply.refline.ch/845721/search.html?form.buttons.listWorkloadFullTime=1'
old=eff-old.ethz
new=eff-new.ethz
w3m -dump "$url" > $new 2> /dev/null
diff -q $old $new > /dev/null
if [ $? -eq 1 ] ; then
        ( echo " check $url" ; echo $url ; diff $old $new ) | $MAILJG -s "CRONTAB : ethz jobs $url" jgp@cscs.ch
fi
mv -f $new $old



