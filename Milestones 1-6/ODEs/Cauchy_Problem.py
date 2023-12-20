################################## INTEGRATE CAUCHY PROBLEM #######################################
from numpy import zeros
from ODEs.Time_Schemes import Euler, EI, CN, RK4, ERK

"""
__________________________________________________________________________________________________
Function to integrate the Cauchy problem, using different temporal schemes

    Inputs: 
            F : represents the  differential operator of the ODE. Imported from Kepler.py, 
            Nbody_functions.py, Oscillator.py or, in the case of the circular restricted 3 body 
            problem, it uses the F defined in Milestone_6.py
            U_0 : initial conditions for the system of ODEs
            t : array representing the time points at which the solution is computed
            scheme : selected numerical method to solve the problem. Imported from Time_schemes.py 
             
    return: 
            U : state array. Each row represented the state vector ar a specific time point
          
Author: Sofia Meson Perez (sofia.meson.perez@alumnos.upm.es) Dec 2023
__________________________________________________________________________________________________

"""
def Integrate_Cauchy(F, U_0, t, scheme):
    Nf = len (U_0) #number of rows needed
    Nc = len(t) - 1 #number of columns needed
    U = zeros((Nc + 1, Nf))
    U[0, :] = U_0
    

    for i in range(Nc):
        U[i + 1 , :] = scheme(F, U[i, :], t[i+1] - t[i], t[i])

    #x = U [0, :]
    #y = U [1, :]
    return U 






