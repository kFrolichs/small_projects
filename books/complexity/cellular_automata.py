# Some code to test out 1 dimensional cellular automata
import numpy as np
import matplotlib.pyplot as plt

# General Settings
radius = 3
num_state = 2
lattice_len = 100
timestep = 100
latMat = np.zeros((timestep,lattice_len))

def setup_ca(radius = 3, num_state = 2, rule = "random"):
    """ Returns a dictionary with specific state rules for the automata
    Standard settings will create an 8 bit state cellular automa
    With a random rule from [0-255]"""
    state_options = num_state**radius
    number_rules  = num_state**state_options
    print(len(str(number_rules)))
    if rule == "random" and state_options < 64:
        # Cannot create a random rule for radius >= 7
        rNum = np.random.randint(0,number_rules+1, dtype=np.int64)
        rule = format(rNum, f'0{state_options}b')
    else:
        rNum = int(input(f'Please choose a rule [1-{number_rules}]: '))-1
        rule = format(rNum, f'0{state_options}b')

    state_rule = {}
    for i in range(state_options):
        state_rule[format(i,f'0{radius}b')] = rule[i]
    return state_rule, rNum

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

state_rule, ruleNum = setup_ca(radius)

# Create a random lattice (change numbers to strings)
lat = np.random.randint(0,2,lattice_len)
lattice = []
for l in lat:
    lattice.append(str(l))

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
    plt.title(f'Rule: {ruleNum}')
    plt.draw()
    plt.pause(.001)
