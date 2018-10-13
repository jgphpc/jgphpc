#!/bin/bash

cd /efface/conferences/crontab.eff/
export MAILJG="/efface/apps/email/201603/bin/email -tls"

######  #     # ####### #     # ####### #     #    #
#     #  #   #     #    #     # #     # ##    #   ##
#     #   # #      #    #     # #     # # #   #  # #
######     #       #    ####### #     # #  #  #    #
#          #       #    #     # #     # #   # #    #
#          #       #    #     # #     # #    ##    #
#          #       #    #     # ####### #     #  #####
# --------------------------------------------------------
old=eff-old.python1
new=eff-new.python1
url='https://www.python.org/events/python-events/'
w3m -dump $url > $new 2> /dev/null
diff -q $old $new > /dev/null
if [ $? -eq 1 ] ; then
        ( echo " check $url" ; echo $url ; diff $old $new ) | $MAILJG -s "CRONTAB : conferences $url" jgp@cscs.ch
fi
mv -f $new $old

# --------------------------------------------------------
old=eff-old.python1page2
new=eff-new.python1page2
url='https://www.python.org/events/python-events/?page=2'
w3m -dump $url > $new 2> /dev/null
diff -q $old $new > /dev/null
if [ $? -eq 1 ] ; then
        ( echo " check $url" ; echo $url ; diff $old $new ) | $MAILJG -s "CRONTAB : conferences $url" jgp@cscs.ch
fi
mv -f $new $old

######  #     # ####### #     # ####### #     #  #####
#     #  #   #     #    #     # #     # ##    # #     #
#     #   # #      #    #     # #     # # #   #       #
######     #       #    ####### #     # #  #  #  #####
#          #       #    #     # #     # #   # # #
#          #       #    #     # #     # #    ## #
#          #       #    #     # ####### #     # #######
old=eff-old.python2
new=eff-new.python2
url='https://www.python.org/events/python-user-group/'
w3m -dump $url > $new 2> /dev/null
diff -q $old $new > /dev/null
if [ $? -eq 1 ] ; then
        ( echo " check $url" ; echo $url ; diff $old $new ) | $MAILJG -s "CRONTAB : conferences $url" jgp@cscs.ch
fi
mv -f $new $old



