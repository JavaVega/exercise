def conversacion (mensaje):
    print("Hola, Como estas?")
    print("Mi nombre es Jhon")
    print(mensaje)
    print("Adios")

saludo = int(input("Escoge alguna de esas opciones: 1,2,3:\n"))
if saludo == 1:
    conversacion("Escogiste la opcion 1")
elif saludo == 2:
    conversacion("Escogiste la opcion 2")
elif saludo == 3:
    conversacion ("Escogiste la opcion 3")
else:
    ("No elegiste ninguna mensionada")