#Actividad 1 - Filtrado compacto

#Utilizamos la libreria sys.argv para que el usuario pueda ingresar el umbral de ventas en el terminal
import sys

#Solicitar umbral de ventas al usuario
umbral = int(sys.argv[1])

#Una empresa provee de los balances del año anterior en un diccionario como se muestra a continuación
ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

#Retornar un diccionario con el mes y el valor asociado solo cuando se supere el umbral especificado
supera_umbral = {}

#Si la condición se cumple, el mes y el valor asociados retornan a un diccionaro que expresa los meses que superan el umbral de ventas
#En donde mes corresponde a Clave
#En donde venta corresponde a Valor
for mes, venta in ventas.items():
    if venta > umbral:
        supera_umbral[mes] = venta
print(f"Meses con ventas superiores al umbral de ventas ingresado {supera_umbral}")



