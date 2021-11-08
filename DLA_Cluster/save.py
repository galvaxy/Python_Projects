import init

def save(check, safe): #Save points that are occupied by the cluster
    
    MAX = 1 #number of walkers to keep track of for animation (keeping track of all walkers requires too much memory)
    if(check == 0 and safe <= MAX): #Save walkers at each iteration
        stream = open("cluster_animate.txt","a")
        for i in range(0, init.MAXi + 1):
            for j in range(0, init.MAXj + 1):
                if(init.cluster[i][j] == 1):
                    stream.write("%d\t%d\n" % (i - init.MAXi/2, j - init.MAXj/2))
        stream.write("\n\n")
    
    if(check == 1 and safe == 0): #save final cluster
        stream = open("DLACluster.txt","w")
        for i in range(0, init.MAXi + 1):
            for j in range(0, init.MAXj + 1):
                if(init.cluster[i][j] == 1):
                    stream.write("%d\t%d\n" % (i - init.MAXi/2, j - init.MAXj/2))