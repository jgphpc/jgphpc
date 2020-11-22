#!/bin/bash
WAV="$1"
if [ -z "$WAV" ]; then
    echo "Usage: $0 OUTPUT.WAV" >&2
    exit 1
fi
rm -f "$WAV"
 
# Get sink monitor:
# pactl: control a running PulseAudio sound server
MONITOR=$(pactl list | egrep -A2 '^(\*\*\* )?Source #' | \
    grep 'Name: .*\.monitor$' | awk '{print $NF}' | tail -n1)
echo "set-source-mute ${MONITOR} false" | pacmd >/dev/null
 
# Record it raw, and convert to a wav
echo "Recording to $WAV ..."
echo "Close this window to stop"
# parec: Playback/record raw or encoded audio streams on a PulseAudio sound server
# sox: Sound eXchange, the Swiss Army knife of audio manipulation
parec -d "$MONITOR" |sox -t raw -r 44k -sLb 16 -c 2 - "$WAV"
