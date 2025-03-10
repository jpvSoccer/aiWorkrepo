# John Vogel 02/28/2025 john.vogel123@gmail.com

# program to plot basic verctor operations to try to understand 
# linear algebra visualization

import matplotlib.pyplot as plt
import numpy as np

# Create the group of plots
fig, ax = plt.subplots()
ax.set_xlim([-4, 4])
ax.set_ylim([-4, 4])

plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
plt.grid(1)

# Define the vectors
V1 = np.array([1, 1])
V2 = np.array([-0.5, 0.5])
V1Times2 = 2*V1
V1PV2 = V1 + V2
twotimesV1PV2 =2*(V1 + V2)

# Plot the vectors
plt.quiver(0, 0, V1[0], V1[1], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(0, 0, V2[0], V2[1], angles='xy', scale_units='xy', scale=1, color='b')
plt.quiver(0, 0, V1PV2[0], V1PV2[1], angles='xy', scale_units='xy', scale=1, color='g')
plt.quiver(0, 0, twotimesV1PV2[0], twotimesV1PV2[1], angles='xy', scale_units='xy', scale=1, color='r')

plt.show()
