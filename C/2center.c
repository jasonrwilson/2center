#include <stdio.h>
#include <stdlib.h>
#include <float.h>
#include <math.h>

#define MAX_POINTS 4096

int read_file (float* points, char* filename) {
    int n = 0;
    float next[2];
    FILE* file_ptr;
    file_ptr = fopen(filename,"r");
    if (file_ptr == NULL) {
	printf ("error : could not open file %s for reading\n",filename);
	exit(1);
    }
    while (fscanf (file_ptr,"%f %f",next,next+1) == 2) {
	if (n < MAX_POINTS) {
	    points[2*n] = next[0];
	    points[2*n+1] = next[1];
	    n += 1;
	} else {
	    printf ("Too many points in file %s\n",filename);
	    fclose (file_ptr);
	    exit(1);
        }
    }
    fclose (file_ptr);
    return n;
}

float dist_sq (float* u, float* v) {
    float diff_x = u[0] - v[0];
    float diff_y = u[1] - v[1];
    return diff_x*diff_x + diff_y*diff_y;
}

float center_cost_sq (float* p, int n, int c1, int c2) {
    float cost_sq = 0;
    for (int i=0;i<n;i++) {
		float min_dist_sq = dist_sq(p+2*i,p+2*c1);
		float dist_sq_2 = dist_sq(p+2*i,p+2*c2);
		if (dist_sq_2 < min_dist_sq) {
	    	min_dist_sq = dist_sq_2;
		}
		if (min_dist_sq > cost_sq) {
	    	cost_sq = min_dist_sq;
		}
    }
    return cost_sq;
}

float solve_2center(float* p, int n, int* c) {
    float min_cost_sq = DBL_MAX;
    for (int i=0;i<n-1;i++) {
        for (int j=i+1;j<n;j++) {
	    	float cost_sq = center_cost_sq (p, n, i, j);
	    	if (cost_sq < min_cost_sq) {
				min_cost_sq = cost_sq;
				c[0] = i;
				c[1] = j;
	    	}
		}
    }
    return sqrt(min_cost_sq);
}

int main (int argc, char** argv) {

    /* storage for the 2d points */
    float p[2*MAX_POINTS];

    /* read the 2d points */
    int n = read_file (p,argv[1]);

    /* solve the 2-center problem exactly */
    int c[2];
    float min_cost = solve_2center(p,n,c);

    /* print the minimal cost for the 2-center problem */
    printf ("minimal cost = %.6f\n",min_cost);

    /* print an optimal solution to the 2-center problem */
    printf ("centers : %d %d\n",c[0],c[1]);

    /* program executed successfully */
    return 0;
}
