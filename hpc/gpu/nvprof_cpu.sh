#!/bin/bash
# USAGE: Add between aprun options and executable
# For Example: aprun -n 16 -N 1 ./foo arg1 arg2
# Becomes: aprun -n 16 -N 1 ./nvprof.sh ./foo arg1 arg2
export PMI_NO_FORK=1 
export TMPDIR=/tmp/$ALPS_APP_PE
mkdir -p $TMPDIR

# Give each *rank* a separate file
LOG=timeline_$ALPS_APP_PE.nvprof

# Set the process and context names
NAME="MPI Rank: %q{ALPS_APP_PE}"

# Stripe each profile file by 1 to share the load on large runs
#if [ !-f $LOG ] ; then lfs setstripe -c 1 $LOG ; fi
lfs setstripe -c 1 $LOG 

# Execute the provided command.
#echo nvprof --cpu-profiling on --process-name "$NAME" --context-name "$NAME" -o "$LOG" $*

# if [ "$ALPS_APP_PE" = 0 ] ;then
exec nvprof --cpu-profiling on --process-name "$NAME" --context-name "$NAME" -o "$LOG" $*
# else
# exec $*
# fi
#exec nvprof --cpu-profiling off --process-name "$NAME" --context-name "$NAME" -o "$LOG" $*
#exec nvprof --process-name "$NAME" --context-name "$NAME" -o "$LOG" $*
