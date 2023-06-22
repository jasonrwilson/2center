import sys
import numpy as np
import matplotlib.pyplot as plt
points = np.loadtxt(sys.argv[1],dtype=np.float32)
plt.gca().set_aspect('equal')
plt.scatter (points[:,0],points[:,1],s=10)
plt.savefig(sys.argv[2])
