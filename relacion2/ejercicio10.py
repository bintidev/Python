'''Escribe un programa que a partir de información de un donante determine si
puede donar sangre. Las condiciones para donar son:
a. No se debe donar en ayunas.
b. Edad: Comprendida entre los 18 y 65 años.
c. Peso: Superior a 50kg.
d. Tensión arterial: dentro de límites adecuados para la extracción.
i. Tensión diastólica (baja): entre 50mm Hg y 100 mm Hg
ii. Tensión sistólica (alta): entre 90mm y 180mm Hg
e. Pulso (frecuencia cardiaca): entre 50 y 110 pulsaciones
f. Valores de hemoglobina:
i. En hombres: superior a 13,5 gramos por litro
ii. En mujeres: superior a 12,5 gramos por litro.
g. Plaquetas: más de 150.000 cc
h. Proteínas totales: más de 6 gr/dl.'''

print ("#######################################################\n")
print ("\t     PROGRAMA DE DONACIÓN DE SANGRE \n")
print ("\tComprobación de cumplimiento de requisitos \n")
print ("########################################################\n")

enAyunas = str(input("¿Se encuentra en estado de ayunas? ")).lower()


if (enAyunas != "si"): # evalúa la próxima condición si no está en ayunas
    sexo = str(input("Sexo: Hombre (H)  o   Mujer (M) ")).lower() # para validación de nivel de hemoglobina más adelante
    edad = int(input("Edad: "))

    if (edad >= 18 and edad < 65): # evalúa la próxima condición si está dentro del rango de edad [18,65)
        peso = float(input("Introduzca su peso: "))

        if (peso > 50): # evalúa la próxima condición si pesa más de 50kg
            tensionD = int(input("Tensión diastólica (baja): "))

            if ((tensionD > 50) and (tensionD < 100)): # evalúa la próxima condición si la tensión baja está en el rango (50, 100)
                tensionS = int(input("Tensión sistólica (sistólica): "))
            
                if ((tensionS > 90) and (tensionS < 180)): # evalúa la próxima condición si la tensión alta está en el rango (90, 180)
                    pulsaciones = int(input("Frecuencia cardíaca: "))

                    if ((pulsaciones > 50) and (pulsaciones < 110)): # evalúa la próxima condición si las pulsaciones están en el rango (50, 110)
                        hemoglobina = float(input("Nivel de sangre: "))

                        # evalúa la próxima condición si: es hombre y el nivel de hemoglobina/litro supera los 13.5; si es mujer y el nivel de hemoglobina/litro supera los 12.5
                        if ((sexo == 'h' and hemoglobina > 13.5) or (sexo == 'm' and hemoglobina > 12.5)):
                            plaquetas = float(input("Plaquetas: "))

                            # evalúa la próxima condición si la cantidad de plaquetas por centímetro cúbico supera los 150
                            if (plaquetas > 150.00):
                                proteinas = float(input("Proteínas: "))

                                if (proteinas > 6): # es apto para donar si cumple con la última condición de 6gr de proteína por decilitro
                                    print ("Cumple con todos los requisitos para donar sangre.")

                                # ramas alternativas en caso de que alguna condición no se cumpliera
                                else:
                                    print ("No se puede donar con un peso menor de 6 gramos/dL.")

                            else:
                                print ("No se puede donar con un nivel de plaquetas menor o igual a los 150,00cc.")

                        else:
                            print ("El mínimo de hemoglobina por litro debe ser: para hombres 13,5 y para mujeres 12,5.")

                    else:
                        print ("No se puede donar con pulsaciones fuera del rango 50-110.")

                else:
                    print ("No se puede donar con una tensión sistólica fuera del rango 90-80mm Hg.")

            else:
                print ("No se puede donar con tensión diastólica fuera del rango 50-100mm Hg.")

        else:
            print ("No se permite la donación a aquellxs personas por debajo de los 51kg.")    

    else:
        print ("No se permite donar a aquellxs menores de 18 años, ni a mayores de 65 años.")
    
else:
    print ("No está permitida la donación de sangre en ayunas.")
