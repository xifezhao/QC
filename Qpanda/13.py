from pyqpanda import *

import time

def trotter_circuit(params, qubits, time, depth, noise_prob):
    """构建噪声Trotter化线路"""
    
    hamiltonian = create_hamiltonian(params, qubits) # 创建Hamiltonian
    
    circuit = QCircuit()
    
    for _ in range(depth):
        circuit.insert(evolution(time/depth, hamiltonian)) # 演化场景
        circuit.insert(depolarizing_channel(qubits, noise_prob)) # 加入退相干噪声
        
    return circuit

def run(qubits, params, time, depth, noise_prob):
    """运行模拟"""
    
    circuit = trotter_circuit(params, qubits, time, depth, noise_prob)
    result = run_with_configuration(circuit, cbits, shot_num=1) 
    return result.get_qs()

# 计算保真度
def fidelity(qubits, params, time, depth, noise_prob):
    
    state1 = run(qubits, params, time, depth, 0)
    state2 = run(qubits, params, time, depth, noise_prob)  
    
    return qfunc_full_state_fidelity(state1, state2)

if __name__ == "__main__":

    qubits = 4
    params = [1,2,1,0.3]
    time = 2.5
    depth = 1
    noise_prob = 0.5 

    times = []
    for i in range(2, qubits+1):
        
        start = time.time()
        
        print(fidelity(range(i), params, time, depth, noise_prob))
        
        end = time.time()
        times.append(end-start)

    print(f"Average time: {np.mean(times)}")