########################################## HARMONIC OSCILLATOR ###########################################

from numpy import array, zeros, float64 

"""
___________________________________________________________________________________________________________
Definition of the function that represents the  differential operator of the harmonic oscillator system

    Inputs: 
            U : state vector (2 components)
            t : array representing the time points at which the solution is computed
            
    return: 
            1D array that characterizes the harmonic oscillator
          
Author: Sofía Mesón Pérez (sofia.meson.perez@alumnos.upm.es) Dec 2023
___________________________________________________________________________________________________________

"""

def Oscillator (U, t):
    x, y = U[0], U[1]
    return array([y, -x])


def System_matrix(F, U0, t):

    eps=1e-6
    N=len(U0)
    A = zeros((N,N), dtype=float64)
    delta = zeros(N)

    for j in range(N):
        delta[:] = 0
        delta[j] = eps
        A[:,j] = (F(U0 + delta, t)-F(U0 - delta, t))/(2*eps)

    return A
