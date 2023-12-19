######################################### MILESTONE 5 ####################################################
## N body problem ##

from ODEs.Cauchy_Problem import Integrate_Cauchy
from ODEs.Time_Schemes import Euler, EI, RK4, CN, LF, choose_integration_method
from ODEs.Stability_Regions import Stability_regions
from Physics.Kepler import F_Kepler
from Physics.Oscillator import Oscillator
from Errors import Richardson_Cauchy_Problem, Temporal_Convergence_Rate
from numpy import array, zeros, log10, ones, vstack, linspace, transpose 
from numpy.linalg import norm, lstsq
import matplotlib.pyplot as plt