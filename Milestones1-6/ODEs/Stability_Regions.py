######################################### STABILITY REGIONS ########################################

from ODEs.Time_Schemes import Euler, EI, RK4, CN, LF
from numpy import zeros, linspace, abs, float64, array, transpose
import matplotlib.pyplot as plt

"""
__________________________________________________________________________________________________
Stability regions

    Inputs: 
            - x0, xf : Initial and final values for the x variable
            - y0, yf: Initial and final values for the y variable
            - N : number of points on the grid in the x and y directions. This parameter determines
                  the resolution of the grid
            - scheme : selected numerical method to solve the problem. Imported from Time_schemes.py 
             
    return: 
            - rho: matrix of size (N, N) containing the absolute values of the solutions calculated by 
                   the numerical scheme
            - x: 1D array representing the grid in the x direction
            - y: 1D array representing the grid in the y direction
          
Author: Sofía Mesón Pérez (sofia.meson.perez@alumnos.upm.es) Dec 2023
__________________________________________________________________________________________________

"""


# This function calculates stability regions for each temporal scheme
def Stability_regions (scheme, N, x0, xf, y0, yf): 

    x = linspace(x0, xf, N)
    y = linspace(y0, yf, N)
    rho = zeros((N, N), dtype=float64)

    for i in range(N): 
        for j in range(N):

            w = complex(x[i], y[j])
            r = scheme(lambda u, t: w*u, 1.,  1., 0.)

            rho[i, j] = abs(r) 

    return rho, x, y


# This function tests the previous one, plotting the results for the different schemes
def test_Stability_regions(): 

    time_schemes = {
        Euler: "Euler",
        EI: "Inverse Euler",
        RK4: "Runge-Kutta 4",
        CN: "Crank-Nicolson",
        LF: "Leap-Frog"
    }

    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    axes = axes.flatten()

    for ax, (scheme, scheme_name) in zip(axes, time_schemes.items()):
        rho, x, y = Stability_regions(scheme, 100, -4, 2, -4, 4)
        contour = ax.contour(x, y, transpose(rho), levels=linspace(0, 1, 11))
        ax.axis('equal')
        ax.grid()
        ax.set_title(f"Stability Region - {scheme_name}")


    plt.tight_layout()
    plt.show()


    
    
if __name__ == '__main__':  
    test_Stability_regions()  # It only calls the test function if the script is being run as the main program.