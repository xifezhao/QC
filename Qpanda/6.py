from pyqpanda import *

import matplotlib.pyplot as plt

def plot_runtimes_vs_qubits(num_qubits, runtimes_cpu, runtimes_gpu):

    plt.plot(num_qubits, runtimes_cpu, label='CPU', marker='*', color='tab:blue')

    plt.plot(num_qubits, runtimes_gpu, label='GPU', marker='*', color='tab:green')

    plt.xlabel("Number of Qubits")

    plt.ylabel("Runtime (s)")

    plt.yscale('log')

    plt.legend()

    plt.savefig('runtime_vs_qubits.png') 

    plt.show()