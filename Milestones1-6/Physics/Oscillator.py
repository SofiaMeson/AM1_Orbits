########################################## HARMONIC OSCILLATOR ###########################################

from numpy import array 

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