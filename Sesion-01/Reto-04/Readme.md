agrega el programa que se desarrollara con backticks> [agrega la sesion con backticks] 
	
## Precio de helado con descuento
### OBJETIVO 

- Harás uso de condicionales para calcular el precio de un helado

#### REQUISITOS 

1. Python 3

#### DESARROLLO

Escribe un programa que devuelva el precio de un helado solicitado por el cliente de acuerdo al topping:

1. Helado con oreo: $19
2. Helado con m&m: $25
3. Helado con fresas: $22
4. Helado con brownie: $28

En caso de introducir otro topping, se le debe decir al cliente que el producto no esta disponible

<details>
	Solución

	print("Qué topping quieres en tu helado?")
	topping = input()

	if topping == "oreo":
		precio = 19
	elif topping == "m&m":
		precio = 25
	elif topping == "fresas":
		precio = 22
	elif topping  == "brownie":
		precio = 28
	else:
		print("producto no disponible")

	print("El precio es ${}".format(precio))
</details> 



