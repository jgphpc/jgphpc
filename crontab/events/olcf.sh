#!/bin/bash

cd /home/piccinal/keep/linux.git/crontab/events/
export MAILJG="/efface/apps/email/201603/bin/email -tls"

####### ######  #     # #
#     # #     # ##    # #
#     # #     # # #   # #
#     # ######  #  #  # #
#     # #   #   #   # # #
#     # #    #  #    ## #
####### #     # #     # #######
# ------------------------------------------------------
# old=eff-old.ornl1
# new=eff-new.ornl1
# html=eff-html.ornl1.html
# url='https://www.olcf.ornl.gov/training-events/list/'
# wget --no-check-certificate --quiet -O $html $url 
# w3m -dump $html |grep -v Impressum > $new
# diff -q $old $new > /dev/null
# if [ $? -eq 1 ] ; then
#         ( echo check $url ; diff $old $new ) | $MAILJG -s "conferences $url" jgp@cscs.ch
# fi
# mv -f $new $old
# 
# ------------------------------------------------------
old=eff-old.ornl2
new=eff-new.ornl2
html=eff-html.ornl2.html
url='https://www.olcf.ornl.gov/support/training-events/'
wget --no-check-certificate --quiet -O $html $url 
w3m -dump $html |grep -v Impressum > $new
diff -q $old $new > /dev/null
if [ $? -eq 1 ] ; then
        ( echo check $url ; diff $old $new ) | $MAILJG -s "conferences $url" jgp@cscs.ch
fi
mv -f $new $old


####### ######  #     # #
#     # #     # ##    # #
#     # #     # # #   # #
#     # ######  #  #  # #
#     # #   #   #   # # #
#     # #    #  #    ## #
####### #     # #     # #######
# url="https://www.olcf.ornl.gov/training-events/upcoming/"
# old=eff-old.ornl3
# new=eff-new.ornl3
# html=eff-html.ornl3.html
# 
# rm -f $new
# wget --quiet --no-check-certificate $url -O $eff
# w3m -dump $eff &> $new
# 
# diff -q $old $new &> /dev/null
#         # if  NOdiff alors $?=0
#         # if YESdiff alors $?=1
# if [ $? -eq 1 ] ; then
# ( echo check $url ; diff $old $new ) | $MAILJG -s "conferences $url" jgp@cscs.ch
# fi
# mv $new $old
 
