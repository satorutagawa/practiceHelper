#!/usr/bin/env python3

import sys
import time
import logging

import Utils
import AudioTool

logger = logging.getLogger(__name__)

def main():
    input_file = "/data/A4-A4_flat_1s.m4a"
    input_midi = "/data/A4.mid"

#    AudioTool.create_midi('example.mid')

    ref_freq = AudioTool.read_midi(input_midi)

#    t0 = time.time()
#    freq = AudioTool.get_freq(input_file, ref_freq)
#    t1 = time.time()
#    logger.info("get_freq: %f" % (t1-t0))
#
#    score = AudioTool.pitch_cmp(ref_freq, freq)
#    logger.info("score: %d" % score)

if __name__ == "__main__":
    main()
