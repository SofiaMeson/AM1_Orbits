######################################### LAGRANGE POINTS FUNCTIONS ####################################################
## Lagrange points and their stability ##

from numpy.linalg import eig
from numpy import zeros
from scipy.optimize import fsolve
from Systems_of_equations.Newton import Jacobian
from Physics.CR3BProblem import CR3BP

"""
___________________________________________________________________________________________________________
Definition of the functions that calculate Lagrange points and their stability

# Function 1: Lagrange_points
This function calculates the positions of Lagrange points in the Circular Restricted Three-Body Problem 
(CR3BP). It uses an iterative method (fsolve) to find the roots of a system of equations defined by the
function `F(Y)`. The initial guesses for the roots are provided by the input array `U_0`.
The output L_P contains the x and y coordinates for each of the `Np`calculated Lagrange points.

     Inputs:
             U_0 : 2D array representing the initial conditions for Lagrange points (x,y)
             Np: number of Lagrange points to calculate
             mu : scalar parameter representing the mass ratio in the CR3BP

     Output:
             L_P : 2D array of shape (5, 2) representing the calculated Lagrange points

# Function 2: Stability_LP
ThIS function checks the stability of the calculated Lagrange points in the CR3BP. It computes the Jacobian 
matrix (imported from Physics.Newton.py) of the CR3BP system evaluated at the Lagrange points. The eigenvalues 
of the Jacobian matrix are computed and returned.

     Inputs:
             U_0`: 2D array representing the initial conditions for Lagrange points
             mu : scalar parameter representing the mass ratio in the CR3BP

     Output:
             values : array containing the eigenvalues of the Jacobian matrix evaluated at the Lagrange points

Author: Sofia Meson Perez (sofia.meson.perez@alumnos.upm.es) Dec 2023
___________________________________________________________________________________________________________

"""

# Np refers to the umber of points of Lagrange
def Lagrange_points(U_0, Np, mu):
    
    L_P = zeros([5,2])

    def F(Y):
        X = zeros(4)
        X[0:2] = Y
        X[2:4] = 0
        FX = CR3BP(X, mu)
        return FX[2:4]
   
    for i in range (Np):
        L_P[i,:] = fsolve(F, U_0[i,0:2])

    return L_P


# Checks the stability of the calculated Lagrange Points
def Stability_LP(U_0, mu):

    def F(Y):
        return CR3BP(Y, mu)

    A = Jacobian(F, U_0)
    values, vectors = eig(A)

    return values


