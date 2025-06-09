set terminal pngcairo size 1000,700 enhanced font 'Verdana,10'
set output 'interpolation_plot.png'

set title "Lagrange Interpolation vs Actual Function"
set xlabel "x"
set ylabel "y"
set grid
set key outside top center

plot "table.txt" using 1:2 with lines lw 2 lc rgb "black" title "Original", \
     "interpolated.txt" using 1:2 with lines lw 2 lc rgb "green" title "Interpolated (Uniform)", \
     "interpolated2.txt" using 1:2 with lines lw 2 lc rgb "blue" title "Interpolated (Chebyshev)", \
     1/(1 + 12*x**2) with lines lw 2 lc rgb "red" title "f(x) = 1 / (1 + 12x^2)"
