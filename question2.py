#question 2
import numpy as np
import matplotlib.pyplot as plt

num_samples = 100
input_voltage = np.random.uniform(0, 1, num_samples)  
conductance = np.random.uniform(10e-6, 100e-6, num_samples)  

output_current_q1 = np.sum(conductance * input_voltage)
wire_conductance = 0.1
wire_resistance = 1 / wire_conductance
output_current_q2 = np.sum((conductance / (1 + conductance * wire_resistance)) * input_voltage)
ideal_current = np.dot(input_voltage, conductance)
plt.scatter(ideal_current, output_current_q2)
plt.xlabel('Ideal Current (I_ideal)')
plt.ylabel('Output Current with Wire Resistance (Iout_b)')
plt.title('Scatter Plot of Iout_b vs. I_ideal')
plt.show()