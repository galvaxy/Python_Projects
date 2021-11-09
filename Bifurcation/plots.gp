set terminal jpeg
set output "bifur_zoom1.jpeg"
set size square
set xrange [2.8:3.3] 
set xlabel "r" font "Menlo,15"
set ylabel "x" font "Menlo,15"
set xtics 0.2 font "Menlo,15"
set ytics 0.1 font "Menlo,15"
set key font "Menlo,15"
set grid lt 0 lw 1
set title "Bifurcation r1" font "Menlo,15"
plot 'bifurcation.txt' ti " " lc rgb "black" lw 2 pt 0

set terminal jpeg
set output "bifur_zoom2.jpeg"
set size square
set xrange [3.3:3.7]
set xlabel "r" font "Menlo,15"
set ylabel "x" font "Menlo,15"
set xtics 0.2 font "Menlo,15"
set ytics 0.1 font "Menlo,15"
set key font "Menlo,15"
set grid lt 0 lw 1
set title "Bifurcation r2" font "Menlo,15"
plot 'bifurcation.txt' ti " " lc rgb "black" lt 0 lw 2

set terminal jpeg
set output "bifur_zoom3.jpeg"
set size square
set xrange [3.5:3.9]
set xlabel "r" font "Menlo,15"
set ylabel "x" font "Menlo,15"
set xtics 0.2 font "Menlo,15"
set ytics 0.1 font "Menlo,15"
set key font "Menlo,15"
set grid lt 0 lw 1
set title "Bifurcation r3" font "Menlo,15"
plot 'bifurcation.txt' ti " " lc rgb "black" lt 0 lw 2

set terminal jpeg
set output "bifurcation.jpeg"
set size square
set xrange [2.4:4]
set xlabel "r" font "Menlo,15"
set ylabel "x" font "Menlo,15"
set xtics 0.2 font "Menlo,15"
set ytics 0.1 font "Menlo,15"
set key font "Menlo,15"
set grid lt 0 lw 1
set title "Bifurcation of Logistics Map" font "Menlo,15"
set label "x" at 2.88,0.64 tc rgb "red" font "{,30}"
set label "x" at 3.38,0.43 tc rgb "red" font "{,30}"
set label "x" at 3.40,0.83 tc rgb "red" font "{,30}"
plot 'bifurcation.txt' ti " " lc rgb "black" lw 2 lt 0
unset label