import sys
import numpy as np
num = int(sys.argv[1])
np.random.seed(int(sys.argv[2]))
done = 0
count = 0
points = np.zeros((num,2),dtype=np.float32)
while (done == 0):
    x = np.random.uniform(-4.0,4.0)
    y = np.random.uniform(-2.0,2.0)
    if ((x*x/16+y*y < 1) or (x*x+y*y/4 < 1) or
        ((x-3)*(x-3) + y*y/4 < 1) or
        ((x+3)*(x+3) + y*y/4 < 1)):
        point = np.array([x,y])
        if (count > 0):
            dist = min(np.linalg.norm(points[:count]-point,axis=1))
        else:
            dist = 100
        if (dist > 0.15):
            points[count] = point
            count += 1
    if (count == num):
        done = 1
np.savetxt(sys.argv[3],points,fmt='%.6f')
