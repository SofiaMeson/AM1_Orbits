################################## MILESTONE 2 ####################################################

#In this program, the user will be able to compare the different methods to integrate Kepler orbits.

import numpy as np
import matplotlib. pyplot as plt
from Cauchy_Problem import Integrate_Cauchy
from Time_Schemes import Euler, EI, RK4, CN

#Initial conditions are defined
n = 100000
dt = 0.0001
t = np.linspace(0, n*dt, n+1)
U_0 = np.array ( [ 1, 0, 0, 1 ] )

#A function is created to define Kepler force in orbits
def F(U):
    x, y, vx, vy = U[0], U[1], U[2], U[3]
    mr = (x**2 + y**2)**(3/2)

    if mr == 0:
        # To handle the case where mr is zero to avoid division by zero
        return np.array([vx, vy, 0.0, 0.0])
    else:
        return np.array([vx, vy, -x / mr, -y / mr])


sol_Euler = Integrate_Cauchy(F, U_0, t, Euler)
print ("Euler finished.")
sol_inverse_euler = Integrate_Cauchy(F, U_0, t, EI)
print ("Inverse Euler finished.")
sol_cn = Integrate_Cauchy(F, U_0, t, CN)
print ("Crank-Nicolson finished.")
sol_rk4 = Integrate_Cauchy(F, U_0, t, RK4)
print ("Runge-Kutta 4 finished.")



##Curves


#All methods together

plt.figure(5)

plt.plot(sol_Euler[0, :], sol_Euler[1, :], color='blue', label='Orbit Euler Method')
plt.plot(sol_inverse_euler[0, :], sol_inverse_euler[1, :], color='green', label='Orbit Inverse Euler Method')
plt.plot(sol_cn[0, :], sol_cn[1, :], color='yellow', label='Orbit Crank-Nicolson Method')
plt.plot(sol_rk4[0, :], sol_rk4[1, :], color='red', label='Orbit Runge-Kutta 4 Method')

plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Orbit with different methods.')
plt.legend()
plt.grid()


# #Euler method

# plt.figure(1)

# plt.plot(sol_Euler[0, :], sol_Euler[1,:])
# plt.axis('equal')
# plt.xlabel('x')
# plt.ylabel('y')     
# plt.title('Orbit Euler Method.')  
# plt.grid()

    
# ##Inverse Euler method
     
# plt.figure(2)

# plt.plot(sol_inverse_euler[0, :], sol_inverse_euler[1,:])
# plt.axis('equal')
# plt.xlabel('x')
# plt.ylabel('y')     
# plt.title('Orbit Inverse Euler Method.')  
# plt.grid()    


# #Crank Nicholson method

# plt.figure(3)

# plt.plot(sol_cn[0, :], sol_cn[1,:])
# plt.axis('equal')
# plt.xlabel('x')
# plt.ylabel('y')     
# plt.title('Orbit Crank-Nicolson Method.')  
# plt.grid()


# #Runge-Kutta 4 Method

# plt.figure(4)

# plt.plot(sol_rk4[0, :], sol_rk4[1,:])
# plt.axis('equal')
# plt.xlabel('x')
# plt.ylabel('y')     
# plt.title('Orbit Runge-Kutta 4 Method.')  
# plt.grid()


plt.show()

      
