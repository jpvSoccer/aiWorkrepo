import numpy as np
import os
import matplotlib.pyplot as plt

def getPythonPath():
   pythonPathEnv = os.getenv("PYTHONPATH")
   print("pythonPathEnv is \n",pythonPathEnv)
   return

def enableJpvDebuggingFeatures():
    global jpvDebug
    jpvDebug = os.getenv("JPVDEBUG")
    if jpvDebug == "True":
        print("JPVDEBUG on")
    else:
        print("JPVDEBUG off")
    return

def defineAllMatrices():

#     P3x3 permutation matrix
#     P11 P12 P13
#     P21 P22 P23
#     P31 P32 P33

#     A3X3 target matrix
#     A11 A12 A13
#     A21 A22 A23
#     A31 A32 A33

#     I10=(A10*B00) + (A11*B10) + (A12*B20)
#     I11=(A10*B01) + (A11*B11) + (A12*B21)
#     I12=(A10*B02) + (A11*B12) + (A12*B22)

#     Multiplication with Permutation on LEFT!!!
#     this results in "ROW" manipulation
#     operate on row 2: add row 1 (P21=1) to row 2 (P22=1 and P23-0)
#     P12=2 means add 2 of row 2 to row 1
#     P21=-1,P22=1,P23=0 means take one of row 1 away from row 2
#     P31=-2 means subtract 2 of row 1 from row 3

#     I11=(P11*A11) + (P12*A21) + (P13*A31)
#     I12=(P11*A12) + (P12*A22) + (P13*A32)
#     I13=(P11*A13) + (P12*A23) + (P13*A33)
#
#     I21=(P21*A11) + (P22*A21) + (P23*A32)
#     I22=(P21*A12) + (P22*A22) + (P23*A32)
#     I23=(P21*A13) + (P22*A23) + (P23*A33)
#
#     I31=(P31*A11) + (P32*A23) + (P33*A31)
#     I32=(P31*A12) + (P32*A22) + (P33*A32)
#     I33=(P31*A13) + (P32*A23) + (P33*A33)
# PI Identity Matrix leaves A unchanged
# take one of each row
# 1 0 0
# 0 1 0
# 0 0 1
# A =
#    1 2 −1
#    2 1 2
#    −1 2 1
# A-1 =
#     3/16 1/4 −5/16
#     1/4 0 1/4
#     −5/16 1/4 3/16

    global M_3x3_xxx_xxx_xxx_debug
    global M_3x3_xxx_xxx_xxx_debug_1
    global M_3x3_xxx_xxx_xxx_debug_2
    global M_3x3_000_000_000
    global M_3x3_100_000_000
    global M_3x3_100_010_001
    global M_3x3_111_222_333
    global M_3x3_123_456_789
    global M_3x1_sum_all_rows, M_3x1_sum_row1, M_3x1
    global M_1x3_100_grab_row1, M_1x3_010_grab_row2, M_1x3_001_grab_row3
    global M_3x2
    global M_3x3_swap_r1_r2, M_3x3_swap_r1_r3, M_3x3_swap_r2_r3
    global M_3x3_reverse_rows, M_3x3_rotate_rows

    M_3x3_xxx_xxx_xxx_debug = np.array([[0, 0, 1], [0, 0, 0], [0, 0, 0]])
    #this is a matrix and its inverse; when multiplies you get the identity matrix
    M_3x3_xxx_xxx_xxx_debug_1 = np.array([[1, 2, -1], [2, 1, 2], [-1, 2, 1]])
    M_3x3_xxx_xxx_xxx_debug_2 = np.array([[3/16, 1/4, -5/16], [1/4, 0, 1/4], [-5/16, 1/4, 3/16]])

    M_3x1_sum_all_rows = np.array([[1], [1], [1]])
    M_3x1_sum_row1 = np.array([[1], [0], [0]])
    M_3x1 = np.array([[0], [0], [1]])

    M_1x3_100_grab_row1 = np.array([1, 0, 0])
    M_1x3_010_grab_row2 = np.array([0, 1, 0])
    M_1x3_001_grab_row3 = np.array([0, 0, 1])

    M_3x2 = np.array([[0, 0], [0, 0], [1, 0]])

    M_3x3_000_000_000 = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    M_3x3_100_000_000 = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
    M_3x3_100_010_001 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    M_3x3_swap_r1_r2 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    M_3x3_swap_r1_r3 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    M_3x3_swap_r2_r3 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    M_3x3_reverse_rows = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    M_3x3_rotate_rows = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])

    M_3x3_111_222_333 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    M_3x3_123_456_789 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    return

def matrixPlotRoutines():
    # cmap values
    # viridis, plasma, gray, Blues, Greens, coolwarm, RdBu, tab10, Set1
    # img1=plt.imshow(mA, cmap='Set1')
    # plt.colorbar(img1, label="Data Values" )
    # plt.title("Matrix Plot")
    # plt.xlabel("Columns")
    # plt.ylabel("Rows")
    # plt.show()

    # fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 8))
    # fig, ax = plt.subplots(nrows=1, ncols=4, figsize=(10,8))
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
    return
