library(R.utils)

rm(list = ls())
cat("\014")

vector <- c(-5.4, -3.2, -1.0, 1.2, 3.4, 5.6, 7.8)

print(vector)

for(i in 1:length(vector)){
  printf("vector[%d] = %.2f\n", vector[i])
}
#printf("vector[1] = %.2f\n", vector[1])
#printf("vector[2] = %.2f\n", vector[2])
#printf("vector[3] = %.2f\n", vector[3])
#printf("vector[4] = %.2f\n", vector[4])
#printf("vector[5] = %.2f\n", vector[5])
#printf("vector[6] = %.2f\n", vector[6])
#printf("vector[7] = %.2f\n", vector[7])