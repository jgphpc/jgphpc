#!/bin/bash

#crontab: # m h  dom mon dow   command
#crontab: # vim => set nobackup nowritebackup
#crontab: 0 18 * * * /Users/jg/linux.git/crontab/ski.sh > /dev/null

unset DISPLAY
tstamp=`date +%Y%m%d-%H%M%S`
cd ~/linux.git/crontab/
url='http://www.infosnow.ch/~apgmontagne/?tab=web&xid=164&saison=1&lang=it'
data=`/usr/local/bin/w3m -dump "$url" |grep "Ultima mutazione" |awk '{print $3}'`
if [ "$data" != "21.03.2016" ] ;then
    ssh -x piccinal@ela2.login.cscs.ch /users/piccinal/linux.git/crontab/mail.sh "checkmacjg $url"
fi
# echo "$tstamp $data"
