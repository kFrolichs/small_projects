# Book
# Mitchell, M. (2009). Complexity: A guided tour. Oxford University Press.

# Paper
# Mitchell, M., Crutchfield, J. P., & Das, R. (1996).
# Evolving cellular automata with genetic algorithms:
# A review of recent work. In Proceedings of the First international
# conference on evolutionary computation and its applications (EvCA’96)

# Use genetic algorithms to evolve one-dimensional cellular automata to
# perform a task
# The task in this case being: Majority Classification

# A lot of code reused from /cellular_automata.py

# Some code to test out 1 dimensional cellular automata
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# General settings
n = 149 # lattice size
m = 2*n # Maximum timesteps
# Choose 100 uniformly distributed initial configurations
