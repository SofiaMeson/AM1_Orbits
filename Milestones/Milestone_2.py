######################################### MILESTONE 2 ####################################################
## Prototypes to integrate orbits with functions##

#In this program, the user will be able to compare the different methods to integrate Kepler orbits.

from numpy import linspace, array 
import matplotlib.pyplot as plt
from ODEs.Cauchy_Problem import Integrate_Cauchy
from ODEs.Time_Schemes import Euler, EI, RK4, CN


### Definition of the initial conditions ###

# They can be given manually (using the parameters defined below)
# n = 100000
# dt = 0.0001
# t = np.linspace(0, n*dt, n+1)
# U_0 = np.array ( [ 1, 0, 0, 1 ] )

# The user can also write them in the terminal:

user_n = input("Number of iterations (n) (note that it has to be an integer): ")
user_dt = input("Time interval (dt) (note that it needs to be 0.1, 0.01, 0.001... in order to be correct): ")
user_U_0= input("Enter the initial conditions for U_0 (x, y, vx, vy), separated by commas (e.g.: 1, 2, 3, 4): ")

n = int(user_n) 
dt = float(user_dt)
t = linspace(0, n*dt, n+1)
U_0 = array([float(x.strip()) for x in user_U_0.split(',')])

# Check if the user entered U_0 correctly
if U_0.size == 4:
    # Print the resulting vector
    print("The initial conditions array U_0 is:", U_0)
else:
    print("U_0 is not defined correctly (it needs to have 4 components).")



### Integrating Kepler orbits with different time schemes ###

# A function is created to define Kepler force in orbits
def F(U):
    x, y, vx, vy = U[0], U[1], U[2], U[3]
    mr = (x**2 + y**2)**(3/2)

    if mr == 0:
        # To handle the case where mr is zero to avoid division by zero
        return array([vx, vy, 0.0, 0.0])
    else:
        return array([vx, vy, -x / mr, -y / mr])


# The orbit is integrated using the Cauchy problem for different time schemes:

sol_Euler = Integrate_Cauchy(F, U_0, t, Euler)
print ("Euler finished.")

sol_inverse_euler = Integrate_Cauchy(F, U_0, t, EI)
print ("Inverse Euler finished.")

sol_cn = Integrate_Cauchy(F, U_0, t, CN)
print ("Crank-Nicolson finished.")

sol_rk4 = Integrate_Cauchy(F, U_0, t, RK4)
print ("Runge-Kutta 4 finished.")



### The results for the different time schemes are compared: ###


# All methods together

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


# Euler method

plt.figure(1)

plt.plot(sol_Euler[0, :], sol_Euler[1,:])
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')     
plt.title('Orbit Euler Method.')  
plt.grid()

    
# Inverse Euler method
     
plt.figure(2)

plt.plot(sol_inverse_euler[0, :], sol_inverse_euler[1,:])
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')     
plt.title('Orbit Inverse Euler Method.')  
plt.grid()    


# Crank Nicholson method

plt.figure(3)

plt.plot(sol_cn[0, :], sol_cn[1,:])
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')     
plt.title('Orbit Crank-Nicolson Method.')  
plt.grid()


# Runge-Kutta 4 method

plt.figure(4)

plt.plot(sol_rk4[0, :], sol_rk4[1,:])
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')     
plt.title('Orbit Runge-Kutta 4 Method.')  
plt.grid()


plt.show()

      
