#pip install mysql.connector
import mysql.connector # type: ignore

class CConexion:
    
    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user="root",
                                                host="127.0.0.1",
                                                database="clientesdb",
                                                port="3306")
            print("Conexion Correcta")

            return conexion
        
        except mysql.connector.Error as error:
            print("Error al conectarse con la base de datos {}".format(error))

    ConexionBaseDeDatos()