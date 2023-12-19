######################################### OSCILLATOR ####################################################

from numpy import array 

def Oscillator (U, t):
    x, y = U[0], U[1]
    return array([y, -x])