########### INTEGRATE CAUCHY PROBLEM ###############
import numpy as np
from Time_Schemes import Euler, EI, CN, RK4

def Integrate_Cauchy(F, U_0, t, Scheme):
    Nf = len (U_0) #number of rows needed
    Nc = len(t) - 1 #number of columns needed
    U = np.zeros((Nf, Nc + 1))
    U[:, 0] = U_0
    dt = t[2] - t[1]

    for i in range(Nc):
        U[:, i + 1] = Scheme(F, U[:, i], dt)

   # x = U [0, :]
    #y = U [1, :]
    return U #, x, y




