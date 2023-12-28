# Realizar un programa que obtenga la mediana de las alturas en el 
# dataset de Women

# Repetir usando funciones de R
# Verificar la correcta implementación del algoritmo restando ambos vectores
# El resultado debe acercarse a cero.

library(R.utils)
rm(list = ls())
cat("\014")

data <- women$height

N <- length(data)
X <- sort(data)

if(N%%2 == 0)
{
 med1 <- (X[N/2] + X[N/2 + 1])/2 
}else{
    med1 <- X[(N+1)/2]
}
med2 <- median(data)
