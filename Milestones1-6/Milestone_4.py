######################################### MILESTONE 4 ###########################################################
## Linear problems. Regions of absolute stability ##

from ODEs.Cauchy_Problem import Integrate_Cauchy
from ODEs.Time_Schemes import Euler, EI, RK4, CN, LF, choose_integration_method
from ODEs.Stability_Regions import Stability_regions
from Physics.Oscillator import Oscillator
from numpy import array, zeros, log10, ones, vstack, linspace, transpose 
from numpy.linalg import norm, lstsq
import matplotlib.pyplot as plt


# This module integrates the linear oscillator d2x/dt2 + dx/dt = 0 with different temporal schemes
# It also finds the absolute stability regions for the used temportal schemes

#Initial conditions:

user_n = input("Number of iterations (n) (note that it has to be an integer): ")
user_dt = input("Time interval (dt) (note that it needs to be 0.1, 0.01, 0.001... in order to be correct): ")
user_U_0= input("Enter the initial conditions for U_0 (x, y), separated by commas (e.g.: 1, 2): ")

n = int(user_n) 
dt = float(user_dt)
t = linspace(0, n*dt, n+1)
U_0 = array([float(x.strip()) for x in user_U_0.split(',')])

if U_0.size == 2:
    # Print the resulting vector
    print("The initial conditions array U_0 is:", U_0)
else:
    print("U_0 is not defined correctly (it needs to have 2 components).")


# Choose the integration method

integration_method = choose_integration_method()

# Integrate the Cauchy problem

U = Integrate_Cauchy(Oscillator, U_0, t, integration_method)

# Extract the position values
x = U[:, 0]
y = U[:, 1]

# Initial and final positions
x0, xf = x[0], x[-1]
y0, yf = y[0], y[-1]

print(f"Initial position: x0={x0}, y0={y0}")
print(f"Final position: xf={xf}, yf={yf}")


print ("The stability regions for a solution that has an acceptable output are plotted (if the user wants to plot the ones obtained, they just need to change the parameters inside the code):")
# As it becomes quite difficult to find an interval where the stability regions are clear, investigating the below range is 
# considered acceptable.


n = 100
x0 = -4
xf = 2
y0 = -4
yf = 4

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
    rho, x, y = Stability_regions(scheme, n, x0, xf, y0, yf)
    
    # Plot stability region contours
    contour = ax.contour(x, y, transpose(rho), levels=linspace(0, 1, 11))
    
    # Plot eigenvalues at (0, ±dt)
    ax.plot(0, dt, 'g+')
    ax.plot(0, -dt, 'g+')
    
    ax.axis('equal')
    ax.set_title(scheme_name)
    ax.grid()


plt.tight_layout()
plt.show()
