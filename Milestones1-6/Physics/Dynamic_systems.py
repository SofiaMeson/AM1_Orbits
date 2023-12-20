################################ Dynamic Systems Integration ####################################
from numpy import array, zeros, linspace
import matplotlib.pyplot as plt
from scipy.optimize import fsolve, newton
from mpl_toolkits.mplot3d import axes3d
import math as math


"""
_________________________________________________________________________________________________________________
Definition of different dynamic systems

    Inputs: 
           - U : state vector
           - t : array representing the time points at which the solution is computed
            
    return: 
            1D array that characterizes each dynamic system
            
          
Author: Sofía Mesón Pérez (sofia.meson.perez@alumnos.upm.es) Dec 2023
_________________________________________________________________________________________________________________

"""

## In this program, the user will be able to plot different dynamic systems by solving them solving
## the Cauchy problem using different time schemes.

## Examples of dynamic systems

# Chaotic systems with k<1
def ODE_DUffing(U, t): 
    x, y = [U[0], U[1]]

    vx=y
    vy=-x**3-0.01*y+math.cos(t)

    return array( [vx, vy] )

def ODE_Van_Der_Por_1(U, t): 
    x, y = [U[0], U[1]]

    vx=y
    vy=-0.2*(x**2-1)*y-x

    return array( [vx, vy] )

def ODE_Van_Der_Por_2(U, t): 
    x, y = [U[0], U[1]]

    vx=y
    vy=-5*(x**2-1)*y-x

    return array( [vx, vy] )

def ODE_Rayleigh(U, t): 
    x, y = [U[0], U[1]]

    vx=y
    vy=x-x**3-y+0.6*math.cos(t)

    return array( [vx, vy] )

def ODE_Rayleigh2(U,t):
    x, y = [U[0], U[1]]
    vx=y
    vy=x-x**3-y+0.7*math.cos(t)

    return array( [vx, vy] )
    
def Lorentz (U, t):
    #es un oscilador
    x = U[0]
    y = U [1]
    z = U [2]
    
    r = 28
    b = 8/3
    s = 10
    
    return array ([- s*x + s*y, r*x - x*z - y, -b*z + x*y])

def Rossler (U,t):
    #otro oscilador donde se cumple que no se corta ninguna orbita, hay dependencia continua..
    x = U[0]
    y = U [1]
    z = U [2]
    
    a = 0.398
    b = 2
    c = 4
    
    return array ([-y - z, a*y + x, b + z*(x -c)])

def Rossler2 (U,t):
    x = U[0]
    y = U [1]
    z = U [2]
    
    a = 0.17
    b = 0.4
    c = 8.5
    
    return array ([-y - z, a*y + x, b + z*(x -c)])
   

