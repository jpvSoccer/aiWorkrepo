"""
John Vogel 02/28/2025 john.vogel123@gmail.com

program to study basic matrix operations to try to understand
linear algebra
"""

#import os
#import matplotlib.pyplot as plt
#import numpy as np
import jpvFunctions as mf
#import jpvAssertions

#mf.getPythonPath()
mf.defineAllMatrices()

# when mutiplied you get the identity matrix
mA = mf.M_3x3_xxx_xxx_xxx_debug_1 #print("JPV: A")
mB = mf.M_3x3_xxx_xxx_xxx_debug_2 #print("JPV: Ainverse")
#mB = mf.M_3x1_xxx_debug
#mA = mf.M_1x3_xxx_debug

#mA = mf.M_3x3_xxx_xxx_xxx_debug print("JPV: using 3x3 debug matrix")
#mA = mf.M_3x3_000_000_000 print("JPV: using 3x3 null matrix")
#mA = mf.M_3x3_100_010_001; print("JPV: using 3x3 identity matrix")
#mA = mf.M_3x3_100_000_000; print("JPV: using 3x3 null matrix")
#mB = mf.mf.M_3x3_111_222_333; print("JPV: using M_3x3_111_222_333 matrix")
#mB = mf.M_3x3_123_456_789; print("JPV: using M_3x3_123_456_789 matrix")
#mA = mf.M_3x3_reverse_rows
#mA = mf.M_3x3_rotate_rows
#mA = mf.M_3x3_swap_r1_r2
#mA = mf.M_3x3_swap_r1_r3
#mA = mf.M_3x3_swap_r2_r3
#mA = mf.M_3x3_rotate_rows
#mB = mf.M_3x1_sum_all_rows


#print( mA, "\ntimes\n", mB, "\nis\n")

#mA = mf.M_1x3_100_grab_row1; print("JPV: using M1x3 to grab 3x3 row 1")
#mA = mf.M_1x3_010_grab_row2; print("JPV: using M1x3 to grab 3x3 row 2")
#mA = mf.M_1x3_001_grab_row3; print("JPV: using M1x3 to grab 3x3 row 3")

print("\nJPV: calculating...")
print( mA, "\ntimes\n", mB, "\nis\n", mA @ mB, "\n" )
#print( mA, "\ntimes\n", mB, "\nis\n", np.dot(mA, mB), "\n" )
