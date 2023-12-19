######################################### ERK FUNCTIONS ####################################################
## Functions that the embedded Runge-Kutta time scheme uses ##


from scipy.optimize import newton
from numpy import zeros, matmul, size, linspace
from numpy.linalg import norm

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

    orders = [2, 1]
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
