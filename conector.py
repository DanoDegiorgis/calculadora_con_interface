import sqlite3


def crear_base():
    con = sqlite3.connect("DDA Muebles.db")
    return con


def crear_tabla(con):
    con = sqlite3.connect("DDA Muebles.db")
    cursor = con.cursor()
    sql = "CREATE TABLE IF NOT EXISTS muebles(id integer PRIMARY KEY AUTOINCREMENT, mueble VARCHAR, color VARCHAR, stock INTVAR NOT NULL, precio INTVAR NOT NULL)"
    try:
        cursor.execute(sql)
        con.commit()
    except sqlite3.Error as er:
        print(f"Excepción: {er}")


def insert_sqlite(con, dic):
    cursor = con.cursor()
    data = (dic["mueble"], dic["color"], dic["stock"], dic["precio"])
    sql = "INSERT INTO muebles(mueble, color, stock, precio) VALUES(?, ?, ?, ?)"
    try:
        cursor.execute(sql, data)
        con.commit()
    except sqlite3.Error as er:
        print(f"Excepción: {er}")


def update_sqlite(con, dic):
    cursor = con.cursor()
    data = (dic["stock"], dic["precio"], dic["id"])
    sql = "UPDATE muebles SET stock = ?, precio = ? WHERE id = ?"
    try:
        cursor.execute(sql, data)
        con.commit()
    except sqlite3.Error as er:
        print(f"Excepción: {er}")


def delete_sqlite(con, dic):
    cursor = con.cursor()
    data = (dic["id"],)
    sql = "DELETE FROM muebles WHERE id = ?"
    try:
        cursor.execute(sql, data)
        con.commit()
    except sqlite3.Error as er:
        print(f"Excepción: {er}")


def select_sqlite(con):
    cursor = con.cursor()
    sql = "SELECT * FROM muebles"
    try:
        result = cursor.execute(sql)
        con.commit()
    except sqlite3.Error as er:
        print(f"Excepción: {er}")
    return result
