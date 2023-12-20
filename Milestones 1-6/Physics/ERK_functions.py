######################################### ERK FUNCTIONS ####################################################
## Functions that the embedded Runge-Kutta time scheme uses ##


from scipy.optimize import newton
from numpy import zeros, matmul, size, linspace
from numpy.linalg import norm



"""
_________________________________________________________________________________________________________________
Definition of the embedded Runge-Kutta program functions

# Function 1: RK_stages
    This function performs one step of the Runge-Kutta method for a specified order. It uses the Butcher array 
    coefficients obtained from the "butcher" function. The intermediate values `k` are computed based on the 
    coefficients.

     Inputs:
            order: integer representing the order of the Runge-Kutta method
            U1 : current state vector
            t : array representing the time points at which the solution is computed
            dt : time step, determining the size of the time intervals between iterations
            F : a function representing the  differential operator

     Output:
            U2 : state vector after one step of the Runge-Kutta method


# Function 2: StepSize
    This function computes the adaptive time step size 
     
     Inputs:
             dU : 1D array representing the difference between two solutions
             tol: specified tolerance
             dt : current time step
             orders : order of accuracy

     Output:
             step_size: adaptive time step size based on the error between two solutions, the specified tolerance,
             and the orders of accuracy



# Function 3: butcher
 This function defines the Butcher array coefficients for the embedded Runge-Kutta method. These coefficients are 
 used in the `RK_stages` function to perform one step of the Runge-Kutta method

     Outputs:
             orders: list of integers representing the orders of accuracy for the embedded Runge-Kutta method
             Ns: integer representing the number of stages
             a : 2D array containing the coefficients \(a\) for the Butcher array
             b : 1D array containing the coefficients \(b\) for the Butcher array
             bs : 1D array containing the coefficients \(b_s\) for the Butcher array
             c : 1D array containing the coefficients \(c\) for the Butcher array
          
Author: Sofia Meson Perez (sofia.meson.perez@alumnos.upm.es) Dec 2023
_________________________________________________________________________________________________________________

"""

# This function performs one step of the RK method for the specified order
def RK_stages(order, U1, t, dt, F):
    
    orders, Ns, a, b, bs, c = butcher()
    
    Nk = len(U1)
    # k are the intermediate values based on the butcher array coefficients
    k = zeros([Ns, Nk])
    
    k[0,:] = F(U1, t + c[0]*dt)

    if order == 1:
        for i in range(1,Ns):
            
            Up = U1
            
            for j in range(i):
                
                Up = Up + dt * a[i,j] * k[j,:]
                
            k[i,:] = F(Up, t + c[i]*dt)
            
        # Final solution
        U2 = U1 + dt*matmul(b,k)

    elif order == 2:
        for i in range(1,Ns):
            
            Up = U1
            
            for j in range(i):
                
                Up = Up + dt * a[i,j] * k[j,:]
                
            k[i,:] = F(Up, t + c[i]*dt)
            
        U2 = U1 + dt*matmul(bs,k)

    return U2

# This function computes the adaptive step size based on the error between two solutions (dU),
# a specified tolerance (tol), the current time step (dt), and the orders of accuracy.
def StepSize(dU, tol, dt, orders): 
    error = norm(dU)

    if error > tol:
        step_size = dt*(tol/error)**(1/(orders+1))
    else:
        step_size = dt

    return step_size

# This funnction defines the butcher array coefficients for the embedded RK method
def butcher():
    # ... other code

    orders = [2, 1]     # List of orders, in this case the order of accuracy for the primary stage of the
                        # Runge-Kutta method is 2 and 1 represents the order of accuracy for the embedded 
                        # stage, used to estimate the error and adapt the step size
    Ns = 2

    a = zeros([Ns, Ns-1])
    b = zeros([Ns])
    bs = zeros([Ns])
    c = zeros([Ns])

    c = [0., 1.]
    a[0, :] = [0.]
    a[1, :] = [1.]
    b[:] = [1./2, 1./2]
    bs[:] = [1., 0.]

    return orders, Ns, a, b, bs, c
