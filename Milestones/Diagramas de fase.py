import numpy as np
from Time_Schemes import RK4
from Cauchy_Problem import Integrate_Cauchy
import matplotlib.pyplot as plt

#Initial conditions are defined
n = 20
dt = 0.1
t = np.linspace(0, n*dt, n+1)

print ("Dame un valor inicial: ")
U_0 = np.array ([4, -5])

def F_silla (U, t=0) :
    vx = 3 * U[0] - 2 * U[1]
    vy = 2 * U[0] - 2 * U[1]
    return np.array ([vx, vy])


U = Integrate_Cauchy(F_silla, U_0, t, RK4)


plt.plot(U[0,:], U [1,:])

plt.show()







