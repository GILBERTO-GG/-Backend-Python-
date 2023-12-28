
library(R.utils)

sumatoria <- 0
num <- 0

while (sumatoria < 100) {
  num <- as.integer(readline("Introduce un número: "))
  sumatoria <- sumatoria + num
  printf("Num = %d\tSumatoria = %d\n",num,sumatoria)
}