#!/bin/bash

cd /home/piccinal/keep/linux.git/crontab/conferences/
export MAILJG="/efface/apps/email/201603/bin/email -tls"

 #####   #####   #####   #####
#     # #     # #     # #     #
#       #       #       #
#        #####  #        #####
#             # #             #
#     # #     # #     # #     #
 #####   #####   #####   #####
# ------------------------------------------------------
old=eff-old.cscsjob
new=eff-new.cscsjob
html=eff-html.cscsjob.html
url='http://www.cscs.ch/about/working_at_cscs/open_positions/index.html'
# w3m -dump $url |grep -v Impressum > $new
wget --quiet -O $html $url 
w3m -dump $html |grep -v Impressum > $new
diff -q $old $new > /dev/null
if [ $? -eq 1 ] ; then
        ( echo check $url ; diff $old $new ) | $MAILJG -s "conferences $url" jgp@cscs.ch
fi
mv -f $new $old

# ------------------------------------------------------
old=eff-old.cscsevents
new=eff-new.cscsevents
html=eff-html.cscsevents.html
url='http://www.cscs.ch/events/upcoming_events/index.html'
# w3m -dump $url |grep -v Impressum > $new
wget --quiet -O $html $url 
w3m -dump $html |grep -v Impressum > $new
diff -q $old $new > /dev/null
if [ $? -eq 1 ] ; then
        ( echo check $url ; diff $old $new ) | $MAILJG -s "conferences $url" jgp@cscs.ch
fi
mv -f $new $old

