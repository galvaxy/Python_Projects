import calc
import init
import math

def checkSave( ):
    output = open("accuracy.txt","w")
    stream = open("capacitor.txt","w")
    #Call on calc() untill convergence is met
    while(init.dv > init.threshold):
        calc.calc()
    #Calculate the capacitance C = q / v[]
    c = math.fabs(init.q / init.v[init.MAX])
    #Calculate theoretical answer
    theory = (2 * math.pi * (8.854187817 * pow(10, -12))) / math.log(2)
    #Percent Error
    Err = 100 * (c - theory) / theory
    #Save data to a file
    for i in range(0, init.MAX + 1):
        stream.write("%.2f\t%.3f\n" % (i * init.dr, init.v[i], ))
    output.write(" Calculated Capacitance -> %.4e\n\n Analytical Capacitance -> %.3e\n\n Percent Error -> %.2f" % (c, theory, Err))