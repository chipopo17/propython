import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

N=16
t=np.arange(N)
x=np.cos(2*np.pi/N*t)

from scipy.fftpack import fft, ifft

X=fft(x)

plt.plot(np.abs(X),'bo-')
plt.plot(np.real(X),'go-')
plt.plot(np.imag(X),'ro-')

plt.show()
