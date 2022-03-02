import pylab as py
import numpy as np
from numpy.fft import rfft, rfftfreq

def sin(f = 1, T = 1, fs = 128, phi =0 ):
    dt = 1.0/fs
    t = np.arange(0,T,dt)
    s = np.sin(2*np.pi*f*t + phi)
    return (s,t)

from scipy.fft import fft, fftfreq
fs = 100
T = 1

(y,t) = sin(f = 10.0, T=T, fs=fs)

N=int(Fs*T)

yf = fft(y)
xf = ......
import matplotlib.pyplot as plt
plt.stem(xf, np.abs(yf), use_line_collection=True)
plt.grid()
plt.show()
