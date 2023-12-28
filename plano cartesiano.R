#Función que recibe dos puntos de un plano cartesiano y calcula la función distancia

library(R.utils)

calcular_distancia <- function(x1, y1, x2, y2){
  distancia <- sqrt((x2-x1)^2 + (y2-y1)^2)
  return(distancia)
}

x1 <- as.numeric(readline("Introduce x1: "))
y1 <- as.numeric(readline("Introduce y1: "))
x2 <- as.numeric(readline("Introduce x2: "))
y2 <- as.numeric(readline("Introduce y2: "))


distancia <- calcular_distancia(x1, y1, x2, y2)

printf("La distancia entre (%.2f, %.2f) y (%.2f, %.2f) es %.2f\n", x1,y1,x2,y2, distancia)