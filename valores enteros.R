library(R.utils)

sumatoria <- 0

for(contador in 1:100){
  sumatoria <- sumatoria + contador
  printf("Contador = %d\tSumatoria = %d\n", contador, sumatoria)
}