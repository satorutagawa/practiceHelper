#!/usr/bin/env python3

import sys
import time
import logging

import Utils
import AudioTool

logger = logging.getLogger(__name__)

def main():
    input_file = "/data/440_flat.m4a"
    input_midi = "/data/440.mid"

    t0 = time.time()
    freq = AudioTool.get_freq(input_file, 440)
    t1 = time.time()
    logger.info("get_freq: %f" % (t1-t0))

    ref_freq = AudioTool.read_midi(input_midi)

    score = AudioTool.pitch_cmp(ref_freq, freq)
    logger.info("score: %d" % score)

if __name__ == "__main__":
    main()
