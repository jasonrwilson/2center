import sys
import numpy as np

def centers_cost_sq(p,c1,c2,c3):
    dist_sq_1 = np.sum((p-p[c1])*(p-p[c1]),axis=1)
    dist_sq_2 = np.sum((p-p[c2])*(p-p[c2]),axis=1)
    dist_sq_3 = np.sum((p-p[c3])*(p-p[c3]),axis=1)
    dist_sq = np.array([dist_sq_1,dist_sq_2,dist_sq_3])
    return np.max(np.min(dist_sq,axis=0))

def solve_3center(p,c):
    min_cost_sq = float("inf")
    n = len(p)
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                cost_sq = centers_cost_sq(p,i,j,k)
                if (cost_sq < min_cost_sq):
                    min_cost_sq = cost_sq
                    c[0] = i
                    c[1] = j
                    c[2] = k
    return np.sqrt(min_cost_sq)

p = np.loadtxt(sys.argv[1])
c = np.array([0,0,0])
min_cost = solve_3center(p,c)
print ('minimum cost =',np.round(min_cost,6))
print ('centers =',c[0],c[1],c[2])
