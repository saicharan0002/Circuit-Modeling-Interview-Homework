#Question 1
import numpy as np
import matplotlib.pyplot as plt

num_samples = 100
input_voltage = np.random.uniform(0, 1, num_samples)  
conductance = np.random.uniform(10e-6, 100e-6, num_samples)  

output_current_q1 = np.sum(conductance * input_voltage)

ideal_current = np.dot(input_voltage, conductance)
plt.scatter(ideal_current, output_current_q1)
plt.xlabel('Ideal Current (I_ideal)')
plt.ylabel('Output Current Q1 (Iout_a)')
plt.title('Scatter Plot of Iout_a vs. I_ideal')
plt.show()