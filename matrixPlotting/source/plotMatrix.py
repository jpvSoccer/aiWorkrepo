# John Vogel 02/28/2025 john.vogel123@gmail.com

# program to plot basic matrix operations to try to understand
# linear algebra via visualization

#note:
#.venv/bin/pip install matplotlib
#.venv/bin/pip install PyQt6

import matplotlib.pyplot as plt
import numpy as np

# cmap values
# viridis, plasma, gray, Blues, Greens
# coolwarm, RdBu
#tab10, Set1

'''
matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
plt.imshow(matrix, cmap='viridis')
plt.colorbar()
plt.title("Matrix Plot")
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.show()
'''

V1 = np.array([1, 1])

# 1  2
# 3  4
#                   [[row1] , [row2]]
matrix_a = np.array([[1, 2], [3, 4]])

# 5  6
# 7  8
#                   [[row1] , [row2]]
matrix_b = np.array([[5, 6], [7, 8]])

result_add = matrix_a + matrix_b
result_mult = matrix_a @ matrix_b
result_dot = np.dot(matrix_a , matrix_b)
print("\n", matrix_a, "\nplus\n", matrix_b, "\nis\n", result_add, "\n" )
print( matrix_a, "\ntimes\n", matrix_b, "\nis\n", result_mult, "\n" )
print( matrix_a, "\ndot\n", matrix_b, "\nis\n", result_mult, "\n" )
#result = np.dot(matrix2, V1)
#print(result)
#img1=plt.imshow(matrix_a, cmap='Set1')
#plt.colorbar(img1, label="Data Values" )
#plt.title("Matrix Plot")
#plt.xlabel("Columns")
#plt.ylabel("Rows")
#plt.show()


'''
#fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 8))
#fig, ax = plt.subplots(nrows=1, ncols=4, figsize=(10,8))
fig, ax = plt.subplots(figsize=(10, 8))
fig.supxlabel("Linear Algebra Plots", fontsize=15, color='blue')  # add labels to the canvas

ax.set_xlim([-4, 4])
ax.set_ylim([-4, 4])

plt.xlabel(xlabel="X AXIS", loc="center")
plt.ylabel(ylabel="Y AXIS", loc="center")
plt.grid(visible=True)
# Define the vectors
V1 = np.array([1, 1])
V2 = np.array([-0.5, 0.5])
V1Times2 = 2 * V1
NegV1 = -V1
V1PV2 = V1 + V2
CTV1 = 2 * V1
VTV = V1 * V2

X1, Y1 = V1[0], V1[1]
X2, Y2 = V2[0], V2[1]
X3, Y3 = CTV1[0], CTV1[1]
X4, Y4 = V1PV2[0], V1PV2[1]
X5, Y5 = VTV[0], VTV[1]

# colors b, g, r, c, m, y, k, w
ax.quiver(0, 0, X1, Y1, angles='xy', scale_units='xy', scale=1, color='r')
ax.quiver(0, 0, X2, Y2, angles='xy', scale_units='xy', scale=1, color='g')
ax.quiver(0, 0, X3, Y3, angles='xy', scale_units='xy', scale=1, color='y')
ax.quiver(0, 0, X4, Y4, angles='xy', scale_units='xy', scale=1, color='c')
ax.quiver(0, 0, X5, Y5, angles='xy', scale_units='xy', scale=1, color='m')
#ax.quiver(0, 0, -1*X, -1*Y, angles='xy', scale_units='xy', scale=1, color='g')
#ax.quiver(0, 0, 5*X, 5*Y, angles='xy', scale_units='xy', scale=1, color='y')
#ax.quiver(0, 0, -5*X, -5*Y, angles='xy', scale_units='xy', scale=1, color='c')
#plt.savefig("fig.png")
#plt.show()
'''
