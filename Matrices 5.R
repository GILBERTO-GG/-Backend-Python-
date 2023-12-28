# Se solicita realizar un programa que multiplique dos matrices.
# Se tiene que verificar el resultado con el operador (%*%).

library(R.utils)
rm(list = ls())
cat("\014")

A <- matrix(data = c(1,2,3,4,5,6,7,8,9), nrow = 3, ncol = 3, byrow = TRUE)
B <- matrix(data = c(1,0,0,0,1,0,0,0,1), nrow = 3, ncol = 3, byrow = TRUE)
C <- matrix(data = 0, nrow = 3, ncol = 3, byrow = TRUE)

#for(i in 1:nrow(A)){
#  for(j in 1:ncol(A)){
 #   C[i,j] <- sum(A[i,]*B[,j])
#  }
#}

C <- A%*%B

print(C)