#!/bin/bash

cd /home/piccinal/keep/linux.git/crontab/events/
export MAILJG="/efface/apps/email/201603/bin/email -tls"

#     #  #####   #####     #
##    # #     # #     #   # #
# #   # #       #        #   #
#  #  # #        #####  #     #
#   # # #             # #######
#    ## #     # #     # #     #
#     #  #####   #####  #     #
old=eff-old.ncsa
new=eff-new.ncsa
url='http://jointlab.ncsa.illinois.edu/events/'
w3m -dump $url > $new 2> /dev/null
diff -q $old $new > /dev/null

if [ $? -eq 1 ] ; then
        ( echo " check $url" ; echo $url ; diff $old $new ) | $MAILJG -s "CRONTAB : conferences ncsa" jgp@cscs.ch
fi

mv -f $new $old




