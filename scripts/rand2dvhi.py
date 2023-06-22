import sys
import numpy as np
num = int(sys.argv[1])
np.random.seed(int(sys.argv[2]))
done = 0
count = 0
points = np.zeros((num,2),dtype=np.float32)
while (done == 0):
    x = np.random.uniform(-12.0,12.0)
    y = np.random.uniform(-8.0,8.0)
    if ((x*x/25+y*y < 1.5) or (x*x+y*y/25 < 1.5) or
        ((x-10)*(x-10) + y*y/25 < 2) or
        ((x+10)*(x+10) + y*y/25 < 2) or
        ((x-7.5)*(x-7.5)/2 + y*y/16 < 1.5) or
        ((x+7.5)*(x+7.5)/2 + y*y/16 < 1.5) or
        ((x-5)*(x-5)/2 + y*y/25 < 1.5) or
        ((x+5)*(x+5)/2 + y*y/25 < 1.5) or
        ((x-2.5)*(x-2.5)/2 + y*y/9 < 1.5) or
        ((x+2.5)*(x+2.5)/2 + y*y/9 < 1.5)):
        point = np.array([x,y])
        if (count > 0):
            dist = min(np.linalg.norm(points[:count]-point,axis=1))
        else:
            dist = 100
        if (dist > 0.2):
            points[count] = point
            count += 1
    if (count == num):
        done = 1
np.savetxt(sys.argv[3],points,fmt='%.6f')
