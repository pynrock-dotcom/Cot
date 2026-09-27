import sqlite3
conexion = sqlite3.connect('Velazcres')
cursorBD = conexion.cursor()

def tableexist(nombreTabla):
    cursorBD.execute('''SELECT COUNT(NAME) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{}' '''.format(nombreTabla))
    if cursorBD.fetchone()[0] == 1:
        return True
    else:
        cursorBD.execute('''CREATE TABLE PRODUCTOENTRY (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE TEXT, PRECIODIVISAS REAL, GANANCIA REAL)''')
    return False

tableexist('PRODUCTO')

def insert(nombre, precio):
    cursorBD.execute('''INSERT INTO PRODUCTO (NOMBRE, PRECIO) VALUES (?,?)''', (nombre, precio))
    conexion.commit()
# insert('20w40', 50)
# insert('mamañema', 50)
# insert('mamacoña', 50)

def select():
    cursorBD.execute('''SELECT * FROM PRODUCTO''')
    X1=[]
    for filaEncontrada in cursorBD.fetchall():
        X1.append(filaEncontrada)
    return X1 


def update(codigo, diccionario):
    VV = ['NOMBRE', 'PRECIO']
    for key in diccionario.keys():
        if key not in VV:
            raise Exception('Esa columna no existe')
        else:
            cursorBD.execute('''UPDATE PRODUCTO SET {} = '{}' WHERE CODIGO = {} '''.format(key, diccionario[key], codigo))
    conexion.commit

def delete(codigo):
    cursorBD.execute('''DELETE FROM PRODUCTO WHERE CODIGO = {} '''.format(codigo))
    conexion.commit()
    