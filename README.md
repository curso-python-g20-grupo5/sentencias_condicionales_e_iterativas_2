# Sentencias Condicionales e iterativas Parte II
En este repositorio se presenta el desarrollo para la actividad sobre Sentencias Condicionales e Iterativas Parte II.

## Descripción del proyecto

Este repositorio está compuesto por tres archivos: 
  - mayor_a_version1.py: este archivo corresponde a la solución (a) de la actividad 1
  - mayor_a_version2.py: este archivo corresponde a la solución (b) de la actividad 1
  - primeros_auxilios.py: este archivo corresponde a la solución de la actividad 2
  - fuerza_bruta_v1.py: este archivo corresponde a la solución de la actividad 3

## Actividad 1

### Solución (a)
Esta solución se basa solamente ocupando el Ciclo for, la cual nos permite nombrar la variable iteradora de cualquier manera. 
Para ello, nuesto objetivo se basa en poder aplicar el ciclo for a un diccionario. En este sentido, es necesario entender que un diccionario se compone de una clave y un valor, es por eso que la manera más común de iterar diccionarios es utilizando .items().

Entendiendo que el ciclo for para un diccionario se entiende como:
```
for clave, valor in diccionario.items():
```
Para nuestro trabajo ```mes``` corresponderá ```clave``` y ```venta``` corresponderá a ```valor``` y ```diccionario.items()``` se presentará como ```ventas.items()``` puesto que éste corresponde a nuestro diccionario. Por tanto:
```for mes, venta in ventas.items()```


### Solución (b)
Esta solución corresponde a la transformación de un ciclo for a un python comprehension. Basicamente, se sigue manteniendo la estructura de un ciclo for, solo que los elementos que están identados al ciclo se presentan de manera inversa.
Para entenderlo de una forma mucho más didáctica, el código se compone en tres partes: 1) ```clave```: ```valor```; 2) Ciclo for para un diccionario: 3) La condición del código. Esto queda representado de la siguiente manera:

```resultado = {mes: valor for mes, valor in ventas.items() if valor > umbral}```

## Actividad 2

Se nos solicita construir una aplicación interactiva con el usuario que permita indicar los distintos pasos a seguir en tiempo real, dependiendo de su respuesta, ante una emergencia. Esta aplicación debe cumplir con el plan de primeros auxilios que se presenta en el siguiente diagrama:

![Home](imagenes/diagrama-primeros-auxilios.png)

Esto será posible a través de un Ciclo While. Este tipo de ciclo permitirá, en un primer momento, consultar si la persona accidentada responde a estímulos. Dependendiendo de su respuesta la aplicación deberá finalizar el ciclo o continuar con éste en función del plan de primeros auxilios. Un ejemplo de ello es el siguiente: 

```
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
```

Si la persona accidentada responde a estímulos, la aplicación cerrará el ciclo, mediante un ```break```, comunicando al usuario valorar la posibilidad de llevar a la persona accidentada al hospital más cercano. Por el contrario, si la persona no responde a estímulos, la aplicación deberá emitir un mensaje que exprese abir la vía aérea y, en función de ello, consultar si la persona respira o no; dependiendo de su respuesta el programa irá continuando con el ciclo basado en el diagráma de primeros auxilios.

## Actividad 3
Se pide elaborar un programa para determinar cuántos intentos son necesarios para encontrar cominaciones numéricas en minúscula. Por ello, el programa a presentar pide una contraseña al usuario y simula un ataque de fuerza bruta para adivinarla, contando el número de intentos necesarios. Cada intento consiste en comparar cada carácter de la contraseña con todas las letras minúsculas del alfabeto, uno por uno, hasta encontrar una coincidencia.
Ante ello, se presentan los siguientes elementos: 

- Se importa ```ascii_lowercase``` de la biblioteca string, que es una cadena que contiene todas las letras minúsculas del alfabeto inglés: 'abcdefghijklmnopqrstuvwxyz'.
- Función ```fuerza_bruta```: esta función permite adivinar una contraseña mediante un ataque de fuerza bruta. Por consiguiente, ```password``` será el parametro que se busca adivinar.
- La variable ```intentos``` iniciará su contador en 0
- El bucle ```for i, char in enumerate(password):``` itera sobre cada carácter de la contraseña, con ```i``` como el índice y ```char``` como el carácter. 
- El bucle interno ```for c in ascii_lowercase``` itera sobre cada letra del alfabeto minúsculo.
- ```intentos += 1:``` incrementa el contador de intentos en 1 por cada letra que prueba.
- En ```if c == char: break:``` Si la letra ```c``` coincide con el carácter actual ```char``` de la contraseña, se sale del bucle interno.
- ```return intentos:``` devuelve el número total de intentos necesarios para adivinar todos los caracteres de la contraseña.  
- Función ```main``` corresponde a la función principal que ejecuta el programa. Ésta pide al usuario ingresar la contraseña
- Con la variable ```intentos = fuerza_bruta(password):``` se llama a la función ```fuerza_bruta``` con la contraseña ingresada y guarda el número de intentos necesarios para adivinarla.
- Como salida ```print(f"La contraseña fue forzada en {intentos} intentos"):``` imprime el número de intentos necesarios para adivinar la contraseña.
- Ejecución del programa: la condición asegura que ```main``` se ejecuta solo si el archivo se ejecuta directamente.

## Autores y Autoras

- [Rosa Rubio](https://github.com/PaulinaRubioP)
- [Valery Maragaño](https://github.com/Valyxp)
- [Marco Alvarado](https://github.com/7pixel-cl)
- [Esteban Hernández](https://github.com/stivhc)
- [Claudia Aguayo](https://github.com/aguayo40)

⌨️ con ❤️ por el Grupo 5 - G20 😊
