def palindromo ():
    palabra = str(input("Escribir la palabra: ").lower().replace(" ",""))
    palabra_invertida = palabra [::-1]
    if palabra == palabra_invertida:
        print("PALINDROMO")
    else:
        print("NO ES PALINDROMO")


if __name__ == "__main__":
    palindromo()