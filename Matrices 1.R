#Definir e imprimir las siguientes matrices:
#--Matriz de 3x2 primero llenando las columnas.
#--Matriz de 2x3 primero llenando las columnas.
#--Matriz de 2x3 primero llenando las filas.
#--Matriz de 3x3 primero llenando las filas y con elemantos faltantes a la hora de definir
#  los datos de entrada.
#--Matriz de 3x3 primero llenando las filas y con elementos completos.
#--Matriz de 3x3 primero llenando las filas y con elementos adicionales.
#--Matriz de 3x3 primero llenando las filas con rbind.
#--Matriz de 3x3 primero llenando las columnas con cbind.

library(R.utils)
rm(list =  ls())
cat("\014")

print("Matriz de 3x2 primero llenando las columnas")
A <- matrix(data = c(1,2,3,4,5,6), nrow = 3, ncol = 2)
print(A)

print("Matriz de 2x3 primero llenando las columnas")
A <- matrix(data = c(1,2,3,4,5,6), nrow = 2, ncol = 3)
print(A)

print("Matriz de 2x3 primero llenando las filas")
A <- matrix(data = c(1,2,3,4,5,6), nrow = 2, ncol = 3, byrow = TRUE)
print(A)

print("Matriz de 3x3 primero llenando las filas y con elementos faltantes")
A <- matrix(data = c(1,2,3,4,5,6), nrow = 3, ncol = 3, byrow = TRUE)
print(A)

print("Matriz de 3x3 primero llenando las filas y con elementos completos")
A <- matrix(data = c(1,2,3,4,5,6,7,8,9), nrow = 3, ncol = 3, byrow = TRUE)
print(A)

print("Matriz de 3x3 primero llenando las filas y con elementos adicionales")
A <- matrix(data = c(1,2,3,4,5,6,7,8,9,10,11,12), nrow = 3, ncol = 3, byrow = TRUE)
print(A)

print("Matriz de 3x3 primero llenando las filas con rbind")
A <- rbind(c(1,2,3), c(4,5,6), c(7,8,9))
print(A)

print("Matriz de 3x3 primero llenando las filas con cbind")
A <- cbind(c(1,2,3), c(4,5,6), c(7,8,9))
print(A)





