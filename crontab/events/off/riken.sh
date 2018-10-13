#!/bin/bash

cd /efface/conferences/crontab.eff/
export MAILJG="/efface/apps/email/201603/bin/email -tls"

######    #*#   #    #  ####### #     #
#     #    #    #   #   #       ##    #
#     #    #    #  #    #       # #   #
######     #    ###     #####   #  #  #
#   #      #    #  #    #       #   # #
#    #     #    #   #   #       #    ##
#     #   ###   #    #  ####### #     #
# --------------------------------------------------------
url='http://www.aics.riken.jp/en/outreach/news'
old=eff-old.riken
new=eff-new.riken
w3m -dump $url > $new 2> /dev/null
diff -q $old $new > /dev/null
if [ $? -eq 1 ] ; then
        ( echo " check $url" ; echo $url ; diff $old $new ) | $MAILJG -s "CRONTAB : conferences $url" jgp@cscs.ch
fi
mv -f $new $old



