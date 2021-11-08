FIXED END WAVE: 

 This program simulates a Gaussian profile wave through a string with fixed ends. The string is 0.5 m in length, the speed of propagation of the wave, c, is 300 m/s, delta(x) is 0.01 m and delta(t) varies (varying r). 

 The value of r = c * dt/dx should be equal to 1. Three values of r are chosen 1.5, 1 and 0.5. The wave is initialized in init.py and calculated iteratively and saved to .txt files corresponding to the values of r in calc.py. 

 The file plots.gp is a GnuPlot script which can be run using GnuPlot in terminal to create animated gif plots for the three values of r. It can be seen that for r=1.5 there are serious errors that occur and the wave quickly becomes nonsense. For the value of r=0.5 small errors are seen to become present and the wave lags behind the expected wave. The r=0 wave is the numerically stable and correct proagation of the wave.  