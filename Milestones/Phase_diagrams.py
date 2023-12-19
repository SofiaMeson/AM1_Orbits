import numpy as np
from ODEs.Time_Schemes import RK4
from ODEs.Cauchy_Problem import Integrate_Cauchy
import matplotlib.pyplot as plt

#Initial conditions are defined
# n = 20
# dt = 0.1
# U_0 = np.array ([4, -5])


user_n = input("Number of iterations (n) (note that it has to be an integer): ")
user_dt = input("Time interval (dt) (note that it needs to be 0.1, 0.01, 0.001... in order to be correct): ")
user_U_0= input("Initial conditions for U_0 (please note that U_0 is an array so they shall be given as, for example: 4, -5): ")

U_0 = np.fromstring(user_U_0, dtype=int, sep=',')
n = int(user_n) 
dt = float(user_dt)
t = np.linspace(0, n*dt, n+1)



def F_silla (U, t=0) :
    vx = 3 * U[0] - 2 * U[1]
    vy = 2 * U[0] - 2 * U[1]
    return np.array ([vx, vy])


U = Integrate_Cauchy(F_silla, U_0, t, RK4)


plt.plot(U[0,:], U [1,:])

plt.show()







