"""
jvogel functions for matrix work
"""
import jpv_functions as mf
import numpy as np
mf.enable_jpv_debugging_features()
mf.defineAllMatrices()

assert mf.jpvDebug == "True", "WARNING: jpvDebug not enabled"

assert isinstance(mf.M_3x3_000_000_000, np.ndarray) , "Null Matrix Type is Incorrect!!!"
#assert isinstance(M_3x3_000_000_000, int) , "Null Matrix Type is Incorrect!!!"
assert mf.M_3x3_000_000_000.shape == (3,3) , "Null Matrix Shape is Incorrect!!!"
