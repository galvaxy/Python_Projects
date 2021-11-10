CYLINDRICAL CAPACITOR:

 This program calculates the capacitance of a cylindrical capacitor. The radius of the outer shell (r = 2) is twice the radius of the inner cylinder (r = 1) and they are both given equal but opposite charge densities. The charge per unit length is set equal to Q/L = - epsilon0 for the inner cylinder. The potential at the inner boundary is held at constant V=0. The potential at the outer radius is also a constant although this constant needs to be solved for. 

 Nambla^2 V(r) = - rho(s) / epsilon0

 The program uses the Laplace equation above in cylindrical coordinates to solve for the potential in the inner cavity as well as the outer boundary. The capacitance per unit length is given by C/L = (Q/L) / V(2a) = epsilon0 / V(2a). Initial conditions are set in init.py and the potential is calculated iteratively in calc.py. The calc module is called on untill convergence is met in checkSave.py and then the results are saved to .txt files. The potential profile is saved in capacitor.txt and the accuracy of the calculation is saved in accuracy.txt. The accuracy is calculated by comparing the numerical result with the analytical calculation. The analytical potential profile with the given parameters is found to be V(r) = Ln(r)/(2 pi). The analytic result for the capacitance is found to be C/L = 2 pi epsilon0 / Ln(2). 

 The plots.gp file is a GnuPlot script which can be run using GnuPlot from terminal to create the potential profile plot. The plot is saved to the capacitance.jpeg file. It can be seen that the numerical results agree well with the analytical expectation. The capacitance is found to be within less than %1 error compared to the expected result (can be seen in accuracy.txt)



