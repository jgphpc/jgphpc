#!/bin/bash

echo "use rmconverter instead"
exit

inputfile=$1
inputfilename=$(echo $1 | sed 's/\.[^.]*$//')
ext='.mp3'
outputfilename=$inputfilename$ext

echo 'CONVERTING TO WAV FORMAT'
mplayer $inputfile -vc null -vo null -ao pcm:fast:waveheader:file=audiodump.wav

echo 'CONVERTING WAV FORMAT TO MP3'
lame -h -b 256 audiodump.wav $outputfilename

rm -f audiodump.wav

echo 'DONE...!'
