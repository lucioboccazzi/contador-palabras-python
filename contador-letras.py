palabra_ingresada = input("Por favor, ingrese una palabra: ")

cantidad_letras = len(palabra_ingresada)

if cantidad_letras == 1:
    print("La cantidad de letras es:", cantidad_letras, "letra.")
else:
    print("La cantidad de letras es:", cantidad_letras, "letras.")