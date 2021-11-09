from random import random 
from random import seed

MAX = 501

stream = open("bifurcation.txt","w")
seed(1)
dr = 0.003
r = [2.500]
for n in range(0, MAX):
    x = [1 - random()]
    for i in range(0, int(MAX/10)):
            if(i > 20):
                stream.write("%.3f\t%.3f\n" % (r[n],x[i]))
            x.append( r[n] * x[i] * (1 - x[i]) )
    r.append( r[n] + dr)