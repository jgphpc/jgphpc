#!/bin/bash

cd /efface/conferences/crontab.eff/
export MAILJG="/efface/apps/email/201603/bin/email -tls"

#     #   #*#           #     # ######   #####
#     #    #            #     # #     # #     #
#     #    #            #     # #     # #
#     #    #     #####  ####### ######   #####
 #   #     #            #     # #             #
  # #      #            #     # #       #     #
   #      ###           #     # #        #####
# -----------------------------------------------------------------
url="http://www.vi-hps.org/news/"
old=eff-old.vihps1
new=eff-new.vihps1
rm -f $new
w3m -dump $url > $new 2> /dev/null
diff -q $old $new > /dev/null
# if  NOdiff alors $?=0
# if YESdiff alors $?=1
if [ $? -eq 1 ] ; then
( echo check $url ; diff $old $new ) | $MAILJG -s "conferences $url"  jgp@cscs.ch
fi
mv $new $old


# -----------------------------------------------------------------
url="http://www.vi-hps.org/training/tws/"
old=eff-old.vihps2
new=eff-new.vihps2
rm -f $new
w3m -dump $url > $new 2> /dev/null
diff -q $old $new > /dev/null
# if  NOdiff alors $?=0
# if YESdiff alors $?=1
if [ $? -eq 1 ] ; then
( echo check $url ; diff $old $new ) | $MAILJG -s "conferences $url" jgp@cscs.ch
fi
mv $new $old



######  ######  #######  #####  ######  ####### ######
#     # #     # #     # #     # #     # #       #     #
#     # #     # #     # #       #     # #       #     #
######  ######  #     #  #####  ######  #####   ######
#       #   #   #     #       # #       #       #   #
#       #    #  #     # #     # #       #       #    #
#       #     # #######  #####  #       ####### #     #
# --------------------------------------------------------
#url='http://www.europar2015.org/cfp.html'
#url='http://www.europar2015.org/registration.html'
url='https://europar2016.inria.fr/program/'
old=eff-old.proper
new=eff-new.proper
w3m -dump $url > $new 2> /dev/null
diff -q $old $new > /dev/null
if [ $? -eq 1 ] ; then
        ( echo " check $url" ; echo $url ; diff $old $new ) | $MAILJG -s "CRONTAB : conferences $url" jgp@cscs.ch
fi
mv -f $new $old


# --------------------------------------------------------
url='http://toolsworkshop.hlrs.de/2014/index.php/proceedings'
old=eff-old.proper2
new=eff-new.proper2
w3m -dump $url > $new 2> /dev/null
diff -q $old $new > /dev/null
if [ $? -eq 1 ] ; then
        ( echo " check $url" ; echo $url ; diff $old $new ) | $MAILJG -s "CRONTAB : conferences $url" jgp@cscs.ch
fi
mv -f $new $old


# --------------------------------------------------------
## url='http://www.rapido.deib.polimi.it/program.html'
## old=eff-old.rapido
## new=eff-new.rapido
## w3m -dump $url > $new 2> /dev/null
## diff -q $old $new > /dev/null
## if [ $? -eq 1 ] ; then
##         ( echo " check $url" ; echo $url ; diff $old $new ) | $MAILJG -s "CRONTAB : conferences $url" jgp@cscs.ch
## fi
## mv -f $new $old



