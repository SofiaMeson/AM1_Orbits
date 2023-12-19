######################################### CIRCULAR RESTRICTED 3 BODY PROBLEM ####################################################

from numpy import sqrt, array


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

