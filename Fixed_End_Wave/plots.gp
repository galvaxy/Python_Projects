set terminal gif animate delay 1
set style data linespoint
set size square
set output "fixedEndWave.gif"
set yrange [-2:2]
set xrange [0:0.5]
set xtics font "Menlo,15"
set ytics font "Menlo,15" 
set xlabel "x" font "Menlo,15"
set ylabel "y" font "Menlo,15"
set key font "Menlo,15"
set grid lt 0 lw 1
do for [i=0:200]{plot 'waveCalc_r1.5.txt' index i ti "r=1.5" lt 0 lw 2 lc rgb "red",\
'waveCalc_r1.txt' index i ti "r=1" lt 0 lw 2 lc rgb "black",\
'waveCalc_r0.5.txt' index i ti "r=0.5" lt 0  lw 2 lc rgb "blue"}