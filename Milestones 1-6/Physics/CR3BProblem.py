################################# CIRCULAR RESTRICTED 3 BODY PROBLEM #######################################

from numpy import sqrt, array

"""
_________________________________________________________________________________________________________________
Definition of the circular restriced 3-body problem

    Inputs: 
            U : state vector
            mu :  scalar parameter representing the mass ratio in the circular restricted three-body problem
            
    return: 
            1D array representing the time derivatives of the state vector. These derivatives are used to update
            the state vector in a numerical integration scheme
            
          
Author: Sofia Meson Perez (sofia.meson.perez@alumnos.upm.es) Dec 2023
_________________________________________________________________________________________________________________

"""

def CR3BP(U, mu):
    r = U[0:2]          # Position vector            
    drdt = U[2:4]       # Velocity vector

    # Positions 1 and 2
    r1 = sqrt((r[0]+mu)**2 + r[1]**2)       
    r2 = sqrt((r[0]-1+mu)**2 + r[1]**2)

    # Accelerations 1 and 2
    dvdt_1 = - (1 - mu)*(r[0] + mu)/(r1**3) - mu*(r[0] - 1 + mu)/(r2**3)
    dvdt_2 = - (1 - mu)*r[1]/(r1**3) - mu*r[1]/(r2**3)

    return array([drdt[0], drdt[1], 2*drdt[1] + r[0] + dvdt_1, -2*drdt[0] + r[1] + dvdt_2])



