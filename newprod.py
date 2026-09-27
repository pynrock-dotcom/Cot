import database
insert = database.insert

def new():
    while True:
        name = str(input("Ingresa el Nombre del Producto\n> "))
        print()
        pay = float(input("Ingrese el Precio del Producto por Unidad\n> "))
        print()
        cup = float(input("Ingrese la Tasa a la que Pagó el Producto\n> "))
        print()
        perc = float(input("Ingrese el Porcentaje de Ganancia Deseado en %"))
        
        precioventa = pay * ((perc / 100) + 1)
        
        insert(name, pay, cup, perc, precioventa)
        close = input("Allgood break? Y/n")
        if close == "Y" or close == "y" :
            break 
