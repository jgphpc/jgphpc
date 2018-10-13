#!/bin/bash

# ~/0.sh "date |head -1" ; ~/0.sh "hostname |sed s-jg-XX-";tput cup 0 0 ; tput ech `tput cols`


# echo -e '\033[41;37m fin de readnet.prog (dans readnet.prog) \033[0m'
# black='\E[30;47m'
# red='\E[31;47m'
# green='\E[32;47m'
# yellow='\E[33;47m'
# blue='\E[34;47m'
# magenta='\E[35;47m'
# cyan='\E[36;47m'
# white='\E[37;47m'
  
export PS1=">> "

# echo args = . $@ .

source $MODULESHOME/init/bash

blue='\e[0;32m'
#red='\e[0;31m'
red='\e[31;47m'
backtoblack='\e[1;37m'
road=`pwd |sed "s-/home/jg-~-"`
echo
echo -e "$blue""> $backtoblack $red $@ $backtoblack" 
tput sgr0
eval $@


echo
#tput cup 0 0 ; tput ech 160

# echo -e "\e[0;32m xxx \e[1;37m" ; date
exit 0

# man terminfo
# man tput
