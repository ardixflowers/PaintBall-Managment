from Conexion import *

class CClientes:

    def mostrarClientes():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from usuarios;")
            resultados = cursor.fetchall()
            cone.commit()
            cone.close()
            return resultados

        except mysql.connector.Error as error:
            print("Error al mostrar datos {}".format(error))

    def ingresarClientes(nombres,apellidos,partida,precio,fecha,descripcion):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into usuarios values(null,%s,%s,%s,%s,%s,%s);"
            valores = (nombres,apellidos,partida,precio,fecha,descripcion)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()


        except mysql.connector.Error as error:
            print("Error al ingresar datos {}".format(error))

    def modificarClientes(idUsuario,nombres,apellidos,partida,precio,fecha,descripcion):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "update usuarios set usuarios.nombres = %s, usuarios.apellidos = %s, usuarios.partida = %s, usuarios.precio = %s, usuarios.fecha = %s, usuarios.descripcion = %s Where usuarios.id = %s;"
            valores = (nombres,apellidos,partida,precio,fecha,descripcion,idUsuario)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro modificado")
            cone.close()


        except mysql.connector.Error as error:
            print("Error al modificar datos {}".format(error))

    def eliminarClientes(idUsuario):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "delete from usuarios where usuarios.id = %s;"
            valores = (idUsuario,)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro eliminado")
            cone.close()


        except mysql.connector.Error as error:
            print("Error al modificar datos {}".format(error))