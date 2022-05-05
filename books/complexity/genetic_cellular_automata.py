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

# General Settings
radius = 7
num_state = 2
lattice_len = 101 # Has to be odd so you always have a majority
timestep = 100
latMat = np.zeros((timestep,lattice_len))

state_options = num_state**radius
# number_rules  = num_state**state_options

# Create a random rule for now
rand_rule = np.random.randint(0,2,state_options)

# Attach the rule to the states
state_rule = {}
for i in range(state_options):
    state_rule[format(i,f'0{radius}b')] = str(rand_rule[i])

# Create a random lattice (change numbers to strings)
lat = np.random.randint(0,2,lattice_len)
lattice = []
for l in lat:
    lattice.append(str(l))

def getStates(idx, lattice, radius, lattice_len):
    """returns the lattice states around the idx in size radius"""
    checkIdx = list(range(-(radius//2)+idx,(radius//2)+idx+1))
    stateStr = ''
    for i in checkIdx:
        if i > lattice_len-1:
            stateStr += lattice[i%lattice_len]
        else:
            stateStr += lattice[i]
    return stateStr

# For plotting the figure dynamically
plt.ion()
test = plt.imshow(latMat)
plt.show()

new_lat = ['0' for _ in range(lattice_len)]
int_lat = [0 for _ in range(lattice_len)]
for ts in range(timestep):
    plt.cla() # clear figure axes plt.clf() also works
    # Ugly solution
    for iInt in range(lattice_len):
        int_lat[iInt] = int(lattice[iInt])
    latMat[ts,:] = int_lat

    # print(lattice)
    for idx in range(lattice_len):
        state = getStates(idx, lattice, radius, lattice_len)
        new_lat[idx] = state_rule[state]
    lattice = new_lat

    plt.imshow(latMat)
    plt.draw()
    plt.pause(.001)
