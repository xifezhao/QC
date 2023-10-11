from pyqpanda import *

num_qubits = 4

# 构建Heisenberg模型Hamiltonian
def create_hamiltonian(params, qubits):
    
    hamiltonian = QHamiltonian(qubits)
    
    for i in range(num_qubits-1):
        hamiltonian.insert_pauli_term(-params[-1], PauliOperator(qubits[i], Pauli.Pauli_X))

    for i in range(num_qubits):
        hamiltonian.insert_pauli_term(-params[-2], PauliOperator(qubits[i], Pauli.Pauli_Z) &  
                                        PauliOperator(qubits[(i+1)%num_qubits], Pauli.Pauli_Z))
                                    
    for i in range(num_qubits):
        hamiltonian.insert_pauli_term(-params[-3], PauliOperator(qubits[i], Pauli.Pauli_Y) &
                                        PauliOperator(qubits[(i+1)%num_qubits], Pauli.Pauli_Y))

    for i in range(num_qubits):
        hamiltonian.insert_pauli_term(-params[0],  PauliOperator(qubits[i], Pauli.Pauli_X) &
                                        PauliOperator(qubits[(i+1)%num_qubits], Pauli.Pauli_X))

    return hamiltonian

# 构建量子线路
def circuit(params, time, depth):
    
    qubits = qAlloc_many(num_qubits)
    hamiltonian = create_hamiltonian(params, qubits)
    
    circuit = QCircuit()
    circuit.insert(evolution(time, depth, hamiltonian))
    
    return circuit

# 计算保真度
def calc_fidelity(params, time, depth, noise_prob):
    
    noise_circuit = noise_model(circuit(params, time, depth), noise_prob) 
    ideal_circuit = circuit(params, time, depth)
    
    result1 = run_with_configuration(ideal_circuit, cbits, shot_num=1)
    result2 = run_with_configuration(noise_circuit, cbits, shot_num=1)

    return qfunc_full_state_fidelity(result1.get_qs(), result2.get_qs())