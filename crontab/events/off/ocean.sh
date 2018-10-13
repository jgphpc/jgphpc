#!/bin/bash

cd /home/piccinal/keep/linux.git/crontab/events/
export MAILJG="/efface/apps/email/201603/bin/email -tls"

#######  #####  #######    #    #     #
#     # #     # #         # #   ##    #
#     # #       #        #   #  # #   #
#     # #       #####   #     # #  #  #
#     # #       #       ####### #   # #
#     # #     # #       #     # #    ##
#######  #####  ####### #     # #     #
old=eff-old.ocean
new=eff-new.ocean

#w3m -dump 'http://www.conferencealerts.com/ocean.htm' > $new
w3m -dump 'http://www.conferencealerts.com/search?searchTerm=ocean&x=0&y=0' 2> /dev/null |cut -c36- > $new
diff -q $old $new > /dev/null

if [ $? -eq 1 ] ; then
        ( echo 'This is an automated message - do not reply - check conf list' ; diff $old $new ) | $MAILJG -s "CRONTAB : conferences ocean" jgp@cscs.ch
fi

mv -f $new $old


#####   #####   ######  #    #     #    #    #  ######  #####
#    #  #    #  #       #    #     #    ##  ##  #       #    #
#    #  #    #  #####   #    #     #    # ## #  #####   #    #
#####   #####   #       #    #     #    #    #  #       #####
#       #   #   #        #  #      #    #    #  #       #   #
#       #    #  ######    ##       #    #    #  ######  #    #
url='http://www.previmer.org/actualites/'
old=eff-old.previmer
new=eff-new.previmer
w3m -dump $url > $new 2> /dev/null
diff -q $old $new > /dev/null
if [ $? -eq 1 ] ; then
        ( echo " check $url" ; echo $url ; diff $old $new ) | $MAILJG -s "CRONTAB : conferences $url" jgp@cscs.ch
fi
mv -f $new $old



