library(R.utils)

rm(list = ls())
cat("\014")

libro <- list(Autor = "Baldor, Aurelio", Titulo = "Álgebra", Editorial = "Patria", Edicion
              = "4", Fecha = "2019", ISBN13 = "9786075502090", Precio = 410)

printf("Autor:\t\t%s\n", libro$Autor)
printf("Título:\t\t%s\n", libro[2])
printf("Editorial:\t\t%s\n", libro$Editorial)
printf("Edición:\t\t%s\n", libro[4])
printf("Fecha:\t\t%s\n", libro$Fecha)
printf("ISBN13:\t\t%s\n", libro[6])
printf("Precio:\t\t%s\n", libro$Precio)