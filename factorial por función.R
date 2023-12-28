# calcula el factorial de un número definido por el usuario

library(R.utils)

calcular_factorial <- function(x){
  y <- 1
  contador <- 1
  
  for (contador in 1:x) {
    y <- y*contador
  }
  
  return(y)
}

N <- as.numeric(readline("Introduce N: "))

y <- calcular_factorial(N)

printf("Factorial de %.2f es %.2f", N,y)