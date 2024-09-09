import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#pip install tkcalendar
import tkcalendar # type: ignore
from tkcalendar import * # type: ignore

from Clientes import *
from Conexion import *

#Define Variables Globales
class FormularioClientes():

    global base
    base = None

    global textBoxId
    textBoxId = None

    global textBoxNombres
    textBoxNombre = None

    global textBoxApellidos
    textBoxApellido = None

    global comboBoxPartida
    comboBoxPartida = None

    global comboBoxPrecio
    comboBoxPrecio = None

    global textBoxFecha
    textBoxFecha = None

    global textBoxDescripcion
    textBoxDescripcion = None

    global groupBox
    groupBox = None

    global tree
    tree = None


#Vista
def Formulario():
    global base

    global textBoxId
    global textBoxNombres
    global textBoxApellidos
    global comboBoxPartida
    global comboBoxPrecio
    global textBoxFecha
    global textBoxDescripcion

    global groupBox
    global tree


    try:
        base = Tk()
        base.geometry("1200x350")
        base.title("PaintBall")
        base.iconbitmap(r"PaintBall.ico")


        #Panel De Orden Izquierdo
        groupBox = LabelFrame(base,text="Datos del Usuario",padx=5,pady=5)
        groupBox.grid(row=0,column=0,padx=10,pady=10)

        labelId=Label(groupBox,text="Id:",width=13,font=("arial",12)).grid(row=0,column=0)
        textBoxId = Entry(groupBox,width=17)
        textBoxId.grid(row=0,column=1)

        labelNombres=Label(groupBox,text="Nombres:",width=13,font=("arial",12)).grid(row=1,column=0)
        textBoxNombres = Entry(groupBox,width=17)
        textBoxNombres.grid(row=1,column=1)

        labelApellidos=Label(groupBox,text="Apellidos:",width=13,font=("arial",12)).grid(row=2,column=0)
        textBoxApellidos = Entry(groupBox,width=17)
        textBoxApellidos.grid(row=2,column=1)

        labelPartida=Label(groupBox,text="Partida:",width=13,font=("arial",12)).grid(row=3,column=0)
        seleccionPartida = tk.StringVar()
        comboBoxPartida = ttk.Combobox(groupBox,values=["Comun", "Profesional"],textvariable=seleccionPartida,width=14)
        comboBoxPartida.grid(row=3,column=1)
        seleccionPartida.set("Comun")

        labelPrecio=Label(groupBox,text="Precio:",width=13,font=("arial",12)).grid(row=4,column=0)
        seleccionPrecio = tk.StringVar()
        comboBoxPrecio = ttk.Combobox(groupBox,values=["100", "200"],textvariable=seleccionPrecio,width=14)
        comboBoxPrecio.grid(row=4,column=1)
        if seleccionPartida.get() == "Comun":
            seleccionPrecio.set("100")
        if seleccionPartida.get() == "Profesional":
            seleccionPrecio.set("200")

        labelFecha=Label(groupBox,text="Fecha:",width=13,font=("arial",12)).grid(row=5,column=0)
        textBoxFecha = DateEntry(groupBox,width=14) # type: ignore
        textBoxFecha.grid(row=5,column=1)

        labelDescripcion=Label(groupBox,text="Descripcion:",width=13,font=("arial",12)).grid(row=6,column=0)
        textBoxDescripcion = Text(groupBox,width=17,height=5,font=("arial",12))
        textBoxDescripcion.grid(row=6,column=1)


        Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=7,column=0)
        Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=7,column=1)
        Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=7,column=2)


        #Segundo Grupo De Comando
        groupBox = LabelFrame(base,text="Lista de Registros",padx=5,pady=5,)
        groupBox.grid(row=0,column=1,padx=10,pady=10)

        tree = ttk.Treeview(groupBox,columns=("Id","Nombre","Apellido","Partida","Precio","Fecha","Descripcion"),show="headings",height=11,)
        tree.column("# 1",width=30,anchor=CENTER)
        tree.heading("# 1",text="Id")
        tree.column("# 2",width=95,anchor=CENTER)
        tree.heading("# 2",text="Nombre")
        tree.column("# 3",width=95,anchor=CENTER)
        tree.heading("# 3",text="Apellido")
        tree.column("# 4",width=95,anchor=CENTER)
        tree.heading("# 4",text="Partida")
        tree.column("# 5",width=70,anchor=CENTER)
        tree.heading("# 5",text="Precio")
        tree.column("# 6",width=80,anchor=CENTER)
        tree.heading("# 6",text="Fecha")
        tree.column("# 7",width=300,anchor=CENTER)
        tree.heading("# 7",text="Descripcion")

        #aca se agregan los valores a la tabla y la muestra
        for row in CClientes.mostrarClientes():
            tree.insert("","end",values=row)

        #Ejecuta la funcion de hacer click y muestra el resultado de los Entry
        tree.bind("<<TreeviewSelect>>",seleccionarRegistro)

        tree.pack()

        base.mainloop()


    except ValueError as error:
        print("Error al mostrar la interfaz, error: {}".format(error))




def actualizarTreeWiev():
    global tree

    try:
        #Se borran todos los valores menos las cabeceras y volvemos a dar los valores
        tree.delete(*tree.get_children())
        datos = CClientes.mostrarClientes()

        #Agrega todos los valores a la tabla nuevamenete ya actualizados
        for row in CClientes.mostrarClientes():
            tree.insert("","end",values=row)

    except ValueError as error:
        print("Error al actualizar tabla {}".format(error))




def seleccionarRegistro(event):
    try:
        itemSeleccionado = tree.focus()

        if itemSeleccionado:
            #obtiene el valor de la comlumna
            values = tree.item(itemSeleccionado)["values"]
            
            #Establece los valores en los widgets Entry
            textBoxId.delete(0,END)
            textBoxId.insert(0,values[0])
            textBoxNombres.delete(0,END)
            textBoxNombres.insert(0,values[1])
            textBoxApellidos.delete(0,END)
            textBoxApellidos.insert(0,values[2])
            comboBoxPartida.set(values[3])
            comboBoxPrecio.set(values[4])
            textBoxFecha.delete(0,END)
            textBoxFecha.insert(0,values[5])
            textBoxDescripcion.delete("1.0","end-1c")
            textBoxDescripcion.insert("1.0",values[6])
    
    except ValueError as error:
        print("error al seleccionar el registro {}".format(error))




def guardarRegistros():

    global textBoxNombres,textBoxApellidos,comboBoxPartida,comboBoxPrecio,textBoxFecha,textBoxDescripcion,groupBox

    try:
        #Verifica
        if textBoxNombres is None or textBoxApellidos is None or comboBoxPartida is None or comboBoxPrecio is None or textBoxFecha is None or textBoxDescripcion is None:
            print("Los Widgets no estan inicializados")
            return


    
        nombres = textBoxNombres.get()
        apellidos = textBoxApellidos.get()
        partida = comboBoxPartida.get()
        precio = comboBoxPrecio.get()
        fecha = textBoxFecha.get_date()
        descripcion = textBoxDescripcion.get("1.0","end-1c")

        CClientes.ingresarClientes(nombres,apellidos,partida,precio,fecha,descripcion)
        messagebox.showinfo("Información","Los Datos Fueron Guardados")

        actualizarTreeWiev()

        textBoxNombres.delete(0,END)
        textBoxApellidos.delete(0,END)
        textBoxFecha.delete(0,END)
        textBoxDescripcion.delete("1.0","end-1c")


    except ValueError as error:
        print("Error al ingresar los datos {}".format(error))




def modificarRegistros():

    global textBoxId,textBoxNombres,textBoxApellidos,comboBoxPartida,comboBoxPrecio,textBoxFecha,textBoxDescripcion,groupBox

    try:
        #Verifica
        if textBoxId is None or textBoxNombres is None or textBoxApellidos is None or comboBoxPartida is None or comboBoxPrecio is None or textBoxFecha is None or textBoxDescripcion is None:
            print("Los widgets no estan inicializados")
            return

        idUsuario = textBoxId.get()
        nombres = textBoxNombres.get()
        apellidos = textBoxApellidos.get()
        partida = comboBoxPartida.get()
        precio = comboBoxPrecio.get()
        fecha = textBoxFecha.get_date()
        descripcion = textBoxDescripcion.get("1.0","end-1c")

        CClientes.modificarClientes(idUsuario,nombres,apellidos,partida,precio,fecha,descripcion)
        messagebox.showinfo("Información","Los datos fueron modificados")

        actualizarTreeWiev()

        textBoxId.delete(0,END)
        textBoxNombres.delete(0,END)
        textBoxApellidos.delete(0,END)
        textBoxFecha.delete(0,END)
        textBoxDescripcion.delete("1.0","end-1c")


    except ValueError as error:
        print("Error al modificar los datos {}".format(error))




def eliminarRegistros():

    global textBoxId,textBoxNombres,textBoxApellidos,comboBoxPrecio,textBoxFecha,textBoxDescripcion

    try:
        #Verifica
        if textBoxId is None:
            print("Los Widgets no estan inicializados")
            return

        idUsuario = textBoxId.get()

        CClientes.eliminarClientes(idUsuario)
        messagebox.showinfo("Información","Los datos fueron eliminados")

        actualizarTreeWiev()

        textBoxId.delete(0,END)
        textBoxNombres.delete(0,END)
        textBoxApellidos.delete(0,END)
        textBoxFecha.delete(0,END)
        textBoxDescripcion.delete("1.0","end-1c")


    except ValueError as error:
        print("Error al modificar los datos {}".format(error))


Formulario()