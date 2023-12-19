from numpy import reshape, zeros
from numpy.linalg import norm

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

 