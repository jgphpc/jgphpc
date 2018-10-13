#!/bin/bash

cd /home/piccinal/keep/linux.git/crontab/events/
export MAILJG="/efface/apps/email/201603/bin/email -tls"

#    #  #####    ####   #    #     #    #####   ######
#    #  #    #  #    #  #    #     #    #    #  #
######  #    #  #       #    #     #    #    #  #####
#    #  #####   #       # ## #     #    #####   #
#    #  #       #    #  ##  ##     #    #   #   #
#    #  #        ####   #    #     #    #    #  ######
url='www.hpcwire.com/events/?ical=1&tribe_display=list'
new=eff_hpcwire.new
old=eff_hpcwire.old
html=eff_hpcwire.html
rm -f $new
wget --quiet --no-check-certificate $url -O $html
grep -E "URL:|SUMMARY:" $html &> $new

diff -q $old $new &> /dev/null
        # if  NOdiff alors $?=0
        # if YESdiff alors $?=1
if [ $? -eq 1 ] ; then
( echo check $url ; diff $old $new ) | $MAILJG -s "conferences $url" jgp@cscs.ch
fi
mv $new $old


