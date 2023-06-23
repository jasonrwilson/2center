#include <stdio.h>
#include <stdlib.h>
#include <float.h>
#include <math.h>

#define MAX_POINTS 1024

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

float center_cost_sq (float* p, int n, int c1, int c2, int c3) {
    float cost_sq = 0;
    for (int i=0;i<n;i++) {
	    float dist_sq_1 = dist_sq(p+2*i,p+2*c1);
	    float dist_sq_2 = dist_sq(p+2*i,p+2*c2);
        float dist_sq_3 = dist_sq(p+2*i,p+2*c3);
	    float min_dist_sq = dist_sq_1;
	    if (dist_sq_2 < min_dist_sq) {
	        min_dist_sq = dist_sq_2;
	    }
	    if (dist_sq_3 < min_dist_sq) {
	        min_dist_sq = dist_sq_3;
	    }
	    if (min_dist_sq > cost_sq) {
	        cost_sq = min_dist_sq;
	    }
    }
    return cost_sq;
}

float solve_3center(float* p, int n, int* c) {
	float min_cost_sq = DBL_MAX;
    for (int i=0;i<n-2;i++) {
        for (int j=i+1;j<n-1;j++) {
            for (int k=j+1;k<n;k++) {
		        float cost_sq = center_cost_sq (p, n, i, j, k);
		        if (cost_sq < min_cost_sq) {
			        min_cost_sq = cost_sq;
			        c[0] = i;
			        c[1] = j;
			        c[2] = k;
		        }
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

    /* solve the 3-center problem exactly */
    int c[3];
	float min_cost = solve_3center(p,n,c);

    /* print the minimal cost for the 3-center problem */
    printf ("minimal cost = %.6f\n",min_cost);

    /* print an optimal solution to the 3 center problem */
    printf ("centers : %d %d %d\n",c[0],c[1],c[2]);

	/* program executed successfully */
    return 0;
}
