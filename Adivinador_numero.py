from random import randint

#diviertete

intentos = 0
estimado = 0
numero_secreto = randint(1, 100)
nombre = input('Dime tu nombre: ')

print(f"Bueno {nombre} he pensado en un numero del 1 al 100 \n Tienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input('Cual es mi numero?: '))
    intentos += 1

    if estimado not in range(1, 101):
        print('Tu numero no se encuentra en el rango que va desde el 1 al 100 ')
    elif estimado < numero_secreto:
        print('Mi numero es mas alto')
    elif estimado > numero_secreto:
        print('Mi numero es mas bajo')
    else:
        print(f"Felicitaciones {nombre} Has adivinado en {intentos} Intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotados los intentos. El numero secreto era {numero_secreto}")
