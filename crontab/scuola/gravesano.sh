#!/bin/bash

cd /efface/conferences/crontab.eff/
export MAILJG="/efface/apps/email/201603/bin/email -tls"

# -----------------------------------------------------------------
url='http://www.smgravesano.ti.ch/'
old=eff-old.gravesano1
new=eff-new.gravesano1
rm -f $new
w3m -dump $url > $new 2> /dev/null
diff -q $old $new > /dev/null
# if  NOdiff alors $?=0
# if YESdiff alors $?=1
if [ $? -eq 1 ] ; then
( echo check $url ; diff $old $new ) | $MAILJG -s "scuola $url"  jgp@cscs.ch
fi
mv $new $old

# -----------------------------------------------------------------
url='http://www.smgravesano.ti.ch/sede'
old=eff-old.gravesano2
new=eff-new.gravesano2
rm -f $new
w3m -dump $url > $new 2> /dev/null
diff -q $old $new > /dev/null
# if  NOdiff alors $?=0
# if YESdiff alors $?=1
if [ $? -eq 1 ] ; then
( echo check $url ; diff $old $new ) | $MAILJG -s "scuola $url"  jgp@cscs.ch
fi
mv $new $old

# -----------------------------------------------------------------
url='http://www.smgravesano.ti.ch/sede'
old=eff-old.gravesano2
new=eff-new.gravesano2
rm -f $new
w3m -dump $url > $new 2> /dev/null
diff -q $old $new > /dev/null
# if  NOdiff alors $?=0
# if YESdiff alors $?=1
if [ $? -eq 1 ] ; then
( echo check $url ; diff $old $new ) | $MAILJG -s "scuola $url"  jgp@cscs.ch
fi
mv $new $old

