from random import seed
from random import random
import init
import save

def build():

    seed(1)
    coin1 = random()
    coin2 = random()

    flag1 = 0

    k = 1

    #Set walkers until cluster reaches edge of array
    while(flag1 < 1):
        flag2 = 0
        #set walker at random location on outer edge of array
        coin1 = random() 
        if(coin1 < 0.5):
            coin2 = random() 
            if(coin2 < 0.5):
                N = int( (init.MAXj - 1) * random() )
                if(N == 0):
                    N = N + 1
                init.cluster[1][N] = 1
                x = 1
                y = N
                save.save(0, k)
            else:
                N = int( (init.MAXj - 1) * random() )
                if(N == 0): 
                    N = N + 1
                init.cluster[init.MAXi - 1][N] = 1
                x = init.MAXi - 1
                y = N
                save.save(0, k)
        else:
            coin2 = random()
            if(coin2 < 0.5):
                N = int( (init.MAXi - 1) * random() )
                if(N == 0):
                    N = N + 1
                init.cluster[N][1] = 1
                x = N
                y = 1
                save.save(0, k)
            else:
                N = int( (init.MAXj - 1) * random() )
                if(N == 0):
                    N = N + 1
                init.cluster[N][init.MAXj - 1] = 1
                x = N
                y = init.MAXj - 1
                save.save(0, k)

        #Do a random walk until walker runs into the cluster
        #Check if cluster has grown to outer edge
        test1 = init.cluster[x + 1][y] + init.cluster[x - 1][y] + init.cluster[x][y + 1] + init.cluster[x][y - 1]
        if(test1 < 1):
            while(flag2 < 1):
                #Make sure walker is not on the edge of the array
                if(x == 1):
                    init.cluster[x][y] = 0
                    init.cluster[x + 1][y] = 1
                    x = x + 1
                    save.save(0, k)
                if(x == init.MAXi - 1):
                    init.cluster[x][y] = 0
                    init.cluster[x - 1][y] = 1
                    x = x - 1
                    save.save(0, k)
                test2 = init.cluster[x + 1][y] + init.cluster[x - 1][y] + init.cluster[x][y + 1] + init.cluster[x][y - 1]
                if(y == 1 and test2 == 0):
                    init.cluster[x][y] = 0
                    init.cluster[x][y + 1] = 1
                    y = y + 1
                    save.save(0, k)
                if(y == init.MAXj - 1 and test2 == 0):
                    init.cluster[x][y] = 0
                    init.cluster[x][y - 1] = 1
                    y = y - 1
                    save.save(0, k)
                test3 = init.cluster[x + 1][y] + init.cluster[x - 1][y] + init.cluster[x][y + 1] + init.cluster[x][y - 1]
                #Now that walker is off of edge make a random movement in either the y or the x direction
                if(test3 == 0):
                    coin1 = random()
                    if(coin1 < 0.5):
                        coin2 = random()
                        if(coin2 < 0.5):
                            init.cluster[x][y] = 0
                            init.cluster[x - 1][y] = 1
                            x = x - 1
                            save.save(0, k)
                        else:
                            init.cluster[x][y] = 0
                            init.cluster[x + 1][y] = 1
                            x = x + 1
                            save.save(0, k)
                    else:
                        coin2 = random()
                        if(coin2 < 0.5):
                            init.cluster[x][y] = 0
                            init.cluster[x][y - 1] = 1
                            y = y - 1
                            save.save(0, k)
                        else:
                            init.cluster[x][y] = 0
                            init.cluster[x][y + 1] = 1
                            y = y + 1
                            save.save(0, k)
                test4 = init.cluster[x + 1][y] + init.cluster[x - 1][y] + init.cluster[x][y + 1] + init.cluster[x][y - 1]
                if(test4 > 0):
                    flag2 = 1
                    k = k + 1
        else:
            flag1 = 1

    save.save(1, 0)