import mysql.connector
from tkinter import messagebox

# Configuración de la conexión
def con_db():
    return mysql.connector.connect(
        host="localhost",
        user="octa",
        password="octa",
        database="base_datos"
    )

def agregar_cliente(nombre, apellido, dni):
    if nombre and apellido and dni:
        try:
            con = con_db()
            cursor = con.cursor()

            consulta = "INSERT INTO clientes (nombre, apellido, dni) VALUES (%s, %s, %s)"
            valores = (nombre, apellido, dni)

            cursor.execute(consulta, valores)
            con.commit()

            messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
            return True
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo agregar el cliente: {error}")
        finally:
            cursor.close()
            con.close()
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

def traer_clientes():
    try:
        con = con_db()
        cursor = con.cursor(dictionary=True)

        consulta = "SELECT id, nombre, apellido, dni FROM clientes"
        cursor.execute(consulta)

        clientes = cursor.fetchall()
        return clientes
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo traer los clientes: {error}")
        return []
    finally:
        cursor.close()
        con.close()

def obtener_cliente_por_id(id_cliente):
    if id_cliente:
        try:
            con = con_db()
            cursor = con.cursor(dictionary=True)

            consulta = "SELECT id, nombre, apellido, dni FROM clientes WHERE id = %s"
            cursor.execute(consulta, (id_cliente,))

            cliente = cursor.fetchone()
            return cliente
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo obtener el cliente: {error}")
            return None
        finally:
            cursor.close()
            con.close()
    else:
        messagebox.showwarning("Advertencia", "El ID del cliente es obligatorio.")
        return None

def traer_registros(id_cliente):
    if id_cliente:
        try:
            con = con_db()
            cursor = con.cursor(dictionary=True)  # Usamos dictionary=True para obtener los resultados como diccionarios

            consulta = "SELECT * FROM registros WHERE id_cliente = %s"
            cursor.execute(consulta, (id_cliente,))

            registros = cursor.fetchall()
            return registros
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo traer los registros: {error}")
            return []
        finally:
            cursor.close()
            con.close()
    else:
        messagebox.showwarning("Advertencia", "El ID del cliente es obligatorio.")
        return []
