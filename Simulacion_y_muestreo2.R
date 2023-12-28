#programa en R que genere un vector entre [-5,5], seleccione siempre 5 muestras sin
# reemplazo

rm(list = ls())
cat("\014")

X <- -5:5

Y <- sample(X, 5, replace = FALSE)
print(Y)

Y <- sample(X, 5, replace = TRUE)
print(Y)

