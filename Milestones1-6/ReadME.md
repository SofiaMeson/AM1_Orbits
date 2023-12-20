# Milestones 1-6 Files
Author: Sofía Mesón Pérez

---

This repository contains all the Python programs that I have developed for the  *Milestones 2* to *6*, (as the *Milestone 1* is the same as the *Milestone 2* but without implementing fuctions, making it suboptimal.

---
## FILE STRUCTURE

This repository is divided into different files. All the Python programs have a small explanation inside of them, with their inputs and outputs. The code is also commented so that the user can understand it seamlessly. The **Milestones 1-6** file's structure is:

1. **Milestone_Software_Design**: this file contains all the schemes for *Milestones 2* to *6*.
   
2. **ODEs**: this file contains the programs:
   - [*Cauchy_Problem.py*](Milestones1-6/ODEs/Cauchy_Problem.py): it contains the function that integrates the Cauchy problem, which can be achieved using different temporal schemes.
   - [*Stability_Regions.py*](Milestones1-6/ODEs/Stability_Regions.py): it contains a function that calculates the stability regions for different temporal schemes, as well as a function to plot them.
   - [*Time_Schemes.py*](Milestones1-6/ODEs/Time_Schemes.py): it contains the functions that define the temporal schemes used to integrate the Cauchy problem.

3. **Physics**: this file contains the programs:
   - [*CR3BP.py*](Milestones1-6/Physics/CR3BProblem.py): it contains the function that defines the circular restriced 3-body problem
   - [*Dynamic_Systems.py*](Milestones1-6/Physics/Dynamic_systems.py): it contains a function that defines different dynamic systems.
   - [*ERK_functions.py*](Milestones1-6/Physics/ERK_functions.py): it contains the functions that are used to define the embedded Runge-Kutta temporal scheme.
   - [*Kepler.py*](Milestones1-6/Physics/Kepler.py): it contains the function that represents differential operator in a Kepler orbit.
   - [*Lagrange_Points*](Milestones1-6/Physics/Lagrange_Points.py): it contains the functions that calculate Lagrange points and their stability.
   - [*Nbody_functions.py*](Milestones1-6/Physics/Nbody_functions.py): it contains the function that characterizes the N body problem with pointers.
   - [*Oscillator.py*](Milestones1-6/Physics/Oscillator.py): it contains the function that represents the  differential operator of the harmonic oscillator system.

4. **Systems_of_equations**: this file contains the programs (these programs were developed by Juan A. Hernández):
   - [*Linear_eq.py*](Milestones1-6/Systems_of_equations/Linear_eq.py): it contains the function for solving linear equations using Gauss
   - [*Newton.py*](Milestones1-6/Systems_of_equations/Newton.py): it contains the functions for the Newton solver and the Jacobian.
     
5. [**Errors.py**](Milestones1-6/Errors.py): this module defines two functions to calculate the error of the Cauchy problem programmed in the *Milestone 2* and the convergence rate of the obtained solution.

6. **Milestones 2-6**: Detailed explanations for each milestone are provided in the following section, along with a schematic representation of the functions they utilize.

## MILESTONES EXPLANATION


 


<p align="center">
  <img src="Milestone_Software_Design/Milestone_2_SD.jpg" alt="Descripción de la imagen">
</p>
