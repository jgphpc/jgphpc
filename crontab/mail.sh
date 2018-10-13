#!/bin/bash
in="$1"
echo "$in" | mail -s "crontab: $in" -r jgp@cscs.ch jgp@cscs.ch
