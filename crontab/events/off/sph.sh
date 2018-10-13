#!/bin/bash

cd /efface/conferences/crontab.eff/
export MAILJG="/efface/apps/email/201603/bin/email -tls"

 #####  ######  #     #
#     # #     # #     #
#       #     # #     #
 #####  ######  #######
      # #       #     #
#     # #       #     #
 #####  #       #     #
old=eff-old.spheric
new=eff-new.spheric
# url='https://wiki.manchester.ac.uk/spheric/index.php/Events_and_Activities'
#url='http://www.spheric2015.unipr.it/#registration'
url='https://www.events.tum.de/frontend/index.php?folder_id=265'
w3m -dump $url |grep -v "This page has been accessed" > $new 2> /dev/null
diff -q $old $new > /dev/null
if [ $? -eq 1 ] ; then
        ( echo " check $url" ; echo $url ; diff $old $new ) | $MAILJG -s "CRONTAB : conferences $url" jgp@cscs.ch
fi
mv -f $new $old

# --------------------------------------------------------
old=eff-old.dualsph
new=eff-new.dualsph
url='http://www.dual.sphysics.org/index.php/news/'
w3m -dump $url > $new 2> /dev/null
diff -q $old $new > /dev/null
if [ $? -eq 1 ] ; then
        ( echo " check $url" ; echo $url ; diff $old $new ) | $MAILJG -s "CRONTAB : conferences $url" jgp@cscs.ch
fi
mv -f $new $old

