import os
import re
import tkinter
from tkinter import *
from tkinter import messagebox
from turtle import width
from conector import (
    crear_base,
    crear_tabla,
    delete_sqlite,
    insert_sqlite,
    select_sqlite,
    update_sqlite,
    delete_sqlite,
)
from tkinter.ttk import Combobox, Notebook, Treeview, Style
from tkinter import colorchooser
from tkinter.colorchooser import askcolor

### FUNCIONES
def reiniciar_agregar():
    var_mueble_agregar.set("")
    var_color_agregar.set("")
    var_stock_agregar.set("")
    var_precio_agregar.set(0)


def reiniciar_modificar():
    var_stock_modificar.set("")
    var_precio_modificar.set(0)


def agregar():
    global con

    diccionario = {
        "mueble": var_mueble_agregar.get(),
        "color": var_color_agregar.get(),
        "stock": var_stock_agregar.get(),
        "precio": var_precio_agregar.get(),
    }
    insert_sqlite(con, diccionario)
    listar()
    messagebox.showinfo(
    message=f"Mueble agregado",
    title="Confirmación de mueble agregado",
    )
    reiniciar_agregar()


def modificar():
    global con
    try:
        item_viejo = tree.item(var_id_modificar.get())["values"]
    except tkinter.TclError as er:
        print(f"Excepción: {er}")

    diccionario = {
        "stock": var_stock_modificar.get()
        if var_stock_modificar.get() != ""
        else item_viejo[3],
        "precio": var_precio_modificar.get()
        if var_precio_modificar.get() != ""
        else item_viejo[4],
        "id": var_id_modificar.get(),
    }
    update_sqlite(con, diccionario)
    listar()
    messagebox.showinfo(
    message=f"Mueble modificado",
    title="Confirmación de modificación",
    )
    reiniciar_modificar()


def eliminar():
    global con
    diccionario = {"id": var_id_eliminar.get()}
    pregunta = messagebox.askyesno(
        message=f"¿Desea eliminar el mueble {var_id_eliminar.get()}?",
        title="Confirmación eliminar",
    )
    if pregunta:
        delete_sqlite(con, diccionario)
        listar()
        messagebox.showinfo(
    message=f"Mueble eliminado",
    title="Confirmación de eliminar",
    )
        


def listar():
    global con
    for i in tree.get_children():
        tree.delete(i)
    result = select_sqlite(con)
    for dt in result:
        tree.insert("", "end", id=dt[0], values=(dt[0], dt[1], dt[2], dt[3], dt[4]))

def cambiarColor():
    color = colorchooser.askcolor()
    colores = list(color)
    colorHex = colores[1]
    print(colorHex)
    ventana.configure(background=colorHex)

def salir():
    preguntaSalir = messagebox.askyesno(
        message=f"¿Desea salir?",
        title="Confirmación salir del programa",
    )
    if preguntaSalir:
        ventana.destroy()
    
    else:
        print("Me quedo")

def leeme():
    
    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = os.path.join("docx", "test.docx")
    
    os.startfile(ruta)
    print(ruta)


ventana = Tk()
style = Style(ventana)
ventana.title("DDA Muebles")
ventana.geometry("600x480")
ventana.resizable(0, 0)
tree = Treeview(ventana)
book = Notebook(ventana)
book.grid(column=0, row=0, padx=25, pady=10)

frame_agregar = Frame(book, width=950)
frame_modificar = Frame(book, width=950)
frame_eliminar = Frame(book, width=950)

book.add(frame_agregar, text="Agregar")
book.add(frame_modificar, text="Modificar")
book.add(frame_eliminar, text="Eliminar")

######## VARIABLES #############
var_mueble_agregar = StringVar(ventana, "")
var_color_agregar = StringVar(ventana, "")
var_stock_agregar = IntVar(ventana, "")
var_precio_agregar = StringVar(ventana)
var_id_modificar = IntVar(ventana, 0)
var_stock_modificar = StringVar(ventana, "")
var_precio_modificar = StringVar(ventana, "")
var_id_eliminar = IntVar(ventana, 1)

### BOOK AGREGAR
label_mueble_agregar = Label(frame_agregar, text="Mueble: ")
label_mueble_agregar.grid(pady=10, padx=10, row=1, column=0, sticky=E)
entry_mueble_agregar = Entry(frame_agregar, textvariable=var_mueble_agregar)
entry_mueble_agregar.grid(row=1, column=1)

label_color_agregar = Label(frame_agregar, text="Color: ")
label_color_agregar.grid(pady=10, padx=10, row=1, column=2, sticky=E)
entry_color_agregar = Entry(frame_agregar, textvariable=var_color_agregar)
entry_color_agregar.grid(row=1, column=3)

label_stock_agregar = Label(frame_agregar, text="Stock: ")
label_stock_agregar.grid(pady=10, padx=10, row=2, column=0, sticky=E)
entry_stock_agregar = Entry(frame_agregar, textvariable=var_stock_agregar)
entry_stock_agregar.grid(row=2, column=1)

label_precio_agregar = Label(frame_agregar, text="Precio: ")
label_precio_agregar.grid(pady=10, padx=10, row=2, column=2, sticky=E)
entry_precio_agregar = Entry(frame_agregar, textvariable=var_precio_agregar)
entry_precio_agregar.grid(row=2, column=3)

boton_agregar = Button(frame_agregar, text="Agregar", command=agregar)
boton_agregar.grid(row=4, column=3, pady=10, sticky=EW)

### BOOK MODIFICAR

label_id_modificar = Label(frame_modificar, text="ID: ")
label_id_modificar.grid(pady=10, padx=10, row=1, column=0, sticky=E)
entry_id_modificar = Entry(frame_modificar, textvariable=var_id_modificar)
entry_id_modificar.grid(row=1, column=1)

label_stock_modificar = Label(frame_modificar, text="Stock: ")
label_stock_modificar.grid(pady=10, padx=10, row=1, column=2, sticky=E)
entry_stock_modificar = Entry(frame_modificar, textvariable=var_stock_modificar)
entry_stock_modificar.grid(row=1, column=3)

label_precio_modificar = Label(frame_modificar, text="Precio: ")
label_precio_modificar.grid(pady=10, padx=10, row=1, column=4, sticky=E)
entry_precio_modificar = Entry(frame_modificar, textvariable=var_precio_modificar)
entry_precio_modificar.grid(row=1, column=5)

boton_modificar = Button(frame_modificar, text="Modificar", command=modificar)
boton_modificar.grid(row=4, column=3, pady=10, sticky=EW)

### BOOK ELIMINAR

label_id_eliminar = Label(frame_eliminar)
label_id_eliminar.grid(pady=10, padx=135, row=0, column=1)
label_id_eliminar = Label(frame_eliminar, text="ID: ")
label_id_eliminar.grid(pady=10, padx=10, row=0, column=2, sticky=E)
entry_id_eliminar = Entry(frame_eliminar, textvariable=var_id_eliminar)
entry_id_eliminar.grid(row=0, column=3)

boton_eliminar = Button(frame_eliminar, text="Eliminar", command=eliminar)
boton_eliminar.grid(row=2, column=2, pady=10, sticky=EW)

### TREEVIEW
tree.grid(padx=25, pady=15)
tree["columns"] = ("id", "mueble", "color", "stock", "precio")

tree.heading("#0")
tree.heading("id", text="ID")
tree.heading("mueble", text="Mueble")
tree.heading("color", text="Color")
tree.heading("stock", text="Stock")
tree.heading("precio", text="Precio")

tree.column("#0", width=0, stretch=NO)
tree.column("id", width=50, minwidth=50, anchor=CENTER)
tree.column("mueble", width=100, minwidth=100, anchor=CENTER)
tree.column("color", width=100, minwidth=100, anchor=CENTER)
tree.column("stock", width=100, minwidth=100, anchor=CENTER)
tree.column("precio", width=100, minwidth=100, anchor=CENTER)
tree.grid(row=6, column=0, columnspan=5)

boton_cambiarColor = Button(ventana, text="Cambiar Color", command=cambiarColor)
boton_cambiarColor.grid(row=7, columnspan= 5, pady=10, padx=10, sticky=W)

boton_salir = Button(ventana, text="Salir", command=salir)
boton_salir.grid(row=7, columnspan= 5, pady=10, padx=10, sticky=E)

boton_leeme = Button(ventana, text="Léeme", command=leeme)
boton_leeme.grid(row=7, columnspan= 5, pady=10, padx=10, sticky=S)

if os.path.isfile("muebles.db"):
    con = crear_base()
    listar()
else:
    con = crear_base()
    crear_tabla(con)
    listar()

ventana.mainloop()
