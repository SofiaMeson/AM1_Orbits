######################################### MILESTONE 6 ####################################################
## Lagrange points and their stability ##

from numpy import array, save, zeros, linspace, shape, reshape, around, random
from ODEs.Cauchy_Problem import Integrate_Cauchy
from Physics.CR3BProblem import CR3BP, F
from Physics.Lagrange_Points import Lagrange_points, Stability_LP
from ODEs.Time_Schemes import Euler, RK4, CN, EI, LF, ERK
from Physics.ERK_functions import butcher, StepSize, RK_stages
import matplotlib.pyplot as plt


# System data
mu = 1.2151e-2 #Earth - Moon
#mu = 3.0039e-7 #Sun - Earth


# Variable initialization
N = int(10000)
t = linspace(0, 10, N)
Np = 5          # Number of Lagrange points



# Initial conditions to calculate Lagrange points (5 Lagrange points, with 4 coordinates)
U_0 = zeros([Np, 4])

U_0[0, :] = [0.1, 0, 0, 0]
U_0[1, :] = [0.8, 0.6, 0, 0]
U_0[2, :] = [-0.1, 0, 0, 0]
U_0[3, :] = [0.8, -0.6, 0, 0]
U_0[4, :] = [1.01, 0, 0, 0]


LP = Lagrange_points(U_0, Np, mu)

# Display of the calculated Lagrange points
print("Calculated Lagrange Points:")
for i, point in enumerate(LP, start=1):
    print(f"LP{i} =", point)

# User selects a Lagrange point
selected_point = input("Enter the number of the Lagrange point you want to select to study its stability: ")

try:
    selected_point_index = int(selected_point)

    # Check if the selected index is valid
    if 1 <= selected_point_index <= len(LP):
        selected_lagrange_point = LP[selected_point_index - 1]
        print(f"You have selected Lagrange Point {selected_point_index}: {selected_lagrange_point}")
    else:
        print("Invalid selection. Please enter a valid Lagrange point number.")
except ValueError:
    print("Invalid input. Please enter a number.")
    
# New initial conditions, using the selected Lagrange point. 
# The first two components are the ones from the Lagrange point, by adding a small random number to change them

U0 = zeros(4)
U0[0:2] = LP[selected_point_index - 1,:]
perturbation = 1e-4*random.random()             
U0 = U0 + perturbation

# As the the circular restricted 3 body problem has more inputs than the Cauchy function,
# this function is created to be able to integrate it
def F(U,t):
   return CR3BP(U, mu)


# Integrate the Cauhy problem using an embedded Runge-Kutta method
U = Integrate_Cauchy(F, U0, t, ERK)

# Study the Lagrange point's stability
U0_stab = zeros(4)
U0_stab[0:2] = LP[selected_point_index - 1, :]
eingvalues = Stability_LP(U0_stab, mu)
#print(around(eingvalues.real, 8))

#  Plot the results

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(U[:, 0], U[:, 1], '-', color="red")
ax1.plot(-mu, 0, 'o', color="purple")
ax1.plot(1 - mu, 0, 'o', color="green")
for i in range(Np):
    ax1.plot(LP[i, 0], LP[i, 1], 'o', color="black")

ax2.plot(U[:, 0], U[:, 1], '-', color="red")

ax2.plot(LP[selected_point_index - 1, 0], LP[selected_point_index - 1, 1], 'o', color="black")
fig.suptitle(f"Orbit around Lagrange Point {selected_point_index}")


ax1.set_title("Orbital view, with the solutions from integrating the Cauchy problem")
ax2.set_title("Lagrange point orbit")

for ax in fig.get_axes():
    ax.set(xlabel='x', ylabel='y')
    ax.grid()

plt.show()





