import math 

MAXi = 50
MAXj = 200 
dx = 0.01 
k = 1000 #The value of k is a measure of the width of the Gaussian pluck
y = [[0,0,0]] #initialize the boundary conditions, the ends of the string are fixed
r = 1.5

def init():
    for i in range(1, MAXi): #Initialize the shape of the pluck of the string (cannot contradict the boundary condition)
        y.append([ 2 * math.exp( -k * (i * dx - 0.25) * (i * dx - 0.25) ), 2 * math.exp(-k * (i * dx - 0.25) * (i * dx - 0.25) ), 0] )
    y.append([0,0,0]) 