import numpy as np
import matplotlib.pyplot as plt

def BM():
    T = 100
    # del = 1
    # del = 0.1
    # del = 0.01
    # del = 0.001
    # del = 0.0001
    # del = 0.00001
    delta = 0.000001

    sig = 1

    nT = int(T / delta)

    VecX = np.zeros(nT + 1)
    VecT = np.zeros(nT + 1)

    delX = sig * (delta)**(1/2)
    X = 0
    tem = 0
    Comp = 0

    VecX[0] = X
    VecT[0] = tem

    for i in range(nT):
        Al = np.random.rand()
        if Al > 0.5:
            pr = 1
        else:
            pr = -1
        X = X + pr * delX
        tem = tem + delta
        VecX[i + 1] = X
        VecT[i + 1] = tem
        Comp = Comp + delX

    return VecX, VecT, Comp

VecX, VecT, Comp = BM()

plt.plot(VecT, VecX)
plt.xlabel('Tempo')
plt.ylabel('Brownian Motion')
plt.grid(True)
plt.show()
