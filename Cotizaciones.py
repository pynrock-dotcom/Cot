import database
import newprod

insert = newprod.new
dbinsert = database.insert
dbshow = database.select
dbupdate = database.update
dbdelete = database.delete

def main():
    while True:
        print("1. Añadir")
        print("2. Mostrar")
        print("3. Eliminar")
        Op=int(input(""))
            
        if Op == 1:
            insert()
        elif Op == 2:
            print(dbshow())
            input("presiona enter para continuar ")
        elif Op == 3:
            d=input("Ingrese el codigo del producto a eliminar ")
            dbdelete(d)
            input("El producto se eliminó correctamente, presione enter para continuar ")
        elif Op == 5:
            pass
            break

main()