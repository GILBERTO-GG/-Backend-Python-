library(R.utils)

area_cuadrado <- function(lado){
  area <- lado**2
  return(area)
}

lado <- as.numeric(readline("Introduce lado: "))
area <- area_cuadrado(lado)

printf("El area del cuadrado es: %.2f\n", area)