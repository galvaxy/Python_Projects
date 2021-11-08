import init

def calc():
    stream = open("waveCalc_r1.5.txt","w")

    for i in range(0, init.MAXi + 1): #print the initial wave profile because that information (stored in an array) will be replaced in the net loop
        stream.write("%.2f\t%e\n" % (i * init.dx, init.y[i][0]))
    stream.write("\n\n")

    for j in range(0, init.MAXj): # calculate the wave profile at the next time step
        for i in range(1, init.MAXi):
            init.y[i][2] = 2 * (1 - init.r * init.r) * init.y[i][1] + init.r * init.r * (init.y[i + 1][1] + init.y[i - 1][1]) - init.y[i][0]
        
        for i in range(0, init.MAXi +1): #print newly calculated profile
            stream.write("%.2f\t%e\n" % (i * init.dx, init.y[i][2]))
        stream.write("\n\n")
        
        for i in range(1, init.MAXi): #re-initialize arrays so to save memory usage. Only 3 time steps are ever stored at a time.
            init.y[i][0] = init.y[i][1]
            init.y[i][1] = init.y[i][2]
    stream.close()