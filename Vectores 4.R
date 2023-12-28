library(R.utils)

rm(list = ls())
cat("\014")

producto_punto <- function(A, B){
  acumulador <- 0
  for(i in A){
    acumulador <- acumulador + A[i]*B[i]
  }
  return(acumulador)
}

A <- seq(1, 5, 1)
B <- 1:5

producto <- producto_punto(A, B)

printf("El producto punto de los vectores A y B es:  %d", producto)