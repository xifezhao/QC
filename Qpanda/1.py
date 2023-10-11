from pyqpanda import *
import matplotlib.pyplot as plt

# 读取经典运行时间
file_name = "times_dm.pickle"
f = open(file_name,'rb')
times_dm = pickle.load(f)
f.close()

# 读取量子CPU运行时间 
file_name = "times_q_cpu.pickle"
f = open(file_name,'rb')
times_q_cpu = pickle.load(f)
f.close()

# 读取量子GPU运行时间
file_name = "times_q_gpu.pickle"
f = open(file_name,'rb')
times_q_gpu = pickle.load(f) 
f.close()

# 绘制运行时间抽样对比图
plot_runtime_sampling(times_dm, times_q_cpu, times_q_gpu)