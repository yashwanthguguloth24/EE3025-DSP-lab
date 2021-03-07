import numpy as np
import matplotlib.pyplot as plt

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
            o += pow(-0.5,i)
        if i - 2 >= 0:
            o += pow(-0.5,i-2)
        h.append(o)
    return h




def FFT(x):
    N = len(x)
    # Base case
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

def main():
    N = 8
    x = x_n(N)
    X = FFT(x)
    h = h_n(N)
    H = FFT(h)
    Y = np.multiply(X,H)

    plt.figure(1,figsize=(7,15))
    plt.subplot(3,2,1)
    plt.stem(np.abs(X),use_line_collection=True)
    plt.title(r'$|X(k)|$')
    plt.grid()

    plt.subplot(3,2,2)
    plt.stem(np.angle(X),use_line_collection=True)
    plt.title(r'$\angle{X(k)}$')
    plt.grid()

    plt.subplot(3,2,3)
    plt.stem(np.abs(H),use_line_collection=True)
    plt.title(r'$|H(k)|$')
    plt.grid()

    plt.subplot(3,2,4)
    plt.stem(np.angle(H),use_line_collection=True)
    plt.title(r'$\angle{H(k)}$')
    plt.grid()

    plt.subplot(3,2,5)
    plt.stem(np.abs(Y),use_line_collection=True)
    plt.title(r'$|Y(k)|$')
    plt.grid()

    plt.subplot(3,2,6)
    plt.stem(np.angle(Y),use_line_collection=True)
    plt.title(r'$\angle{Y(k)}$')
    plt.grid()


    plt.show()



main()