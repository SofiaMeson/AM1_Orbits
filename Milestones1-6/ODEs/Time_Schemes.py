##########################################TIME SCHEMES######################################################

from scipy.optimize import newton
from numpy import zeros, matmul, size, linspace
from numpy.linalg import norm
from Physics.ERK_functions import butcher, StepSize, RK_stages

"""
___________________________________________________________________________________________________________
Definition of the temporal schemes used to integrate the Cauchy problem

# Euler, Runge-Kutta oder 4 (RK4), Crank-Nicolson (CN), Inverse Euler (EI), Leap-Frog (LF), 
  Embedded Runge-Kutta
       
    Inputs: 
            - F : represents the  differential operator. Imported from Kepler.py, Nbody_functions.py, 
                  Oscillator.py or, in the case of the circular restricted 3 body problem, it uses
                  the F defined in Milestone_6.py
            - U : state vector at a specific time point
            - dt: time step, determining the size of the time intervals between iterations
            - t : array representing the time points at which the solution is computed
            
    return: 
            The updated state vector at the next time step, computed using the selected numerical 
            method
            
# Choose integration method: this function is defined to optimize the code and allow the user to use the 
  temporal schemes without writing inside of the code itself
       
    Inputs: 
           - All temporal schemes: Euler, Runge-Kutta oder 4 (RK4), Crank-Nicolson (CN), Inverse Euler (EI), 
             Leap-Frog (LF) and Embedded Runge-Kutta
            
    return: 
            The selected temporal method
          
Author: Sofía Mesón Pérez (sofia.meson.perez@alumnos.upm.es) Dec 2023
___________________________________________________________________________________________________________

"""

# Euler method
def Euler(F, U, dt, t):
    return U + dt * F(U, t)


#Runge-Kutta 4 method
def RK4 (F, U, dt, t) :
       k1 = F (U, t)
       k2 = F (U + k1 * dt/2, t + dt/2)
       k3 = F (U + k2 * dt/2, t + dt/2)
       k4 = F (U + k3 * dt, t + dt)
       return U + dt/6 * (k1 + 2 * k2 + 2 * k3 + k4)   

#Crank-Nicolson method
def CN (F, U, dt, t) :
      def Residual_CN (X) :
          return X - a - dt/2 * F(X, dt + t)  
      a = U + dt/2 * F(U, t)
      return newton (Residual_CN, U)

#Inverse Euler method
def EI (F, U, dt, t) :
    def Residual_IE (X) :
         return X - U - dt * F (X, dt + t)
    return newton (Residual_IE, U)
     
     
# Leap-Frog

def LF(F, U, dt, t):
    U_mediopaso = U + 0.5 * dt * F(U, t)
    return U + dt * F(U_mediopaso, t)


# Embedded Runge-Kutta (order 3)

def ERK(F, U, dt, t):

    tol = 1e-9
    
    # Calculates Runge-Kutta of order 1 and order 2 
    stage1 = RK_stages(1, U, t, dt, F)  
    stage2 = RK_stages(2, U, t, dt, F) 
    
    # Define the butcher array
    orders, Ns, a, b, bs, c = butcher()
    
    # Determine the minimum step size between dt and the stepsize, which compares the error with the tolerance
    h = min(dt, StepSize(stage1 - stage2, tol, dt,  min(orders)))
    N_n = int(dt/h) + 1        # Number of steps to update solution U2
    n_dt = dt / int(N_n)           
    stage1 = U
    stage2 = U

    for i in range(N_n):
        time = t + i * n_dt
        stage1 = stage2
        stage2 = RK_stages(1, stage1, time, n_dt, F)
        
    # Final solution
    U2 = stage2
    
    ierr = 0

    return U2





def choose_integration_method():
    print("Choose an integration method:")
    print("1. Euler")
    print("2. Inverse Euler")
    print("3. Runge-Kutta 4")
    print("4. Crank-Nicolson")
    print("5. Leap-Frog")
    print("6. Embedded Runge-Kutta")   

    choice = input("Enter the number corresponding to the desired method: ")
    
    if choice == '1':
        return Euler
    elif choice == '2':
        return EI
    elif choice == '3':
        return RK4
    elif choice == '4':
        return CN
    elif choice == '5':
        return LF
    elif choice == '6':
        return ERK
    else:
        print("Invalid choice. Using default method (Euler).")
        return Euler   

