https://replit.com/join/yeqomcnjee-sol-veronicaver

"""
crea un programa que registre los clientes que entran a una tienda y cuántos de ellos
compran varitas. Debe registrar qué clientes compraron qué varitas. Las opciones de varitas
son: 1. Varita de Saúco, 2. Varita de Espino, 3. Varita de Sauce y 4. Varita de Acebo
"""
contador = 0
varita_de_sauco = 0
varita_de_espino = 0
varita_de_sauce = 0
varita_de_acebo = 0

cliente = input("entró algún cliente? conteste con si/no"  )
while cliente == "si":
  contador =+ 1
  cliente = input("entró algún cliente? conteste con si/no  ")
  varita = input("Se vendió alguna varita? conteste con si/no  ")
  if varita == "si":
    print("""
    1. Varita de sauco
    2. Varita de Espino
    3. Varita de Sauce
    4. Varita de acebo
    """)
    tipo_de_varita = int(input("Escoge el número de la varita vendida:  "))
    if tipo_de_varita == 1:
      varita_de_sauco =+ 1
    elif tipo_de_varita == 2:
      varita_de_espino =+ 1
    elif tipo_de_varita == 3:
      varita_de_sauce =+ 1
    elif tipo_de_varita == 4:
      varita_de_acebo += 1
    cliente = input("entró algún cliente? conteste con si/no  ")

print(f"El número de clientes que vinieron hoy fue:{contador}")
print(f"El número de varitas de sauco que se vendieron hoy fue:{varita_de_sauco}")
print(f"El número de varitas de espino que se vendieron hoy fue:{varita_de_espino}")
print(f"El número de varitas de sauce que se vendieron hoy fue:{varita_de_sauce}")
print(f"El número de varitas de acebo que se vendieron hoy fue:{varita_de_acebo}")
