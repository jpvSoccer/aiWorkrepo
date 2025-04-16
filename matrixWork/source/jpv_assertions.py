"""
jvogel functions for matrix work
"""
import jpvFunctions as mf
import numpy as np
mf.enableJpvDebuggingFeatures()
mf.defineAllMatrices()

assert mf.jpvDebug == "True", "WARNING: jpvDebug not enabled"

assert isinstance(mf.M_3x3_000_000_000, np.ndarray) , "Null Matrix Type is Incorrect!!!"
#assert isinstance(M_3x3_000_000_000, int) , "Null Matrix Type is Incorrect!!!"
assert mf.M_3x3_000_000_000.shape == (3,3) , "Null Matrix Shape is Incorrect!!!"
