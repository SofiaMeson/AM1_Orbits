###############################SOLVING KEPLER ORBITS######################################################
import numpy as np
from scipy.optimize import newton

#Euler method
def Euler (F, U, dt) :
    return U + dt * F (U)


#Runge-Kutta 4 method
def RK4 (F, U, dt) :
       k1 = F (U)
       k2 = F (U + k1 * dt/2)
       k3 = F (U + k2 * dt/2)
       k4 = F (U + k3 * dt)
       return U + dt/6 * (k1 + 2 * k2 + 2 * k3 + k4)   

#Crank-Nicolson method
def CN (F, U, dt) :
      def CN_prev (x) :
          return x - U - dt/2 * (F (U) + F (x))  
      return newton (CN_prev, U)

#Inverse_Euler method
def EI (F, U, dt) :
    def EI_prev (x) :
         return x - U - dt * F (x)
    return newton (EI_prev, U)
     