from pyqpanda import * 

def R_XX(angle, qubit1, qubit2):
    """构建两个量子比特XX耦合门"""
    circuit = QCircuit()
    circuit.insert(CNOT(qubit1, qubit2))
    circuit.insert(RX(angle, qubit2))
    circuit.insert(CNOT(qubit1, qubit2))
    return circuit

def R_YY(angle, qubit1, qubit2):
    """构建两个量子比特YY耦合门"""  
    circuit = QCircuit()
    circuit.insert(RZ(np.pi/2, qubit1))
    circuit.insert(RZ(np.pi/2, qubit2))
    circuit.insert(CNOT(qubit1, qubit2))
    circuit.insert(RX(angle, qubit2))
    circuit.insert(CNOT(qubit1, qubit2))
    circuit.insert(RZ(-np.pi/2, qubit1))
    circuit.insert(RZ(-np.pi/2, qubit2))
    return circuit
    
def R_ZZ(angle, qubit1, qubit2):
    """构建两个量子比特ZZ耦合门"""
    circuit = QCircuit()
    circuit.insert(CNOT(qubit1, qubit2))
    circuit.insert(RZ(angle, qubit2))
    circuit.insert(CNOT(qubit1, qubit2))
    return circuit
    
def R_X(angle, qubit):
    """构建单量子比特RX门"""
    circuit = QCircuit()
    circuit.insert(RX(angle, qubit))
    return circuit