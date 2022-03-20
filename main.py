import pandas as pd
import pylab as py
import numpy as np
from numpy.fft import rfft, rfftfreq

def sin(f = 1, T = 1, fs = 128, phi =0 ):
    dt = 1.0/fs
    t = np.arange(0,T,dt)
    s = np.sin(2*np.pi*f*t + phi)
    return (s,t)

from scipy.fft import fft, fftfreq

import h5py
import numpy as np
import pandas as pd
filename = "./emg_gestures-12-repeats_short-2018-04-12-14-05-19-091.hdf5"


df = pd.read_hdf(filename)
emg15 = df["EMG_15"]
print(emg15)


