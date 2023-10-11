from pyqpanda import *

import matplotlib.pyplot as plt

def plot_fidelities_vs_noise(noise_probs, fidelities_list, depth_list):

    for i, depth in enumerate(depth_list):

        plt.loglog(noise_probs, fidelities_list[i], label="Depth = "+str(depth))

    plt.title("Fidelity vs Noise")  
    plt.xlabel("Noise probability")
    plt.ylabel("Fidelity")

    plt.legend()
    plt.savefig("fidelity_vs_noise.png") 
    plt.show()