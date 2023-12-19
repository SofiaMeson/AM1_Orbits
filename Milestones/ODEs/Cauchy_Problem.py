########### INTEGRATE CAUCHY PROBLEM ###############
from numpy import zeros
from ODEs.Time_Schemes import Euler, EI, CN, RK4


def Integrate_Cauchy(F, U_0, t, scheme):
    Nf = len (U_0) #number of rows needed
    Nc = len(t) - 1 #number of columns needed
    U = zeros((Nc + 1, Nf))
    U[0, :] = U_0
    

    for i in range(Nc):
        U[i + 1 , :] = scheme(F, U[i, :], t[i+1] - t[i], t[i])

   # x = U [0, :]
    #y = U [1, :]
    return U #, x, y






