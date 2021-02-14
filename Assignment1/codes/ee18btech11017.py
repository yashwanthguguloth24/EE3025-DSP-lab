import numpy as np
import matplotlib.pyplot as plt

def DFT(x):
    '''
    :param x: Time domain Signal
    :return: DFT of x --> X(k)
    '''
    N = len(x)
    W = 1j*np.zeros((N,N))
    w = np.exp(-1j*2.0*np.pi/N)
    W[1] = np.power(w*np.ones((N,)),1.0*np.arange(N))
    for i in range(N):
        W[i] = np.power(W[1],i)
    X = np.dot(W,x)
    return X


def IDFT(X):
    '''
    :param X: Frequency domain signal
    :return: time domain signal x
    '''
    N = len(X)
    W = 1j*np.zeros((N,N))
    w = np.exp(-1j*2.0*np.pi/N)
    W[1] = np.power(w*np.ones((N,)),1.0*np.arange(N))
    for i in range(N):
        W[i] = np.power(W[1],i)
    W_inv = (np.linalg.inv(W))
    x = np.dot(W_inv,X)
    return x



def x_n(N):
    '''
    :param N: Length of the signal neeeded
    :return: x with padded zeros to make signal of length N
    '''
    x = [1,2,3,4,2,1]
    if N > 6:
        x_new = np.pad(x,(0,N-6),'constant',constant_values=(0))
    else:
        x_new = x
    return x_new



def h_n(N):
    '''
    :param N: length
    :return: impulse response h computed from definition
    '''
    h = []
    for i in range(N):
        o = 0
        if i >= 0:
            o += pow(-0.5, i)
        if i - 2 >= 0:
            o += pow(-0.5, i - 2)
        h.append(o)
    return h



def main():
    N = 6
    x = x_n(N)
    X = DFT(x)
    h = h_n(N)
    H = DFT(h)
    Y = np.multiply(X,H)

    plt.figure(1,figsize=(9,7.5))
    plt.subplot(2,2,1)
    plt.stem(np.abs(X),use_line_collection=True)
    plt.title(r'$|X(k)|$')
    plt.grid()

    plt.subplot(2,2,2)
    plt.stem(np.angle(X),use_line_collection=True)
    plt.title(r'$\angle{X(k)}$')
    plt.grid()

    plt.subplot(2,2,3)
    plt.stem(np.abs(H),use_line_collection=True)
    plt.title(r'$|H(k)|$')
    plt.grid()

    plt.subplot(2,2,4)
    plt.stem(np.angle(H),use_line_collection=True)
    plt.title(r'$\angle{H(k)}$')
    plt.grid()


    plt.figure(2,figsize=(9,4))
    plt.subplot(1,2,1)
    plt.stem(np.abs(Y),use_line_collection=True)
    plt.title(r'$|Y(k)|$')
    plt.grid()

    plt.subplot(1,2,2)
    plt.stem(np.angle(Y),use_line_collection=True)
    plt.title(r'$\angle{Y(k)}$')
    plt.grid()


    plt.show()



main()
