import os

# Returns how much samp is off from ref by
#   100% :  Within 1/8 pitch
#    75% :  Within 1/4 pitch
#    50% :  Within 1/2 pitch
#    25% :  Within 1 pitch
#     0% :  > 1 pitch
def pitchCmp(ref,samp):
	ref_whole_high   = ref * 2**(2.0/12)
	ref_whole_low    = ref * 2**(-2.0/12)
	ref_half_high    = ref * 2**(1.0/12)
	ref_half_low     = ref * 2**(-1.0/12)
	ref_quarter_high = ref * 2**(0.5/12)
	ref_quarter_low  = ref * 2**(-0.5/12)
	ref_eighth_high  = ref * 2**(0.25/12)
	ref_eighth_low   = ref * 2**(-0.25/12)


	print(ref,samp)
	print(100,ref_eighth_low, ref_eighth_high)
	print(75,ref_quarter_low, ref_quarter_high)
	print(50,ref_half_low, ref_half_high)
	print(25,ref_whole_low, ref_whole_high)

	if ref_eighth_low < samp < ref_eighth_high:
		return 100
	elif ref_quarter_low < samp < ref_quarter_high:
		return 75
	elif ref_half_low < samp < ref_half_high:
		return 75
	elif ref_whole_low < samp < ref_whole_high:
		return 75
	else:
		return 0
