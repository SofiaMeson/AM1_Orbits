########### INTEGRATE CAUCHY PROBLEM ###############
import numpy as np
from Time_Schemes import Euler, EI, CN, RK4

def Integrate_Cauchy(F, U_0, t, Scheme):
    N = len(t) - 1
    U = np.zeros((len(U_0), N + 1))
    U[:, 0] = U_0
    dt = t[2] - t[1]

    for i in range(N):
        U[:, i + 1] = Scheme(F, U[:, i], dt)

    return U




