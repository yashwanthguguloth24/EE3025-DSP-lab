# Run Time comparisions
import time
import numpy as np
import matplotlib.pyplot as plt

def DFT(x):
    '''
    :param x: Time domain Signal
    :return: DFT of x --> X(k)
    '''
    N = len(x)
    if N == 1:
        return x
    W = 1j*np.zeros((N,N))
    w = np.exp(-1j*2.0*np.pi/N)
    W[1] = np.power(w*np.ones((N,)),1.0*np.arange(N))
    for i in range(N):
        W[i] = np.power(W[1],i)
    X = np.dot(W,x)
    return X

def FFT(x):
    N = len(x)
    # Base cases
    if N == 1:
        return x

    if (N == 2):
        return np.hstack((x[0]+x[1],x[0]-x[1]))
    # even point fft
    Xe = FFT(x[::2])
    # odd point fft
    Xo = FFT(x[1::2])

    D = np.zeros((N//2,),dtype=np.complex128)
    for i in range(N//2):
        D[i] = np.exp(-2j*np.pi*i/N)

    X_u = Xe + D*Xo
    X_l = Xe - D*Xo
    return np.hstack((X_u,X_l))

K = 14
DFT_comp_time = np.zeros(K)
FFT_comp_time = np.zeros(K)
FFTinBuilt_comp_time = np.zeros(K)

for i in range(K):
    n = 2**i
    x = np.random.randint(1,5,size=n)
    t1 = time.time()
    X_DFT = DFT(x)
    t2 = time.time()
    X_FFT = FFT(x)
    t3 = time.time()
    X_FFT_inBuilt = np.fft.fft(x)
    t4 = time.time()
    DFT_comp_time[i] = t2-t1
    FFT_comp_time[i] = t3-t2
    FFTinBuilt_comp_time[i] = t4-t3

ax = 2**np.arange(K)
plt.plot(ax,DFT_comp_time,label='DFT')
plt.plot(ax,FFT_comp_time,label='FFT')
plt.plot(ax,FFTinBuilt_comp_time,label='Inbuilt FFT')
plt.title('Computation Times comparision')
plt.xlabel('n')
plt.xscale('log',basex=2)
plt.ylabel('Execution Time(s)')
plt.grid()
plt.legend()
plt.show()






