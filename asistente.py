https://replit.com/join/vjkhqdqwjl-sol-veronicaver

"""
Escribe un programa que detecte si se escribe 'Alexa' en un texto. Si se escribe más de una
vez, el programa debería responder "Tranquilo, solo di mi nombre una vez". Tip: usa las
funciones split() para separar el texto y count() para identificar las veces que dice Alexa
"""

x = input("Escribe el nombre:  ")
y = x.split()
contador = y.count("alexa")
if contador == 1:
    print("Dime, cómo puedo ayudarte?")
elif contador > 1:
    print("Ey, tranquilo, sólo di mi nombre una vez")
  
