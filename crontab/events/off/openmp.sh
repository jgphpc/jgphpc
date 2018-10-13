#!/bin/bash

cd /efface/conferences/crontab.eff/
export MAILJG="/efface/apps/email/201603/bin/email -tls"
 ####   #    #  #####    ####    ####   #    #
#    #  ##  ##  #    #  #    #  #    #  ##   #
#    #  # ## #  #    #  #       #    #  # #  #
#    #  #    #  #####   #       #    #  #  # #
#    #  #    #  #       #    #  #    #  #   ##
 ####   #    #  #        ####    ####   #    #
url='http://openmpcon.org/registration/'
old=eff-old.ompcon
new=eff-new.ompcon
w3m -dump $url > $new 2> /dev/null
diff -q $old $new &> /dev/null
        # if  NOdiff alors $?=0
        # if YESdiff alors $?=1
if [ $? -eq 1 ] ; then
( echo check $url ; diff $old $new ) | $MAILJG -s "conferences $url" jgp@cscs.ch
fi
mv $new $old


#    #    #   ####   #    #  #####
#    #    #  #    #  ##  ##  #    #
#    #    #  #    #  # ## #  #    #
#    # ## #  #    #  #    #  #####
#    ##  ##  #    #  #    #  #
#    #    #   ####   #    #  #
url='http://www.iwomp.org/registration/'
old=eff-old.iwomp
new=eff-new.iwomp
w3m -dump $url > $new 2> /dev/null
diff -q $old $new &> /dev/null
        # if  NOdiff alors $?=0
        # if YESdiff alors $?=1
if [ $? -eq 1 ] ; then
( echo check $url ; diff $old $new ) | $MAILJG -s "conferences $url" jgp@cscs.ch
fi
mv $new $old


  ###   #     # ####### #     # ######
   #    #  #  # #     # ##   ## #     #
   #    #  #  # #     # # # # # #     #
   #    #  #  # #     # #  #  # ######
   #    #  #  # #     # #     # #
   #    #  #  # #     # #     # #
  ###    ## ##  ####### #     # #
# old=eff-old.iwomp
# new=eff-new.iwomp
# url='http://openmpcon.org/2015-con/'  # subscribed to mailinglist 
# 
# w3m -dump 'http://portais.fieb.org.br/senai/iwomp2014/registration.php' &> $new
# diff -q $old $new
# 
# # if  NOdiff alors $?=0
# # if YESdiff alors $?=1
# if [ $? -eq 1 ] ; then
#    ( echo 'This is an automated message - do not reply. register http://portais.fieb.org.br/senai/iwomp2014/registration.php' ; diff $old $new ) | mail -s 'CRONTAB : IWOMP' jgp@cscs.ch
# fi
# mv -f $new $old
# http://openmpcon.org/timeline/ -> subscribed 





