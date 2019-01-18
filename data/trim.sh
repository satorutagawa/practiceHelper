#!/bin/bash -x

input_audio=$1
start_sec=$2
end_sec=$3
OUTFILE=$4

ffmpeg -y -i ${input_audio} -acodec copy -ss ${start_sec} -to ${end_sec} ${OUTFILE} < /dev/null 2> /dev/null
