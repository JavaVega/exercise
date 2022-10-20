"""EJERCICIOS ESTRUCTURADOS"""
def ejercicio_1():
    """Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!."""
    print ("¡Hola Mundo!")

def ejercicio_2():
    """Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable."""
    mundo = "¡Hola Mundo!"
    print (mundo) 

def ejercicio_3():
    """Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido."""
    mundo = "¡Hola"
    nombre = input("Como se llama?: ")
    print(mundo + " " + nombre + "!") 

def ejercicio_4():
    """Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido."""
    nombre = input ("What is your name?: ")
    numero = int(input ("Digitar las veces que quiere imprimir: "))
    operacion = nombre  *  numero
    print (operacion)

def ejercicio_5():
    """Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre."""
    nombre = input("What is your name?: ")
    print("Su nombre en Mayuscula es: " + nombre.upper() + " tiene :" + str(len(nombre.replace(" ",""))) + " Caracteres")
    print("La letra r se repite en su nombre es: " + str(nombre.count('r')))

def ejercicio_6():
    """Escribir un programa que realice la siguiente operación aritmética  (3+2/2.5)2 """
    aritmetica = ((3+2)/(2.5))**2
    print(aritmetica)
    return aritmetica

def ejercicio_7():
    """Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde."""

def ejercicio_8():
    """Escribir un programa que lea un entero positivo, [Math Processing Error], introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta [Math Processing Error]. La suma de los suma=𝑛(𝑛+1)/2 primeros enteros positivos puede ser calculada de la siguiente forma:
    """

def ejercicio_9():
    """Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
    """

def ejercicio_10():
    """Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
    """

def ejercicio_11():
    """Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión."""

def ejercicio_12():
    """Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado."""

def ejercicio_13():
    """Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales."""

def ejercicio_14():
    """Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total. """

if __name__ == "__main__":
   pass 