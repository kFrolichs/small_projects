# Some code to test out 1 dimensional cellular automata
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# General Settings
radius = 3
num_state = 2
lattice_len = 250
timestep = 100
latMat = np.zeros((timestep,lattice_len))

def setup_ca(radius = 3, num_state = 2, rule = "random"):
    """ Returns a dictionary with specific state rules for the automata
    Standard settings will create an 8 bit state cellular automa
    With a random rule from [0-255]"""
    state_options = num_state**radius
    number_rules  = num_state**state_options
    # print(len(str(number_rules)))
    if rule == "random" and state_options < 64:
        # Cannot create a random rule for radius >= 7
        rNum = np.random.randint(0,number_rules+1, dtype=np.int64)
        rule = format(rNum, f'0{state_options}b')
    else:
        rNum = int(input(f'Please choose a rule [1-{number_rules}]: '))
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

def calc_ca(state_rule,lattice_len, timestep):
    # Create a random lattice (change numbers to strings)
    lat = np.random.randint(0,2,lattice_len)
    lattice = []
    for l in lat:
        lattice.append(str(l))

    new_lat = ['0' for _ in range(lattice_len)]
    int_lat = [0 for _ in range(lattice_len)]
    for ts in range(timestep):
        # Ugly solution
        for iInt in range(lattice_len):
            int_lat[iInt] = int(lattice[iInt])
        latMat[ts,:] = int_lat

        # print(lattice)
        for idx in range(lattice_len):
            state = getStates(idx, lattice, radius, lattice_len)
            new_lat[idx] = state_rule[state]
        lattice = new_lat
    return latMat

def show_ca(full_mat, fig_title, anim = True):
    """ Input full_mat is the full matrix with states
    animate (Boolean) determines if you want to animate time or just
    show the finished process. Outputs a figure """
    fig, ax = plt.subplots(figsize=(12.8,9))
    # ax.figure()
    timesteps = np.shape(full_mat)
    show_mat = np.zeros(timesteps)
    # If you want it animated
    if anim:
        ims = []
        for i in range(1,timesteps[0]):
            # Fill-in the matrix timestep by timestep
            show_mat[i,:] = full_mat[i,:]
            im = ax.imshow(show_mat, animated=True, cmap='Greys')
            if i == 0:  # show an initial one first
                show_mat[0,:] = full_mat[0,:]
                ax.imshow(show_mat)
            ims.append([im])

        ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat=False)
    # If you just want the static end image
    else:
        im = ax.imshow(full_mat, cmap='Greys')
    plt.title(fig_title)
    plt.show()

state_rule, ruleNum = setup_ca(radius,2,'Choose Rule')
lat_mat = calc_ca(state_rule, lattice_len, timestep)
show_ca(latMat,f'Rule: {ruleNum}',True)
