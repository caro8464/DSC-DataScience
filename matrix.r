# maximum value in matrix

m <- matrix(runif(8), nrow=2,ncol=4)
which(m == max(m), arr.ind = TRUE)
max(m)
m