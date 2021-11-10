set terminal jpeg
set output "capacitor.jpeg"
set size square
set xrange [0:2]
set yrange [0:0.12]
set xtics 0.4 font "Menlo,15"
set ytics font "Menlo,15"
set xlabel offset 0,-2 "r" font "Menlo,15"
set ylabel offset -3,0 "V" font "Menlo,15"
set key font "Menlo,15"
set grid lt 0 lw 1
f(x) = x > 1 ? log(x) / (2 * pi) : 0 
set style data linespoint
set title "Cylindrical Capacitor" font "Menlo,20"
set label "C/L = 8.0844e-11\nerror = 0.73%" at 0.2,0.05 tc rgb "black" font "{Menlo,15}"
plot 'capacitor.txt' ti "Numerical Solution" lt 0 lw 3 lc rgb "black", f(x) ti "Analytical Solution" lt 1 lw 2 lc rgb "red"
unset label