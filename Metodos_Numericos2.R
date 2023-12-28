# Realizar un programa en R que obtenga la integral numérica de la siguiente función
# f(x) = 2X
# Tomando:  A = 0,  B = 5, N = 1000

# Repetir usando funciones de R
# Verificar la correcta implementación del algoritmo restando ambos vectores
# El resultado debe acercarse a cero.

library(R.utils)
rm(list = ls())
cat("\014")

f <- function(x) { 2*x }
N <- 1000
a <- 0
b <- 5

h <- (b-a)/N

alturas <- 0
for (i in 1:N) 
{
 y <- f(a + i*h)
 alturas <- alturas + abs(y)
}

area1 <- alturas * h

area2 <- integrate(f, lower = a, upper = b)$value

print(area1 - area2)


