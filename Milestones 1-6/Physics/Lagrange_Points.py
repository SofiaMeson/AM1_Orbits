######################################### LAGRANGE POINTS FUNCTIONS ####################################################
## Lagrange points and their stability ##

from numpy.linalg import eig
from numpy import zeros
from scipy.optimize import fsolve
from Systems_of_equations.Newton import Jacobian
from Physics.CR3BProblem import CR3BP


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


