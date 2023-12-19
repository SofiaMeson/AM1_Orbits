######################################### ESTIMATING ERROS AND CONVERGENCE RATE ###############################################################################

## This module includes two functions to calculate the error of the Cauchy problem programmed in the milestone 2 and the convergence rate of the solution ##


from ODEs.Cauchy_Problem import Integrate_Cauchy
from ODEs.Time_Schemes import Euler, EI, RK4, CN
#from Physics.Kepler import Kepler
from numpy import array, zeros, log10, ones, vstack, linspace 
from numpy.linalg import norm, lstsq
import matplotlib.pyplot as plt

 
# This function evaluates errors of numerical integration by mmeans of Richardson extrapolation, based on the Cauchy problem solution implemented in milestone 2.

def Richardson_Cauchy_Problem(t, F, scheme, order, U_0 ):  
   
# Means of Richardson extrapolation (using two grids, one being the double of the other one):
          
       N = len(t) - 1                       # number of columns
       Nv = len(U_0)                      # number of rows 
       cauchy_error = zeros((N + 1, Nv))      # array for Cauchy's error
       
       t1 = t                             # time domain where the Cauchy problem will be calculated. This is the first grid.        
       t2 = zeros(2*N+1)                  # time domain (lenght t2 = 2*t1) to evaluate the numerical integration's error. This is the second grid.
       
       
       
       # As t2's lenght is the double of t1, its components can be defined with the following loop:
       
       for i in range (N):  
           t2[2*i] = t1[i] 
           t2[2*i+1] = (t1[i] + t1[i+1])/2
       t2[2*N] = t1[N]
      
       # Solve the Cauchy problem for the two time domains (t2 doubles t1):
       
       U1 = Integrate_Cauchy(F, U_0, t1, scheme) 
       U2 = Integrate_Cauchy(F, U_0, t2, scheme)  

  
       
       
      # Evaluate the error between the two solutions and create an array to correct U1, the solution obtained for the desired time domain
       for i in range (N+1):  
            cauchy_error[i,:] = (U2[2*i, :]- U1[i, :])/(1 - 1./(2**order)) 
        
      # Correct the solution by applying the error evaluation:
       sol_cauchy = U1 + cauchy_error 
       
       return cauchy_error, sol_cauchy 
             
       
# This function evaluates de convergence rate of different temporal schemes for numerical integration of, in this case, the Cauchy problem.

def Temporal_Convergence_Rate( t, F, U_0, scheme, m): 
     
      log_E = zeros(m)  #log of the mathematical errors
      log_N = zeros(m)  #log with the lenght of the time domain
      
      # Solving the Cauchy problem with the desired scheme
      
      N = len(t)-1
      t1 = t
      U1 = Integrate_Cauchy(F, U_0, t1, scheme) 
     

      for i in range(m): 
         # Similarly to the function to evalute the error, the Cauchy problem is solved for a different time domain, with lenght(t2)= 2*lenght(t1). 
         # This means that the convergence rate is calculated by using two grids. 
         N =  2*N                                              # New "N"
         t2 = array( zeros(N+1) )                              # New time domain
         t2[0:N+1:2] = t1                                      # t2's components are defined using this loop, similarly to the Cauchy error function
         t2[1:N:2] = (t1[1:int(N/2)+1] + t1[0:int(N/2)]) / 2   
         
         # The Cauchy problem is solved for t2 to later evaluate the convergence rate between the two solutions
         U2 = Integrate_Cauchy(F, U_0, t2, scheme)           
        
        # The difference between the two solutions is calculated and normalized
         error = norm(U2[N, :] - U1[int(N/2), :]) 
         
        # The errors are allocated in the logs defined previously to evaluate the convergence rate
         log_E[i] = log10(error)
         log_N[i] = log10(N)
         
         t1 = t2
         U1 = U2 

     # Find and save the iterations where the error was significant
     
      for j in range(m): 
         if abs(log_E[j]) > 12 :  
            break 
      j = min(j, m-1) 
      x = log_N[0:j+1]
      y = log_E[0:j+1]
      
      # Stablish the parameters to calculate the regresion
      
      A = vstack([x, ones(len(x))]).T
      m, c = lstsq(A, y, rcond=None)[0]      # Find the coefficients of the best fit line (or hyperplane) that minimizes the sum of the squares of the residuals
      order = abs(m)                         # Slope. This is the convergence rate
      
      # Correcting the erros based in the convergence rate calculated (order)
      log_E = log_E - log10( 1 - 1./2**order) 

      return order, log_E, log_N


