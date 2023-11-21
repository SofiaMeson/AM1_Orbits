
from numpy import array, zeros, linspace
import matplotlib.pyplot as plt
from scipy.optimize import fsolve, newton
from mpl_toolkits.mplot3d import axes3d
import math as math

################################ Dynamic Systems Integration ####################################

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
   

######################################### Temporal Schemes #########################################

def Euler(F,U,t0, tf):
    dt = tf-t0
    return U + dt * F(U,t0)
    
def Crank_Nicolson(F,i, t0, tf):
    dt = tf-t0
    def g(x):
        return x - a -dt/2 * (F(a,t0) + F(x,t0))
    a = U[:,i]
    
    return newton(g, U)

def RK4(F,U,t0, tf ):
    dt = tf-t0
    k1 = F( U, t0 )
    k2 = F( U +k1*dt/2, t0 + dt/2 )
    k3 = F( U +k2*dt/2, t0 + dt/2 )
    k4 = F( U + k3*dt, t0 + dt )
     
    k = 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    
    return U + dt * k

def Inverse_Euler(F,i, t0, tf):
    dt = tf-t0
    def g(x):
        return x - a - dt * F(x,t) 
    a = U[:,i]
    
    return newton(g, U[:,i])

######################################### Cauchy Problem #########################################

def Integrate_ODE(U, F, t, scheme):

    for i in range(0, N-1):
        U[:,i+1] = scheme(F,U[:,i],t[i],t[i+1])
        
    return U

####################### Establishing boundaries and initial conditions ###########################

## Boundaries
N = 10000
d_t = 0.01                        
t = linspace(0,N*d_t, N+1)


## Keplerian Orbit initial conditions
U = array(zeros((3,len(t)-1)))
U[:,0] = array( [-1, 1, 1] )

U2 = array(zeros((3,len(t)-1)))
U2[:,0] = array( [0, 0, 0] )

################################## Solving the dynamic system #####################################

## Solving the dynamic system, for the initial conditions
U = Integrate_ODE(U, Rossler, t, RK4)
U2 = Integrate_ODE(U2, Rossler2, t, RK4)


## Ploting the results
f1 = plt.figure()
plt.subplot (111, projection = '3d')
plt.plot(U[0,:],U[1,:], U[2,:])

f2 = plt.figure()
plt.plot (t[5000:N], U[0,5000:N], color = 'red')
f3 = plt.figure()
plt.plot(t[5000:N], U[1,5000:N], color = 'yellow')
f4 = plt.figure()
plt.plot(t[5000:N], U[2,5000:N], color = 'green')

f5 = plt.figure()
plt.subplot (111, projection = '3d')
plt.plot(U2[0,:],U2[1,:], U2[2,:])

f6 = plt.figure()
plt.plot (t[5000:N], U2[0,5000:N], color = 'red')
f7 = plt.figure()
plt.plot(t[5000:N], U2[1,5000:N], color = 'yellow')
f8 = plt.figure()
plt.plot(t[5000:N], U2[2,5000:N], color = 'green')

plt.show()

