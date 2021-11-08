MAXi = 100
MAXj = 100
cluster = []

def init(): #initialize all elements in array to zero except for seed in middle of array.
    for i in range(0, MAXi + 1):
        cluster.append([0])
        for j in range(0, MAXj + 1):
            cluster[i].append(0)
    cluster[MAXi//2][MAXj//2] = 1