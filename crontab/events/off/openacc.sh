#!/bin/bash

cd /efface/conferences/crontab.eff/
export MAILJG="/efface/apps/email/201603/bin/email -tls"


####### ######  ####### #     #    #     #####   #####
#     # #     # #       ##    #   # #   #     # #     #
#     # #     # #       # #   #  #   #  #       #
#     # ######  #####   #  #  # #     # #       #
#     # #       #       #   # # ####### #       #
#     # #       #       #    ## #     # #     # #     #
####### #       ####### #     # #     #  #####   #####
# url="http://www.openacc.org/calendar/year"
url="http://www.openacc.org/calendar/month"
new=eff_oacc.new
old=eff_oacc.old

rm -f $new
# wget --quiet $url -O $new
w3m -dump $url > $new 2>&1

diff -q $old $new &> /dev/null
        # if  NOdiff alors $?=0
        # if YESdiff alors $?=1
if [ $? -eq 1 ] ; then
( echo check $url ; diff $old $new ) | $MAILJG -s "conferences $url" jgp@cscs.ch
fi
mv $new $old


