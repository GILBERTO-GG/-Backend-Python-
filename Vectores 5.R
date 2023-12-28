library(R.utils)

rm(list = ls())
cat("\014")

A <- seq(1, 5, 1)
B <- 1:5


producto <- sum(A*B)

printf("El producto punto de los vectores A y B es: %d\n", producto)