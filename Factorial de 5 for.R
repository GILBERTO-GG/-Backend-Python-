library(R.utils)

factorial <- 1
contador <- 1

for (contador in 1:5) {
  factorial <- factorial * contador
  printf("Contador = %d\tFactorial = %d\n", contador, factorial)
}