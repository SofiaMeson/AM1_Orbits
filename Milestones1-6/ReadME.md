# Milestones 1-6
Course: Ampliación de Matemáticas 1

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
   - [*Oscillator.py*](Physics/Oscillator.py): it contains the function that represents the  differential operator of the harmonic oscillator system. It also contains a function that defines the oscillator system's matrix.

4. **Systems_of_equations**: this file contains the programs (these programs were developed by Juan A. Hernández):
   - [*Linear_eq.py*](Systems_of_equations/Linear_eq.py): it contains the function for solving linear equations using Gauss.
   - [*Newton.py*](Systems_of_equations/Newton.py): it contains the functions for the Newton solver and the Jacobian.
     
5. [**Errors.py**](Errors.py): this module defines two functions to calculate the error of the Cauchy problem programmed in the *Milestone 2* and the convergence rate of the obtained solution.

6. **Milestones 2-6**: Detailed explanations for each milestone are provided in the following section, along with a schematic representation of the functions they utilize.

## MILESTONES EXPLANATION

- [**Milestone 2**](Milestone_2.py): "_Prototypes to integrate orbits with functions_"
  
  In this program, the Cauchy problem is integraed using different time schemes. By only changing the time steps, it becomes clear that the Euler and inverse Euler temporal schemes require smaller dt (approximately of 0.001) to close the orbit and correctly integrate it.
  
  Runge-Kutta and Crank-Nicolson solve the orbit correctly, providing a close and precise orbit for each of the dt provided. Smaller dt imply more precision, but with bigger dt they provide a good integration.
  
 <p align="center">
  <img src="Milestone_Software_Design/Milestone_2_SD.jpg" alt="Milestone 2 software scheme">
</p>

- [**Milestone 3**](Milestone_3.py): "_Error estimation of numerical solutions_"

   By utilizing two grids it is possible to estimate the error of the integration of the Cauchy problems for different time schemes. Observing the results, it becomes clear that both Euler and inverse Euler have a first-order truncation error, Crank-Nicolson has a second-order truncation error and Runge-Kutta Order 4 a four-order truncation error. The same occurs with the convergence rate.

   A higher convergence rate means that the temporal scheme can achieve a more accurate solution with a coarser grid or larger time step compared to methods with lower convergence rates.

  Crank-Nicolson and Runge-Kutta order 4 methods se discretization, which may introduce errors if the time step is not small enough.

  Future work for this program would be to try the estimation of the error and the convergence rate for other grids and see if it changes for the better.

   It is recommended that the user utilizes the same number of steps and step size than the ones used in the *Milestone 2* to have a more accurate perception of how the temporal schemes evolve.
 <p align="center">
  <img src="Milestone_Software_Design/Milestone_3_SD.jpg" alt="Milestone 3 software scheme">
</p>

- [**Milestone 4**](Milestone_4.py): "*Linear problems. Regions of absolute stability*"

   The results are plotted for the initial conditions that provide clear plots for the stability regions.

   When observing the results, it becomes clear that:
  
   - _Euler_: the Euler scheme's absolute stability region is a circumference with the center at (-1, 0) and with r=1. The eigenvalues fall on the imaginary axis, outside of the absolute stability region, so the Euler temporal scheme is not stable.

   - _Inverse Euler_: the eigenvalues are inside of the absolute stability region, specifically in the yellow circumference in the plot (with center (1, 0) and r=1). The numeric solution is stable, as well as the system.

   - _Crank-Nicolson_: the absolute stability region is the negative real half-plane, which makes the system stable. The eigenvalues fall on the imaginary axis.

   - _Runge-Kutta order 4_: the absolute stability region is quite peculiar, as some of its stability regions are contained in the positive real half-plane. The solutions fall on the contour of the stability region, in the imaginary plane.


 <p align="center">
  <img src="Milestone_Software_Design/Milestone_4_SD.jpg" alt="Milestone 4 software scheme">
</p>

- [**Milestone 5**](Milestone_5.py): "*N body problem*"

   The initial conditions given for the N-body problem define a system composed by four bodies, each with distinct positions and velocities. The number of coordinates for each one is 3 ([x, y, z]). The arrangement consists of two particles along the x-axis and two along the y-axis, forming a symmetrical configuration.

   Under the influence of gravitational forces, the simulation of this N-body system reveals a stable and periodic motion. The particles follow elliptical orbits, and collectively, these orbits create a circular pattern at the system's center. This configuration indicates a dynamic equilibrium, where gravitational interactions lead to a sustained, harmonious motion.
  
 <p align="center">
  <img src="Milestone_Software_Design/Milestone_5_SD.jpg" alt="Milestone 5 software scheme">
</p>

- [**Milestone 6**](Milestone_6.py): "*Lagrange points and their stability*"

  Initial conditions are given, but they can be changed. 5 Lagrange points will be calculated, but this can also be changed. When observing the results, it becomes clear that:
  
   - _LP1_: the obtained eigenvalues are: [ 2.93206148 -2.93206148  0.  0. ]. The presence of both positive and negative real parts indicates that the Lagrange point has mixed stability. The Lagrange point is likely to be a saddle point, meaning it has directions of stability and instability. Objects near this Lagrange point may experience perturbations that can lead to either stable or unstable behavior depending on the direction of the perturbation. This is confirmed by observing the orbit for this Lagrange point, as it showcases a mix between stable and inestable behaviour.

   - _LP2_: the obtained eigenvalues are: [ 3.4e-07  3.4e-07 -3.4e-07 -3.4e-07 ]. The real parts of the eigenvalues are close to zero but not strictly negative. This suggests that the Lagrange point is on the boundary between stability and instability. Small perturbations may cause the system to exhibit oscillatory behavior, but the perturbations are not large enough to drive the system away from the Lagrange point over time. Observing the plotted orbit, it showcases an open hardly closed eliptical orbit, but with some perturbations that impede to classify it as stable.

   - _LP3_: the obtained eigenvalues are: [ 0. 0. -0.17787832  0.17787832 ]. The real parts are zero and the imaginary parts are non-zero, so the Lagrange point is neutrally stable. Observing the plotted orbit, the oscillatory behavior indicates that small perturbations will cause the system to oscillate around the Lagrange point without diverging over time. 

   - _LP4_: the obtained eigenvalues are: [-3.4e-07 -3.4e-07  3.4e-07  3.4e-07]. The eigenvalues being close to zero suggest a nearly neutrally stable Lagrange point. Similarly to the Lagrange point 2, the plotted orbit showcases an open eliptical orbit, but with some perturbations that impede to classify it as completely stable.
     
   - _LP5_: the obtained eigenvalues are:  [-2.15867061  2.15867061 0. 0.]. The Lagrange point appears to be a neutrally stable equilibrium point with oscillatory behavior. The oscillations indicate that perturbations from this equilibrium will exhibit periodic motion rather than monotonic convergence or divergence. Observing the plotted orbit, this is confirmed

  
 <p align="center">
  <img src="Milestone_Software_Design/Milestone_6_SD.jpg" alt="Milestone 6 software scheme">
</p>





