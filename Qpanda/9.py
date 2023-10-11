from pyqpanda import *

import matplotlib.pyplot as plt

def plot_error_vs_qubits(num_qubits, errors, depth, noise_prob=0, shots=1):

    plt.plot(num_qubits, errors, marker='*', linestyle='--')

    plt.xlabel("Number of qubits")
    plt.ylabel("Error")

    title = "Error vs Qubits (Depth={}, p={}, shots={})".format(depth, noise_prob, shots)
    plt.title(title)

    plt.savefig("error_vs_qubits.png")

    plt.show()