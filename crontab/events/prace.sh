#!/bin/bash

cd /home/piccinal/keep/linux.git/crontab/events/
export MAILJG="/efface/apps/email/201603/bin/email -tls"

######  ######     #     #####  #######
#     # #     #   # #   #     # #
#     # #     #  #   #  #       #
######  ######  #     # #       #####
#       #   #   ####### #       #
#       #    #  #     # #     # #
#       #     # #     #  #####  #######
# ------------------------------------------------------
url="http://www.training.prace-ri.eu/"
effh=eff.html
new=eff.new.prace
old=eff.old.prace
rm -f $new
wget --quiet $url -O $effh
w3m -dump $effh > $new 2> /dev/null

diff -q $old $new &> /dev/null
        # if  NOdiff alors $?=0
        # if YESdiff alors $?=1
if [ $? -eq 1 ] ; then
( echo check $url ; diff $old $new ) | $MAILJG -s "conferences $url" jgp@cscs.ch
fi
mv $new $old

