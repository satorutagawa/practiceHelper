#!/usr/bin/env bash
set -e -x

input_1=$1
input_2=$2
OUTFILE=$3

echo ${input_1}
echo ${input_2}

#ffmpeg -f concat -safe 0 -i <(printf "file $PWD/${input_1}\nfile $PWD/${input_2}\n") -c copy ${OUTFILE}
#ffmpeg -i "concat:${input_1}|${input_2}" -c copy ${OUTFILE}

ffmpeg -i ${input_1} -acodec copy file1.aac
ffmpeg -i ${input_2} -acodec copy file2.aac
cat file1.aac file2.aac >>filenew.aac
ffmpeg -i filenew.aac -acodec copy -bsf:a aac_adtstoasc ${OUTFILE}
