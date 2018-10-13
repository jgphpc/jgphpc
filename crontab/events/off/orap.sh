#!/bin/bash

cd /efface/conferences/crontab.eff/
export MAILJG="/efface/apps/email/201603/bin/email -tls"

####### ######     #    ######
#     # #     #   # #   #     #
#     # #     #  #   #  #     #
#     # ######  #     # ######
#     # #   #   ####### #
#     # #    #  #     # #
####### #     # #     # #
old=eff-old.orap
new=eff-new.orap
url='http://orap.irisa.fr/'
# url="http://www.irisa.fr/orap/ACCUEIL/manifestations.html"
#wget -O eff-new.html -q http://www.irisa.fr/orap/ACCUEIL/manifestations.html
w3m -dump "$url" > $new
diff -q $old $new

# if  NOdiff alors $?=0
# if YESdiff alors $?=1
if [ $? -eq 1 ] ; then
   ( echo $url ; diff $old $new ) | $MAILJG -s "CRONTAB : conferences $url" jgp@cscs.ch
fi
mv -f $new $old





