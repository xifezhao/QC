from pyqpanda import *

def create_ising(h, qubits):
    """构建Ising模型哈密顿量"""
    
    hamiltonian = QHamiltonian(qubits)
    
    for i in range(len(qubits)-1):
        hamiltonian.insert_pauli_term(-h, PauliOperator(qubits[i], Pauli.Pauli_X))
        
    for i in range(len(qubits)):
        hamiltonian.insert_pauli_term(-1, PauliOperator(qubits[i], Pauli.Pauli_Z) & 
                                        PauliOperator(qubits[(i+1)%len(qubits)], Pauli.Pauli_Z))
    
    return hamiltonian
    
def create_heisenberg(params, qubits):
    """构建Heisenberg模型哈密顿量"""
    
    hamiltonian = QHamiltonian(qubits)
    
    for i in range(len(qubits)-1):
        hamiltonian.insert_pauli_term(-params[-1], PauliOperator(qubits[i], Pauli.Pauli_X))
        
    for i in range(len(qubits)):
        hamiltonian.insert_pauli_term(-params[-2], PauliOperator(qubits[i], Pauli.Pauli_Z) &
                                        PauliOperator(qubits[(i+1)%len(qubits)], Pauli.Pauli_Z))
    
    for i in range(len(qubits)):
        hamiltonian.insert_pauli_term(-params[-3], PauliOperator(qubits[i], Pauli.Pauli_Y) & 
                                        PauliOperator(qubits[(i+1)%len(qubits)], Pauli.Pauli_Y))
        
    for i in range(len(qubits)):
        hamiltonian.insert_pauli_term(-params[0], PauliOperator(qubits[i], Pauli.Pauli_X) & 
                                        PauliOperator(qubits[(i+1)%len(qubits)], Pauli.Pauli_X))
        
    return hamiltonian