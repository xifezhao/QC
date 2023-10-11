from pyqpanda import *

import matplotlib.pyplot as plt
import numpy as np

def draw_circuit(circuit):
    """以图片形式绘制量子线路"""
    plt.figure()
    circuit.draw_circuit(output="mpl")
    plt.show()

def calculate_error(state1, state2):
    """计算两个量子态之间的误差"""
    fidelity = qfunc_full_state_fidelity(state1, state2)
    return abs(1 - fidelity)

def calculate_mean(obs, state_vectors):
    """计算期望值(均值)"""
    return np.mean([qfunc_full_state_fidelity(obs, vector) for vector in state_vectors])
    
def calculate_std(obs, state_vectors, means=None):
    """计算标准差""" 
    R = len(state_vectors)
    if R == 1:
        return 0
    
    if means is None:
        means = calculate_mean(obs, state_vectors)
        
    var = np.mean([(qfunc_full_state_fidelity(obs, vector) - means)**2 for vector in state_vectors])
    return np.sqrt(var)

def calculate_avg_dm(state_vectors):
    """计算平均密度矩阵"""
    R = len(state_vectors)
    rho = sum(np.outer(vector, np.conj(vector)) for vector in state_vectors) / R
    return rho