#!/bin/bash

cd /home/piccinal/keep/linux.git/crontab/events/
export MAILJG="/efface/apps/email/201603/bin/email -tls"

######  ######  #######
#     # #     #    #
#     # #     #    #
#     # #     #    #
#     # #     #    #
#     # #     #    #
######  ######     #
url='https://www.allinea.com/events'
old=eff-old.ddt
new=eff-new.ddt
html=eff-html.ddt.html
rm -f $new
wget --quiet --no-check-certificate $url -O $html
w3m -dump $html > $new 2> /dev/null
diff -q $old $new &> /dev/null
        # if  NOdiff alors $?=0
        # if YESdiff alors $?=1
if [ $? -eq 1 ] ; then
( echo check $url ; diff $old $new ) | $MAILJG -s "conferences $url" jgp@cscs.ch
fi
mv $new $old

