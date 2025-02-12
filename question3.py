import numpy as np
import matplotlib.pyplot as plt

num_samples = 100
input_voltage_2 = np.random.uniform(0, 1, (num_samples, 2))
conductance_2 = np.random.uniform(10e-6, 100e-6, (num_samples, 2))

wire_conductance = 0.1
wire_resistance = 1 / wire_conductance
voltage_offset = 0.05

output_current_q3 = np.sum((conductance_2[:, 1] / (1 + conductance_2[:, 1] * wire_resistance)) * (input_voltage_2[:, 1] - voltage_offset))

ideal_current = np.dot(input_voltage_2[:, 1], conductance_2[:, 1])

plt.scatter(ideal_current, output_current_q3)
plt.xlabel('Ideal Current (I_ideal)')
plt.ylabel('Output Current Q3 (Iout_c)')
plt.title('Scatter Plot of Iout_c vs. I_ideal')
plt.show()
