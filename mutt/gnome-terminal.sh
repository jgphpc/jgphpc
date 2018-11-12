#!/bin/bash
 
gnome-terminal \
 --tab -e "bash -c 'printf \"\033]0;---E---\007\";ssh -Y piccinal@dom.cscs.ch; bash'" \
 --tab -e "bash -c 'printf \"\033]0;---T---\007\";bash'" \
 --tab --working-directory=/home/piccinal/o -e "bash -c 'printf \"\033]0;---o---\007\"; bash'" \
 --tab --working-directory=/tmp -e "bash -c 'printf \"\033]0;---TMP---\007\"; bash'"

# --tab -e "bash ~/.titlejg; bash" \
# --tab -e "bash ~/.titlejg; bash" \

# --tab -e "bash -c 'printf \"\033]0;---E---\007\"; bash'" \
# --tab -e "bash -c 'printf \"\033]0;---T---\007\"; bash'" \
# --tab -e "bash -c 'printf \"\033]0;---o---\007\"; bash'"

# --tab-with-profile=jg -e 'bash source ~/.bashrc; set-titlejg fff; bash' \
# --tab-with-profile=jg -e 'bash' 

# --tab-with-profile=jg -e 'bash -c "ssh -Y piccinal@ela2.login.cscs.ch" ;bash' \
### --working-directory=/home/piccinal/o  --tab-with-profile=jg -e 'bash'
