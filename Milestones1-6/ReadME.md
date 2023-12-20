# Milestones 1-6 Files
Author: Sofía Mesón Pérez

---

This repository contains all the Python programs that I have developed for the  *Milestones 2* to *6*, (as the *Milestone 1* is the same as the *Milestone 2* but without implementing fuctions, making it suboptimal.

---
## FILE STRUCTURE

This repository is divided into different files. All the Python programs have a small explanation inside of them, with their inputs and outputs. The code is also commented so that the user can understand it seamlessly. The **Milestones 1-6** file's structure is:

1. **Milestone_Software_Design**: this file contains all the schemes for *Milestones 2* to *6*.
   
2. **ODEs**: this file contains the programs:
   - [*Cauchy_Problem.py*](ODEs/Cauchy_Problem.py): it contains the function that integrates the Cauchy problem, which can be achieved using different temporal schemes.
   - [*Stability_Regions.py*](ODEs/Stability_Regions.py): it contains a function that calculates the stability regions for different temporal schemes, as well as a function to plot them.
   - [*Time_Schemes.py*](ODEs/Time_Schemes.py): it contains the functions that define the temporal schemes used to integrate the Cauchy problem.

3. **Physics**: this file contains the programs:
   - [*CR3BP.py*](Physics/CR3BProblem.py): it contains the function that defines the circular restriced 3-body problem
   - [*Dynamic_Systems.py*](Physics/Dynamic_systems.py): it contains a function that defines different dynamic systems.
   - [*ERK_functions.py*](Physics/ERK_functions.py): it contains the functions that are used to define the embedded Runge-Kutta temporal scheme.
   - [*Kepler.py*](Physics/Kepler.py): it contains the function that represents differential operator in a Kepler orbit.
   - [*Lagrange_Points*](Physics/Lagrange_Points.py): it contains the functions that calculate Lagrange points and their stability.
   - [*Nbody_functions.py*](Physics/Nbody_functions.py): it contains the function that characterizes the N body problem with pointers.
   - [*Oscillator.py*](Physics/Oscillator.py): it contains the function that represents the  differential operator of the harmonic oscillator system.

4. **Systems_of_equations**: this file contains the programs (these programs were developed by Juan A. Hernández):
   - [*Linear_eq.py*](Systems_of_equations/Linear_eq.py): it contains the function for solving linear equations using Gauss
   - [*Newton.py*](Systems_of_equations/Newton.py): it contains the functions for the Newton solver and the Jacobian.
     
5. [**Errors.py**](Errors.py): this module defines two functions to calculate the error of the Cauchy problem programmed in the *Milestone 2* and the convergence rate of the obtained solution.

6. **Milestones 2-6**: Detailed explanations for each milestone are provided in the following section, along with a schematic representation of the functions they utilize.

## MILESTONES EXPLANATION

- [**Milestone 2**](Milestone_2.py):
 <p align="center">
  <img src="Milestone_Software_Design/Milestone_2_SD.jpg" alt="Milestone 2 software scheme">
</p>

- [**Milestone 3**](Milestone_3.py):
 <p align="center">
  <img src="Milestone_Software_Design/Milestone_3_SD.jpg" alt="Milestone 3 software scheme">
</p>

- [**Milestone 4**](Milestone_4.py):
 <p align="center">
  <img src="Milestone_Software_Design/Milestone_4_SD.jpg" alt="Milestone 4 software scheme">
</p>

- [**Milestone 5**](Milestone_5.py):
 <p align="center">
  <img src="Milestone_Software_Design/Milestone_5_SD.jpg" alt="Milestone 5 software scheme">
</p>

- [**Milestone 6**](Milestone_6.py):
 <p align="center">
  <img src="Milestone_Software_Design/Milestone_6_SD.jpg" alt="Milestone 6 software scheme">
</p>





