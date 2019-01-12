#!/usr/bin/env python3

import sys
import time
import logging

import Utils
import AudioTool

logger = logging.getLogger(__name__)

def main():
    input_file = "/data/440_flat.wav"

    t0 = time.time()
    freq = AudioTool.get_freq(input_file, 440)
    t1 = time.time()
    logger.info("get_freq: %f" % (t1-t0))

    score = AudioTool.PitchCmp(440,freq)
    logger.info("score: %d" % score)

if __name__ == "__main__":
    main()
