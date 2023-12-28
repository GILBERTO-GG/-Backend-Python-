# Realizar un programa en R que obtenga la derivada numérica
# f(x)= (x^2)/2        tomando H=0.01 y un dominio entre [-5,5]
# Repetir usando funciones de R
# Verificar la correcta implementación del algoritmo restando ambos vectores
# El resultado debe acercarse a cero.

library(R.utils)
rm(list = ls())
cat("\014")

f <- function(x) {x^2/2}
h <- 0.01

x <- seq(-5, 5, h)
y <- f(x)
yp1 <- rep(0, length(x)-1)

for (i in 1:length(yp1)) 
{
  yp1[i] <- (y[i+1] - y[i])/h
}

yp2 <- diff(y)/h

print(yp1 - yp2)

