#!/bin/bash

ssh ela2.login.cscs.ch "rm -f /users/piccinal/efface/sent"
ssh ela2.login.cscs.ch "touch /users/piccinal/efface/sent"
ssh ela2.login.cscs.ch "ln -fs /users/piccinal/efface/sent"
ssh ela2.login.cscs.ch "rm -f /tmp/mutt-ela2*"
ssh ela2.login.cscs.ch "rm -f /users/piccinal/core*"

exit 0
