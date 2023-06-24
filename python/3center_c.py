import sys
import numpy as np
from ctypes import c_int, c_float, c_void_p, cdll
lib = cdll.LoadLibrary("./3center.so")
solve_3center_c = lib.solve_3center
solve_3center_c.restype = c_float
p = np.loadtxt(sys.argv[1],dtype=np.float32)
c = np.zeros(3,dtype='int32')
min_cost = solve_3center_c(c_void_p(p.ctypes.data),c_int(len(p)),c_void_p(c.ctypes.data))
print ('minimum cost =',np.round(min_cost,6))
print ('centers =',c[0],c[1],c[2])
