import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from con import traer_clientes  # Asegúrate de que esta función esté disponible en con.py
from ventana_principal import \
    VentanaPrincipal  # Asegúrate de que la clase VentanaPrincipal esté en ventana_principal.py


class ListadoClientes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Listado de clientes")

        # Crear tabla (Treeview) para mostrar clientes
        self.tree = ttk.Treeview(self, columns=("ID", "Nombre", "Apellido", "DNI"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("DNI", text="DNI")
        self.tree.pack(pady=20, padx=20)

        # Llenar la tabla con los datos de los clientes
        self.cargar_clientes()

        # Botón para seleccionar un cliente
        btn_seleccionar = tk.Button(self, text="Seleccionar Cliente", command=self.seleccionar_cliente)
        btn_seleccionar.pack(pady=10)

        # Centrar la ventana principal
        self.centrar_ventana(self)

    def cargar_clientes(self):
        clientes = traer_clientes()
        for cliente in clientes:
            self.tree.insert("", tk.END, values=(cliente['id'], cliente['nombre'], cliente['apellido'], cliente['dni']))

    def seleccionar_cliente(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Debe seleccionar un cliente")
            return

        # Obtener los datos del cliente seleccionado
        cliente = self.tree.item(selected_item)['values']
        id_cliente, nombre, apellido, dni = cliente

        # Abrir VentanaPrincipal y pasar el ID del cliente
        self.abrir_ventana_principal(id_cliente)

    def abrir_ventana_principal(self, id_cliente):
        # Crear instancia de VentanaPrincipal con el ID del cliente
        ventana_principal = VentanaPrincipal(id_cliente)
        ventana_principal.grab_set()  # Esto hace que la ventana principal sea modal (opcional)

        # Mostrar la ventana
        ventana_principal.mainloop()

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)
        ventana.geometry(f'{ancho}x{alto}+{x}+{y}')


# Configuración de la ventana principal
if __name__ == "__main__":
    app = ListadoClientes()
    app.mainloop()
