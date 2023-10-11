from pyqpanda import *

import matplotlib.pyplot as plt

def plot_entropies_vs_time(entropies_list, noise_probs):

    for i, p in enumerate(noise_probs):
        if p == 0:
            continue
            
        plt.plot(entropies_list[i], label="p = "+str(p))

    plt.plot(entropies_list[0], linestyle='--', color='black', label="Noiseless")

    plt.xlabel("Time")
    plt.ylabel("Entropy")

    plt.legend()
    plt.savefig("entropy_vs_time.png")
    plt.show()