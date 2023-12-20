from numpy import reshape, zeros
from numpy.linalg import norm

"""
___________________________________________________________________________________________________________
Definition of the function that characterizes the N body problem with pointers

- This function represents the differential operator for the N-body problem. It reshapes the input state 
vector `U` into a 3D array `Us` representing the positions and velocities of the bodies.
- The derivatives `F` are initialized as an array of zeros, and they are reshaped into a 3D array `dUs`.
- The positions and velocities are extracted from `Us`.
- The acceleration (`dvdt`) is set to zero for all bodies.
- The function then iterates through each body to calculate the acceleration based on the gravitational 
interaction with other bodies.
- The resulting derivatives (`F`) are returned as a reshaped 3D array.


   Inputs:
           U : state vector for the N-body problem
           t : array representing the time points at which the solution is computed
           Nb : number of bodies in the N-body problem
           Nc : number of coordinates for each body (normally, 3)

   Outputs:
           F : array representing the derivatives of the state vector


Author: Sofía Mesón Pérez (sofia.meson.perez@alumnos.upm.es) Dec 2023
___________________________________________________________________________________________________________

"""

# As the N-body problem implies the presence of multiple bodies, it is easier to utilize
# pointers to solve it 


# F is the differential operator for the N-body problem. 
def F_NBody(U, t, Nb, Nc): 
     
# Reshape to a Us (U_solution) and F to 3D form     
     Us  = reshape(U, (Nb, Nc, 2))
     F =  zeros(len(U))   
     dUs = reshape(F, (Nb, Nc, 2))  
     
     
     # Obtain position and velocity of the solution
     r = reshape(Us[:, :, 0], (Nb, Nc))    
     v = reshape(Us[:, :, 1], (Nb, Nc))
     
     # Obtain derivatives of the position (velocity) and the velocity (acceleration)
     drdt = reshape(dUs[:, :, 0], (Nb, Nc))
     dvdt = reshape(dUs[:, :, 1], (Nb, Nc))
    
     # ISet acceleration to 0
     dvdt[:,:] = 0 
    
     for i in range(Nb):   
       drdt[i,:] = v[i,:]
       for j in range(Nb): 
         if j != i:  
        # Distance between bodies i and j
           d = r[j,:] - r[i,:]
           dvdt[i,:] = dvdt[i,:] +  d[:] / norm(d)**3 
    
     return F

 