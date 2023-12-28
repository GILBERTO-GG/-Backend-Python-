# Realizar un programa que obtenga la media aritmética de las alturas en el 
# dataset de Women

# Repetir usando funciones de R
# Verificar la correcta implementación del algoritmo restando ambos vectores
# El resultado debe acercarse a cero.

library(R.utils)
rm(list = ls())
cat("\014")

data <- women$height

sum <- 0
N <- length(data)
for (i in 1:N) 
{
 sum <- sum + data[i] 
}

mu1 <- sum/N

mu2 <- mean(data)

print(mu1 - mu2)













