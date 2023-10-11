from pyqpanda import *

import matplotlib.pyplot as plt

def plot_fidelities_vs_noise(noise_probs, fidelities, depth):

    plt.plot(noise_probs, fidelities, marker='*')

    plt.xscale('log')

    plt.xlabel('Noise probability')

    plt.ylabel('Fidelity')

    plt.title('Fidelity vs Noise at depth {}'.format(depth))

    plt.savefig('fidelity_vs_noise.png')

    plt.show()