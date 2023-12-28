#Programe en R que genere 10 muestras usando las distribuciones uniforme, normal
# y binomial

rm(list = ls())
cat("\014")

print("Números aleatorios no repetidos con runif")
A <- runif(10, min = -10, max = 10)
B <- runif(10, min = -10, max = 10)
print(A)
print(B)

print("Números aleatorios no repetidos con rnorm")
A <- rnorm(10, mean = 5, sd = 1)
B <- rnorm(10, mean = 5, sd = 1)
print(A)
print(B)

print("Números aleatorios no repetidos con rbinom")
A <- rbinom(10, size = 100, prob = 0.5)
B <- rbinom(10, size = 100, prob = 0.5)
print(A)
print(B)

print("Números aleatorios repetidos con runif")
set.seed(10);  A <-  runif(10, min = -10, max = 10)
set.seed(10);  B <-  runif(10, min = -10, max = 10)
print(A)
print(B)

print("Números aleatorios repetidos con rnorm")
set.seed(10);  A <-  rnorm(10, mean = 5, sd = 1)
set.seed(10);  B <-  rnorm(10, mean = 5, sd = 1)
print(A)
print(B)

print("Números aleatorios repetidos con rbinom")
set.seed(10);  A <-  rbinom(10, size = 100, prob = 0.5)
set.seed(10);  B <-  rbinom(10, size = 100, prob = 0.5)
print(A)
print(B)

