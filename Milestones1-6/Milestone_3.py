######################################### MILESTONE 3 ###########################################################
## Error estimation of numerical solutions ##

from ODEs.Cauchy_Problem import Integrate_Cauchy
from ODEs.Time_Schemes import Euler, EI, RK4, CN
from Physics.Kepler import F_Kepler
from Errors import Richardson_Cauchy_Problem, Temporal_Convergence_Rate
from numpy import array, zeros, log10, ones, vstack, linspace 
from numpy.linalg import norm, lstsq
import matplotlib.pyplot as plt


# The initial conditions may be changed. The ones used correspond to the ones used during the AM1 classes this semester

N = 10000
dt = 0.0001
N_conv = N/2        
m = 5                           # number of points in the graph 
t = linspace(0, N*dt, N+1)
U_0 = array ([1, 0, 0, 1])
custom_x_limits = [0, max(t)]
print(t)

# To evaluate the error of the numerical integration of orbit calculated integrating the Cauchy problem using different 
# temporal schemes (refer to milestone 2), the functions defined in the module "Error" will be used.

# The user selects the temporal scheme to calculate the error of numerical solutions of integrating the Cauchy problem using it:

print( "Select the desired temporal scheme to estimate the error of the integration of the Cauchy problem using it:" )
print( "     Explicit Euler = 1" )
print( "     Inverse Euler = 2" )
print( "     Crank-Nicolson = 3" )
print( "     Runge-Kutta order 4 = 4" )
print( "" )
scheme = int(input( "Introduce the number that corresponds to the desired time scheme: " ))
print( "" )


# The estimation is calculated using the functions defined in Errors.py, which uses means of Richardson extrapolation.

if scheme == 1:
    
    order = 1       # System of order 1
    
    print( "Numerical integration error for the Cauchy problem, using explicit Euler" )
    cauchy_error, U = Richardson_Cauchy_Problem(t, F_Kepler, Euler, order, U_0)
    
    print("Convergence rate of the explicit Euler time scheme")
    order_conv, log_e, log_n = Temporal_Convergence_Rate( t, F_Kepler, U_0, Euler, m)
    
    print( "order =", order_conv)
    
    # Plot for Euler temporal scheme error
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(t, cauchy_error[:, 0], color='blue')
    plt.xlabel('t')
    plt.xlim(custom_x_limits)
    plt.ylabel('Error Kepler orbit, Euler [-]')
    plt.title('Euler Temporal Scheme Error')
    plt.grid()

    # Plot for Euler temporal scheme convergence rate
    plt.subplot(1, 2, 2)
    plt.plot(log_n, log_e, color='blue')
    plt.xlabel('log(N)')
    plt.ylabel('log(E)')
    plt.title('Euler Temporal Scheme Convergence Rate')
    plt.grid()

    plt.tight_layout()
    plt.show()
    


elif scheme == 2:
    
    order = 2   # System of order 2
    
    print( "Numerical integration error for the Cauchy problem, using inverse Euler" )
    cauchy_error, U = Richardson_Cauchy_Problem(t, F_Kepler, EI, order, U_0)
    
    print("Convergence rate of the inverse Euler time scheme")
    order_conv, log_e, log_n = Temporal_Convergence_Rate( t, F_Kepler, U_0, EI, m)
    
    print( "order =", order)
    
    # Plot for inverse Euler temporal scheme error
    plt.figure(figsize=(12, 6))

    # Plot Inverse Euler temporal scheme error
    plt.subplot(1, 2, 1)
    plt.plot(t, cauchy_error[:, 0], color='green')
    plt.xlabel('t')
    plt.xlim(custom_x_limits)
    plt.ylabel('Error Kepler orbit, Inverse Euler [-]')
    plt.title('Inverse Euler Temporal Scheme Error')
    plt.grid()

    # Plot Inverse Euler temporal scheme convergence rate
    plt.subplot(1, 2, 2)
    plt.plot(log_n, log_e, color='green')
    plt.xlabel('log(N)')
    plt.ylabel('log(E)')
    plt.title('Inverse Euler Temporal Scheme Convergence Rate')
    plt.grid()

    plt.tight_layout()
    plt.show()
    
    

    
elif scheme == 3:
    
    order = 2       # System of order 2
    
    print( "Numerical integration error for the Cauchy problem, using Crank-Nicolson" )
    cauchy_error, U = Richardson_Cauchy_Problem(t, F_Kepler, CN, order, U_0)
    
    print("Convergence rate of the inverse Euler time scheme")
    order_conv, log_e, log_n = Temporal_Convergence_Rate( t, F_Kepler, U_0, CN, m)
    
    print( "order =", order)
    
    # Plot for Crank-Nicolson temporal scheme error
    plt.figure(figsize=(12, 6))

    # Plot Crank-Nicolson temporal scheme error
    plt.subplot(1, 2, 1)
    plt.plot(t, cauchy_error[:, 0], color='yellow')
    plt.xlabel('t')
    plt.xlim(custom_x_limits)
    plt.ylabel('Error Kepler orbit, Crank-Nicolson [-]')
    plt.title('Crank-Nicolson Temporal Scheme Error')
    plt.grid()

    # Plot Crank-Nicolson temporal scheme convergence rate
    plt.subplot(1, 2, 2)
    plt.plot(log_n, log_e, color='yellow')
    plt.xlabel('log(N)')
    plt.ylabel('log(E)')
    plt.title('Crank-Nicolson Temporal Scheme Convergence Rate')
    plt.grid()

    plt.tight_layout()
    plt.show()

    

elif scheme == 4:
    
    order = 4       # System of order 4
    
    print( "Numerical integration error for the Cauchy problem, using Runge-Kutta order 4" )
    cauchy_error, U = Richardson_Cauchy_Problem(t, F_Kepler, RK4, order, U_0)
    
    print("Convergence rate of the inverse Euler time scheme")
    order_conv, log_e, log_n = Temporal_Convergence_Rate( t, F_Kepler, U_0, CN, m)
    
    print( "order =", order)
    
    # Plot for Runge-Kutta order 4 temporal scheme error
    plt.figure(figsize=(12, 6))


    # Plot Runge-Kutta 4 temporal scheme error
    plt.subplot(1, 2, 1)
    plt.plot(t, cauchy_error[:, 0], color='red')
    plt.xlabel('t')
    plt.xlim(custom_x_limits)
    plt.ylabel('Error Kepler orbit, RK4 [-]')
    plt.title('Runge-Kutta Order 4 Temporal Scheme Error')
    plt.grid()

    # Plot Runge-Kutta 4 temporal scheme convergence rate
    plt.subplot(1, 2, 2)
    plt.plot(log_n, log_e, color='red')
    plt.xlabel('log(N)')
    plt.ylabel('log(E)')
    plt.title('Runge-Kutta Order 4 Temporal Scheme Convergence Rate')
    plt.grid()

    plt.tight_layout()
    plt.show()

else:

    print( "No time scheme found." )
    sys.exit()





