# John Vogel 02/28/2025 john.vogel123@gmail.com

# program to plot basic verctor operations to try to understand 
# linear algebra visualization

import matplotlib.pyplot as plt
import numpy as np

# Create the plot
fig, ax = plt.subplots()
# Set plot limits
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
plt.grid()


# Define the vectors
V1 = np.array([1, 1])
V1Times2 = 2*V1
V2 = np.array([-0.5, 0.5])
V1PV2 = V1 + V2

# Plot the vectors
ax.quiver(0, 0, V1[0], V1[1], angles='xy', scale_units='xy', scale=1, color='r')
ax.quiver(0, 0, V2[0], V2[1], angles='xy', scale_units='xy', scale=1, color='b')
ax.quiver(0, 0, V1PV2[0], V1PV2[1], angles='xy', scale_units='xy', scale=1, color='g')

# Show grid and plot
plt.show()
