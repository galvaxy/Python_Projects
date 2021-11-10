import math

MAX = 100
a = 1 #radius of inner cylinder
dr = (2 * a) / MAX #spacial resolution
epsilon = (8.854187817 * pow(10, -12))
q = epsilon #charge per unit length 
rho =  q / (2 * math.pi * (2*a) * dr) #charge density of outer shell
dv = 1
threshold = 1e-7

v = []
vcheck = [] #list to check convergence
v.append(0) #boundary condition for the inner cylinder
vcheck.append(0)
for i in range(1, MAX):
    v.append(0) 
    vcheck.append(0)
v.append(1) #Initial guess for the outer cylinder
vout = v[MAX]
vcheck.append(0)
    