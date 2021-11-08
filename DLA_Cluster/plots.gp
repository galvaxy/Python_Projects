set terminal jpeg
set output "DLACluster.jpeg"
set size square
set grid lt 0 lw 1
set yrange [-50:50]
set xrange [-50:50]
set xtics 10 font "Menlo,15"
set ytics 10 font "Menlo,15"
set xlabel "x" offset 0,-1 font "Menlo,15"
set ylabel "y" offset -3,0 font "Menlo,15"
set key font "Menlo,15"
plot 'DLACluster.txt' ti "DLA Cluster" lt 1 lw 2 lc rgb "black"

set terminal jpeg
set output "frac_dim.jpeg"
set size square
set grid lt 0 lw 1
set logscale xy
set xrange [1:5*1e1]
set yrange [1:5*1e3]
set xlabel "r" font "Menlo,15"
set ylabel "M" font "Menlo,15"
set xtics 10 font "Menlo,15"
set ytics  10 font "Menlo,15"
set key font "Menlo,15"
set format xy "10^{%T}" 
a = 4
f(x)=a*x**d  
fit [0:40] f(x) 'frac_dim.txt' via d, a
plot 'frac_dim.txt' ti "Fractal Dimensionality" lt 1 lw 2 lc rgb "black", f(x) ti "d=1.62" lc rgb "blue"
unset format
unset logscale

set size square
set grid lt 0 lw 1
set yrange [-50:50]
set xrange [-50:50]
set xtics 10 font "Menlo,15"
set ytics 10 font "Menlo,15"
set xlabel "x" offset 0,-1 font "Menlo,15"
set ylabel "y" offset -3,0 font "Menlo,15"
set key font "Menlo,15"
stats "cluster_animate.txt"
do for[i=0:STATS_blocks]{set terminal jpeg
    set output sprintf('Plots/plot%06.0f.jpeg',i)
    plot 'cluster_animate.txt' index i ti "DLA Cluster" lt 1 lw 2 lc rgb "black"}