set terminal qt enhanced size 1280,960
set y2tics
set ytics nomirror
set title "Is there a correlation between student population and beer consumption in the Netherlands?"
set xlabel "Year"
set ylabel "Student Population (×1000)"
set y2label "Beer Consumption (×1000 hectolitres)"
plot "istherecorrelation.dat" u 1:2 w lp axis x1y1 t "Student Population"
rep "istherecorrelation.dat" u 1:3 w lp axis x1y2 t "Beer Consumption"
set grid

set terminal pngcairo size 1280,960 enhanced
dpi = 300
set output "llvm.png"
rep
