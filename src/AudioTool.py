import os
import logging
import scipy.io.wavfile
import numpy as np
#import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

# Returns how much samp is off from ref by
#   100% :  Within 1/8 pitch
#    75% :  Within 1/4 pitch
#    50% :  Within 1/2 pitch
#    25% :  Within 1 pitch
#     0% :  > 1 pitch
def PitchCmp(ref,samp):
    ref = float(ref)
    ref_whole_high   = ref * 2**(2.0/12)
    ref_whole_low    = ref * 2**(-2.0/12)
    ref_half_high    = ref * 2**(1.0/12)
    ref_half_low     = ref * 2**(-1.0/12)
    ref_quarter_high = ref * 2**(0.5/12)
    ref_quarter_low  = ref * 2**(-0.5/12)
    ref_eighth_high  = ref * 2**(0.25/12)
    ref_eighth_low   = ref * 2**(-0.25/12)
    ref_sixteenth_high  = ref * 2**(0.125/12)
    ref_sixteenth_low   = ref * 2**(-0.125/12)

    logger.debug([ref,samp])
    logger.debug([100,ref_sixteenth_low, ref_sixteenth_high])
    logger.debug([75,ref_eighth_low, ref_eighth_high])
    logger.debug([50,ref_quarter_low, ref_quarter_high])
    logger.debug([25,ref_half_low, ref_half_high])
    logger.debug([12.5,ref_whole_low, ref_whole_high])

    if ref_sixteenth_low < samp < ref_sixteenth_high:
        return 100
    if ref_eighth_low < samp < ref_eighth_high:
        return 75 
    elif ref_quarter_low < samp < ref_quarter_high:
        return 50
    elif ref_half_low < samp < ref_half_high:
        return 25
    elif ref_whole_low < samp < ref_whole_high:
         return 12
    else:
        return 0

def get_freq(fname, freq_ref):
    [fs, data] = scipy.io.wavfile.read(fname)

    logger.info("fs = %d" % fs)
    logger.info("#samples = %d" % data.size)

    #t = np.linspace(0,data.size/fs, data.size)
    #plt.plot(t,data)
    #plt.show()

    data_fft = np.fft.fft(data)
    data_fft = data_fft[range(int(data.size/2))]

    freq = np.fft.fftfreq(data.size, 1.0/fs)
    freq = freq[range(int(data.size/2))]

    freq_ref_high = freq_ref * 2**(2.0/12)
    freq_ref_low  = freq_ref * 2**(-2.0/12)

    indices = np.where(np.logical_and(freq > freq_ref_low, freq < freq_ref_high))

    max_ind = np.argmax(data_fft[indices])
    max_freq = freq[indices][max_ind]

    logger.info(max_freq)

    return max_freq
