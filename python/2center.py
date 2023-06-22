import sys
import numpy as np

def centers_cost_sq(p,c1,c2):
    cost_sq = 0
    n = len(p)
    for i in range(n):
        dist_sq_1 = np.inner(p[i]-p[c1],p[i]-p[c1])
        dist_sq_2 = np.inner(p[i]-p[c2],p[i]-p[c2])
        min_dist_sq = dist_sq_1
        if (dist_sq_2 < min_dist_sq):
            min_dist_sq = dist_sq_2
        if (min_dist_sq > cost_sq):
            cost_sq = min_dist_sq
    return cost_sq

def solve_2center(p,c):
    min_cost_sq = float("inf")
    n = len(p)
    for i in range(0,n-1):
        for j in range(i+1,n):
            cost_sq = centers_cost_sq(p,i,j)
            if (cost_sq < min_cost_sq):
                min_cost_sq = cost_sq
                c[0] = i
                c[1] = j
    return np.sqrt(min_cost_sq)

p = np.loadtxt(sys.argv[1])
c = np.array([0,0])
min_cost = solve_2center(p,c)
print ('minimum cost =',np.round(min_cost,6))
print ('centers =',c[0],c[1])
