import init
import math

def fract_dim():
    sum = 0

    output = open("frac_dim.txt","w")

    for R in range(1, int(0.5 * init.MAXi) + 1):
        for i in range(0, init.MAXi + 1):
            for j in range(0, init.MAXj + 1):
                r = math.sqrt( (i - 0.5 * init.MAXi) * (i - 0.5 * init.MAXi) + (j - 0.5 * init.MAXj) * (j - 0.5 * init.MAXj) )
                if(r <= R):
                     sum = sum + init.cluster[i][j]
        output.write("%d\t%d\n" % (R,sum))
        sum=0