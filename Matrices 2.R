#Definir una matriz e imprimir sus elementos uno por uno, primero recorriendo las filas
##y luego las columnas, para posteriormente repetir recorriendo primero las columnas y 
### luego las filas.

library(R.utils)
rm(list = ls())
cat("\014")

A <- matrix(data = c(1,2,3,4,5,6), nrow = 3, ncol = 2, byrow = TRUE)

for(i in 1:nrow(A)){
  for (j in 1:ncol(A)) {
    print(A[i,j])
  }
}