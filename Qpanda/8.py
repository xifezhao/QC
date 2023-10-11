from pyqpanda import * 

import matplotlib.pyplot as plt

def plot_fidelities_vs_qubits(num_qubits, fidelities, depth):

    plt.plot(num_qubits, fidelities, marker='*')

    plt.xlabel('Number of qubits')

    plt.ylabel('Fidelity')

    plt.title('Fidelity vs Qubits at depth {}'.format(depth))

    plt.savefig('fidelity_vs_qubits.png')

    plt.show()