def conversor (tipo_peso, valor_dolar):
    pesos = input("Cuantos pesos" + tipo_peso + " tienes?: ")
    pesos = float(pesos)
    cambio = (pesos / valor_dolar)
    cambio = str(round(cambio,21))
    print ("Su moneda a dolares son:" + cambio + " Dolares")

menu = """
Digite que moneda quiere cambiar
 opcion 1 = Pesos Colombianos
 opcion 2 = Pesos Mexicano
 opcion 3 = Pesos Argentinos
"""
opcion = int(input(menu))
if opcion == 1:
   conversor("colombiano", 4500)
elif opcion == 2:
    conversor("Mexicano" , 2000)
elif opcion == 3 : 
    conversor("Argentinos", 500)
else :
    print("Elegiste mal, vuelva a intentarlo")