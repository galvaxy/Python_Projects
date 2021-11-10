import init
import math

def calc():
    init.dv = 0
    #Update the values of all the points in the array EXCEPT the boundary condition points.
    for i in range(int(init.MAX / 2 + 1), int(init.MAX + 1)):
        if(i == init.MAX):
            init.v[i] = ( init.vout * (1 + init.dr / (i * init.dr)) + init.v[i - 1] + init.dr**2 * init.rho / init.epsilon ) / (2 + init.dr / (i * init.dr))
            init.vout = init.v[i] 
        else:
            init.v[i] = ( init.v[i + 1] * ( 1 + init.dr / (i * init.dr) ) + init.v[i - 1] ) / (2 + init.dr / (i * init.dr))
    for i in range(0, init.MAX + 1): #caclulate the cumulative change in voltage
        init.dv = init.dv + math.fabs(init.v[i] - init.vcheck[i])
    for i in range(0, init.MAX + 1): #re-initialize voltage check list
        init.vcheck[i] = init.v[i]