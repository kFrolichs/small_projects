# Some code to test out 1 dimensional cellular automata
import numpy as np
import matplotlib.pyplot as plt

# General Settings
radius = 3
num_state = 2
lattice_len = 100
timestep = 100
latMat = np.zeros((timestep,lattice_len))

state_options = num_state**radius
number_rules  = num_state**state_options

# Choose a rule and convert to binary
rNum = int(input(f'Please choose a rule [1-{number_rules}]: '))-1
rule = format(rNum, '08b')
print(f'Your chosen rule: {rule}')

# Attach the rule to the states
state_rule = {}
for i in range(state_options):
    state_rule[format(i,'03b')] = rule[i]

# Create a random lattice (change numbers to strings)
lat = np.random.randint(0,2,lattice_len)
lattice = []
for l in lat:
    lattice.append(str(l))

# Check each position of the lattice
pos = [i for i in range(lattice_len)]
pos.insert(0,-1)
pos.append(0)

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
        state = lattice[pos[idx-1]]+lattice[pos[idx]]+lattice[pos[idx+1]]
        new_lat[idx] = state_rule[state]
    lattice = new_lat

    plt.imshow(latMat)
    plt.draw()
    plt.pause(.001)
