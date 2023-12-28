#--Definir una matriz y por cada columna de la misma extraer el elemento con el mayor valor.
# almacenar todos estos elementos en un vector.

library(R.utils)
rm(list = ls())
cat("\014")

A <- matrix(data = c(1,2,3,4,5,6,7,8,9,10), nrow = 2, ncol = 5, byrow = FALSE)
print(A)

y <- rep(0, length(A[1,]))
print(y)

for (i in 1:ncol(A)) 
{
 y[i] <- max(A[,i])
}

print(y)