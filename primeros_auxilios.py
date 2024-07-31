"""
Se requiere la construcción de una aplicación interactiva primeros_auxilios.py que
entregue los distintos pasos a seguir dependiendo de las respuestas que el usuario entrega
en tiempo real.
"""
#Creación ciclo while para consultar si paciente responde estímulos
while True: 
    #creacion de variable paciente 
    paciente= input('¿El paciente responde a estímulos?: ').lower()#input con funcion lower.() para asegurar entrada de texto en minusculas
    if paciente != "si" and paciente != "no":
        print("ingresa respuesta si o no")
    else:
        if paciente == "si":
            print("Valorar la posibilidad de llevarlo al hospital más cercano")
            break #utilizacion de break para dar fin al ciclo con esta respuesta
        else:
            paciente = input("Abrir la vía aérea. ¿Respira? (si/no): ").lower()#input con funcion lower.() para asegurar entrada de texto en minusculas
            if paciente != "si" and paciente != "no":
                print("ingresa respuesta si o no")
            else:
                if paciente == "si":
                    print("Permitirle posición de suficiente ventilación")
                    break #utilizacion de break para dar fin al ciclo con esta respuesta
                else:   
                    print("Admininstrar 5 ventilaciones y llamar a ambulancia")

                    #Creación ciclo while para consultar si paciente presenta signos de vida
                    while True:
                        #creacion de variable signos de vida
                        signos_de_vida = input("¿Hay signos de vida? (si/no): ").lower()#input con funcion lower.() para asegurar entrada de texto en minusculas
                        if signos_de_vida!= "si" and signos_de_vida != "no":
                            print("ingresa respuesta si o no")
                        else:
                            if signos_de_vida == "si":
                                print("Reevaluar a la espera de la ambulancia")

                            elif signos_de_vida == "no":
                                print("Administrar compresiones torácicas hasta que llegue la ambulancia")

                            #creacion de variable ambulancia
                            ambulancia_llego = input("¿Llegó la ambulancia? (si/no): ").lower()#input con funcion lower.() para asegurar entrada de texto en minusculas
                            if ambulancia_llego!= "si" and ambulancia_llego != "no":
                                print("ingresa respuesta si o no")
                            else:
                                if ambulancia_llego == "si":
                                    print("Fin del ciclo. La ambulancia ha llegado.")
                                    break #utilizacion de break para dar fin al ciclo con esta respuesta

                                elif ambulancia_llego != "no":
                                    print("Respuesta no válida. Por favor, responde con 'si' o 'no'.")
                    break
                       
                                

                    
                        
                

