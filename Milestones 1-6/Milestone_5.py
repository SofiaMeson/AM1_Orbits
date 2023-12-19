######################################### MILESTONE 5 ####################################################
## N body problem ##

from ODEs.Cauchy_Problem import Integrate_Cauchy
from ODEs.Time_Schemes import RK4
from Physics.Nbody_functions import F_NBody
from numpy import array, zeros, reshape, shape, linspace, concatenate, split, ceil, sqrt 
from numpy.linalg import norm, lstsq
from scipy.integrate import odeint, ode, solve_ivp
import matplotlib.pyplot as plt

N = 1000    # Time steps
Nb = 4      # Number of bodies
Nc = 3      # Number of coordinates

Nt = (N+1)*2*Nc*Nb

t0 = 0
tf = 10
t = linspace(t0, tf, N + 1)

def F(U, t):
   return F_NBody(U, t, Nb, Nc)

#Initial conditions
U_0 = zeros(2*Nc*Nb)
U1 = reshape(U_0, (Nb, Nc, 2))
r0 = reshape(U1[:, :, 0], (Nb, Nc))
v0 = reshape(U1[:, :, 1], (Nb, Nc))

# Define initial conditions. These were takem for example, but the
# user can set them via the commented code
# Body 1
r0[0, :] = [1, 0, 0]       
v0[0, :] = [0, 0.4, 0]     

# Body 2
r0[1, :] = [-1, 0, 0]      
v0[1, :] = [0, -0.4, 0]    

# Body 3
r0[2, :] = [0, 1, 0]       
v0[2, :] = [-0.4, 0., 0.]   

# Body 4
r0[3, :] = [0, -1, 0]       
v0[3, :] = [0.4, 0., 0.]    

# # Get the number of bodies from the user
# Nb = int(input("Enter the number of bodies: "))


# # Initialize arrays for positions (r0) and velocities (v0)
# r0 = zeros((Nb, 3))
# v0 = zeros((Nb, 3))

# # Loop to input initial positions and velocities for each body
# for i in range(Nb):
#     # Body index starts from 1
#     body_number = i + 1
    
#     # Get user input for initial position of the body
#     r0[i, :] = [float(coord) for coord in input(f"Enter initial position (x, y, z) for body {body_number}: ").split()]

#     # Get user input for initial velocity of the body
#     v0[i, :] = [float(vel) for vel in input(f"Enter initial velocity (vx, vy, vz) for body {body_number}: ").split()]

# # Print the resulting arrays
# print("Initial positions (r0):")
# print(r0)

# print("Initial velocities (v0):")
# print(v0)


U = Integrate_Cauchy(F, U_0, t, RK4)

Us = reshape(U, (N + 1, Nb, Nc, 2))              # Vector de estado de solución
r = reshape(Us[:, :, :, 0], (N + 1, Nb, Nc))     # Each of the body's final positions


# # Plotted solution
# for i in range(Nb):
#     plt.plot(r[:, i, 0], r[:, i, 1]) 
# plt.axis('equal')
# plt.grid()

# plt.show()


#Graph 3D
fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')
col = ["blue","red","green","purple","yellow","orange","black"]
for i in range(Nb):
    ax1.plot_wireframe(r[:,i,0].reshape((-1, 1)), r[:,i,1].reshape((-1, 1)), r[:,i,2].reshape((-1, 1)), color = col[i])
plt.title("N-body problem, XYZ")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")
plt.grid()
plt.show()

#Graph 2D
for i in range(Nb):
   plt.plot(r[:, i, 0], r[:, i, 1], color = col[i])
plt.axis('equal')
plt.title("N-body problem, XY plane")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()



