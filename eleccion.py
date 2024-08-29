import tkinter as tk
from ventana_inicio import ventana1  # Asegúrate de que ventana1 esté correctamente importado
from ventana_principal import VentanaPrincipal
from lista_clientes import ListadoClientes

class Ventana3(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Elección")
        self.geometry("300x150")  # Ajusta el tamaño de la ventana según lo necesites
        self.centrar_ventana(300, 150)
        # Crear el botón "Nuevo Cliente"
        self.nuevo_cliente_button = tk.Button(self, text="Nuevo Cliente", command=self.abrir_nuevo_cliente)
        self.nuevo_cliente_button.pack(pady=10)

        # Crear el botón "Cliente Existente"
        self.cliente_existente_button = tk.Button(self, text="Cliente Existente", command=self.abrir_cliente_existente)
        self.cliente_existente_button.pack(pady=10)

    def abrir_nuevo_cliente(self):
        # Instanciar y mostrar ventana1
        ventana1_1 = ventana1()
        self.destroy()  # Cierra la ventana actual
        ventana1_1.mainloop()  # Muestra la nueva ventana

    def abrir_cliente_existente(self):
        lista_clientes_1 = ListadoClientes()
        self.destroy()
        lista_clientes_1.mainloop()

    def centrar_ventana(self, width, height):
        # Obtener el ancho y alto de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular la posición x e y
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Establecer las dimensiones y la posición de la ventana
        self.geometry(f'{width}x{height}+{x}+{y}')


if __name__ == "__main__":
    app = Ventana3()  # Crear una instancia de la clase Ventana3
    app.mainloop()  # Iniciar el bucle principal de la ventana
