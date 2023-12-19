######################################### MILESTONE 3 ####################################################
## Error estimation of numerical solutions ##

from ODEs.Cauchy_Problem import Integrate_Cauchy
from ODEs.Time_Schemes import Euler, EI, RK4, CN
from Physics.Kepler import F_Kepler
from Errors import Richardson_Cauchy_Problem, Temporal_Convergence_Rate
from numpy import array, zeros, log10, ones, vstack, linspace 
from numpy.linalg import norm, lstsq
import matplotlib.pyplot as plt




# The initial conditions may be changed. The ones used correspond to the ones used during
# the AM1 classes this semester.
N = 5000
dt = 0.001
N_conv = N/2        
m = 5       # number of points in the graph 
t = linspace(0, N*dt, N+1)
U_0 = array ([1, 0, 0, 1])






# To evaluate the error of the numerical integration of the Cauchy problem, achieved in the 
# milestone 2, the functions defined in the module "Error" will be used.

# To evaluate the error in the numerical integration of the Cauchy problem by using different
# time schemes, the user must

print( "Select the desired time scheme to determine the Cauchy's problem numerical integration error:" )
print( "     Explicit Euler = 1" )
print( "     Inverse Euler = 2" )
print( "     Crank-Nicolson = 3" )
print( "     Runge-Kutta order 4 = 4" )
print( "" )
scheme = int(input( "Introduce the number that corresponds to the desired time scheme: " ))
print( "" )



if scheme == 1:
    
    order = 1       # System of order 1
    
    print( "Numerical integration error for the Cauchy problem, using explicit Euler" )
    cauchy_error, U = Richardson_Cauchy_Problem(t, F_Kepler, Euler, order, U_0)
    
    plt.figure (1)
    plt.plot(t, cauchy_error[:,0], color = 'blue' )
    plt.xlabel('t')
    plt.ylabel('Error Kepler orbit, Euler')
    plt.title('Euler time scheme')  
    plt.grid()

    
    print("Convergence rate of the explicit Euler time scheme")
    order_conv, log_e, log_n = Temporal_Convergence_Rate( t, F_Kepler, U_0, Euler, m)
    
    print( "order =", order)
    
    plt.figure (2)
    plt.plot(log_n, log_e, color = 'blue' )
    plt.xlabel('log(N)')
    plt.ylabel('log(E)')
    plt.title('Euler time scheme convergence rate')  
    plt.grid()
    plt.show()
    

elif scheme == 2:
    
    order = 2 
    
    print( "Numerical integration error for the Cauchy problem, using inverse Euler" )
    cauchy_error, U = Richardson_Cauchy_Problem(t, F_Kepler, EI, order, U_0)
    
    plt.figure (3)
    plt.plot(t, cauchy_error[:,0], color = 'green' )
    plt.xlabel('t')
    plt.ylabel('Error Kepler orbit, inverse Euler')
    plt.title('Inverse Euler time scheme')  
    plt.grid()

    
    print("Convergence rate of the inverse Euler time scheme")
    order_conv, log_e, log_n = Temporal_Convergence_Rate( t, F_Kepler, U_0, EI, m)
    
    print( "order =", order)
    
    plt.figure (4)
    plt.plot(log_n, log_e, color = 'green' )
    plt.xlabel('log(N)')
    plt.ylabel('log(E)')
    plt.title('Inverse Euler time scheme convergence rate')  
    plt.grid()
    plt.show()
    
    

    
elif scheme == 3:
    
    order = 2
    
    print( "Numerical integration error for the Cauchy problem, using Crank-Nicolson" )
    cauchy_error, U = Richardson_Cauchy_Problem(t, F_Kepler, CN, order, U_0)
    
    plt.figure (5)
    plt.plot(t, cauchy_error[:,0], color = 'red' )
    plt.xlabel('t')
    plt.ylabel('Error Kepler orbit, CN')
    plt.title('Crank-Nicolson time scheme')  
    plt.grid()

    
    
    print("Convergence rate of the inverse Euler time scheme")
    order_conv, log_e, log_n = Temporal_Convergence_Rate( t, F_Kepler, U_0, CN, m)
    
    print( "order =", order)
    
    plt.figure (6)
    plt.plot(log_n, log_e, color = 'red' )
    plt.xlabel('log(N)')
    plt.ylabel('log(E)')
    plt.title('Crank-Nicolson time scheme convergence rate')  
    plt.grid()
    plt.show()
    

elif scheme == 4:
    
    order = 4
    
    print( "Numerical integration error for the Cauchy problem, using Runge-Kutta order 4" )
    cauchy_error, U = Richardson_Cauchy_Problem(t, F_Kepler, RK4, order, U_0)
    
    plt.figure (7)
    plt.plot(t, cauchy_error[:,0], color = 'yellow' )
    plt.xlabel('t')
    plt.ylabel('Error Kepler orbit, RK4')
    plt.title('Runge-Kutta order 4 time scheme')  
    plt.grid()

    
    print("Convergence rate of the inverse Euler time scheme")
    order_conv, log_e, log_n = Temporal_Convergence_Rate( t, F_Kepler, U_0, CN, m)
    
    print( "order =", order)
    
    plt.figure (8)
    plt.plot(log_n, log_e, color = 'yellow' )
    plt.xlabel('log(N)')
    plt.ylabel('log(E)')
    plt.title('Runge-Kutta order 4 time scheme convergence rate')  
    plt.grid()
    
    plt.show()
    

else:

    print( "No time scheme found." )
    sys.exit()





