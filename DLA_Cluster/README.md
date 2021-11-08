DLA CLUTER:

 This program builds a diffusion limited aggregation (DLA) cluster and calculates its fractal dimensionality. An initial point is set at the center of the grid. Then a "walker"  is initialized somwhere on the boundary of the grid and takes random steps until it reaches the cluster (initially a single point at the center of the grid). This process continues untill the cluster grows large enough to reach the boundary of the grid. 

 The grid and central point are initialized in init.py. The random walks are calculated in build.py. The random walks are calculated by taking random numbers between 0 and 1 and deciding how to move based on this random number (ex. if the number is    # < 0.5 the walker moves to the right, if # > 0.5 it moves to the left). When a walker hits the cluster, a new walker is initialized on the grid boundary. When the cluster grows such that it touches the grid boundary the caclulation stops. 

 M ~ r^(d)

 The clusters fractal dimensionality is calculated in frac_dim.py. The fractal dimensionality is calculated by counting the number of points in the cluster within a given radius and plotting this as a function of radius. The number of points M will grow proportionally to r given by the equation above. The exponent d is the fractal dimensionality. On a log log plot d will be the slope of the line fitting the M(r) curve. 

 Data is saved to .txt files using save.py. The plots.gp file is a GnuPlot script that can be run using GnuPlot from terminal to view plots and animations. Only the first walker is animated since it requires a vast amount of memory to animate the entire cluster. The animation is saved as the cluster_animate.gif file. The final cluster is saved as DLACluster.jpeg. The data and best fit line for the clusters fractal dimensionality is saved as frac_dim.jpeg. 