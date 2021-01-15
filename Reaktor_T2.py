import collections
import numpy as np


f = open("Reaktor_T2_data", "r") # open file
signal = f.read() # save text to string variable

sub = signal # after first iteration, gives characters found in signal immediately after new base character
mode = None # most frequent in sub
base = None

while mode != ';':
    mode = collections.Counter(sub).most_common(1)[0][0] # use Counter to determine most frequent letter

    base = (base + mode if base else mode) # add character to base

    indices = [i + 1 for i, ltr in enumerate(signal) if ltr == mode] # (indices of mode in signal) + 1
    sub = ''.join([ltr for i, ltr in enumerate(signal) if i in indices]) # new string to examine


print(base[:-1]) # [:-1] --> prints without ';'
    





    
