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

#     A3x3 TIMES B3x3 multiplication
#     A00 A01 A02
#     A10 A11 A12
#     A20 A21 A22
#    times
#     B00 B01 B02
#     B10 B11 B12
#     B20 B21 B22
#    equals
#     I00 I01 I02
#     I10 I11 I12
#     I20 I21 I22

#     I00=(A00*B00) + (A01*B10) + (A02*B20)
#     I01=(A00*B01) + (A01*B11) + (A02*B21)
#     I02=(A00*B02) + (A01*B12) + (A02*B22)

#     I10=(A10*B00) + (A11*B10) + (A12*B20)
#     I11=(A10*B01) + (A11*B11) + (A12*B21)
#     I12=(A10*B02) + (A11*B12) + (A12*B22)

#     I20=(A20*B00) + (A21*B10) + (A22*B20)
#     I21=(A20*B01) + (A21*B11) + (A22*B21)
#     I22=(A20*B02) + (A21*B12) + (A22*B22)

    global M_3x3_xxx_xxx_xxx_debug
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
