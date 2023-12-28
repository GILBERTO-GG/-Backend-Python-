library(R.utils)

rm(list = ls())
cat("\014")

inicio <- 2
fin <- 100
paso <- 2


vector <- seq(from = inicio, to = fin, by = paso)

for(i in 1:length(vector)){
  printf("vector[%d] = %d\n", i, vector[i])
}