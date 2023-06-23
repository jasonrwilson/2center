import sys
import numpy as np
import matplotlib.pyplot as plt

# read the points
p = np.loadtxt(sys.argv[1],dtype=np.float32)

# plot the points
plt.gca().set_aspect('equal')
plt.scatter (p[:,0],p[:,1],s=2,color='black')

# plot the centers (if additional command line arguments present)
if (len(sys.argv)-3 > 0):
    ctr = np.array([int(s) for s in sys.argv[3:]])
    dist_sq = np.zeros((len(ctr),len(p)))
    for i in range(len(ctr)):
        dist_sq[i] = np.sum((p-p[ctr[i]])*(p-p[ctr[i]]),axis=1)
    clu = np.argmin(dist_sq,axis=0)
    ex = np.argmax(np.min(dist_sq,axis=0))
    plt.scatter (p[:,0],p[:,1],c=clu,cmap="tab10",s=10)
    plt.scatter (p[ctr,0],p[ctr,1],c=range(len(ctr)),cmap="tab10",s=100)
    plt.scatter (p[ex,0],p[ex,1],s=50,facecolors='none', edgecolors='black')

#save the plot as an image
plt.savefig(sys.argv[2])
