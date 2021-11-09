BIFURCATION -> LOGISTIC MAP

 x[i + 1] = r * x[i] * (1 - x[i]) 

 This program studies chaos in the logist map (iterative equation above). The program chooses a random value of x from 0 to 1 and then interates through the logist map for 50 iterations. After 20 iterations (to map convergence of logistic map) the results are saved. This is repeated for various values of r ranging from 2.5 to 4 (for r > 4 the above the logistic map becomes unstable). The results are calculated in bifurcation.py and saved to bifurcation.txt

 The plots.gp file is a GnuPlot script that can be run using GnuPlot from terminal to create plots. As can be see, the logist map converges to a single value while r is small. As r becomes larger the convergence splits into two branches. Increasing r further causes more and more branches with a binary behavior at each split. The entire plot is found in bifurcation.jpeg. Zoomed in plots at the first three splits are found in bifur_zoom1.jpeg, bifur_zoom2.jpeg and bifur_zoom3.jpeg. 