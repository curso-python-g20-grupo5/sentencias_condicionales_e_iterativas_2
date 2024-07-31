# fuerza_bruta_v1.py
# se solicita un programa llamado fuerza bruta para poder determinar cuantos intentos se necesitan para lograr hackear la contraseña

from string import ascii_lowercase
# esta función intenta adivinar una contraseña usando fuerza_bruta que toma como entrada el passwordlo que entrega la cantidad de números necesarios para hackear la contraseña
def fuerza_bruta(password):
    intentos = 0 # aquí se inicia el contador de intentos
    # el siguiente ciclo for busca iterar cada carácter de la contraseña  
    for i, char in enumerate(password):
        # el siguiente ciclo for recorre las letras del abecedario alfabeto en minúscula
        for c in ascii_lowercase:
            # se incrementa el contador de intento por cada letra probada
            intentos += 1
            # si la letra que se prueba coincide con el carácter de la contraseña se finaliza el ciclo
            if c == char:
                break
    return intentos #queremos que se devuelva el total de intentos

def main(): 
    # esta corresponde a la función principal del programa
    # se solicita al usuario que ingrese una contraseña y, a su vez, calcular los intentos necesarios para forzar esa contraseña
    password = input("Ingrese la contraseña: ")
    intentos = fuerza_bruta(password)
    print(f"La contraseña fue forzada en {intentos} intentos")

if __name__ == "__main__": # punto de entrada del script
    main()
