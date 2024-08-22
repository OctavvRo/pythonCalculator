import tkinter as tk
from ventana_principal import VentanaPrincipal

class ventana1(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Pantalla de inicio")

        # Llamada para centrar la ventana
        self.centrar_ventana(400, 270)  # Puedes ajustar el tamaño de la ventana aquí

        form_cliente = tk.Frame(self)
        form_cliente.pack(padx=10, pady=10, fill="both", expand=True)

        # Centrar los widgets dentro del Frame
        form_cliente.grid_columnconfigure(0, weight=1)
        form_cliente.grid_columnconfigure(1, weight=1)

        # Agrega el título y alinéalo al centro
        label_titulo = tk.Label(form_cliente, text="Formulario datos cliente", font=("Arial", 14, "bold"))
        label_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

        # Configurar la columna para que ocupe todo el ancho disponible
        form_cliente.grid_columnconfigure(0, weight=1)
        form_cliente.grid_columnconfigure(1, weight=1)

        label_nombre = tk.Label(form_cliente, text="Nombre:")
        label_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="e")  # 'e' alinea a la derecha dentro de la celda

        self.entry_nombre = tk.Entry(form_cliente)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="w")  # 'w' alinea a la izquierda dentro de la celda

        label_apellido = tk.Label(form_cliente, text="Apellido:")
        label_apellido.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_apellido = tk.Entry(form_cliente)
        self.entry_apellido.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        label_dni = tk.Label(form_cliente, text="DNI:")
        label_dni.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.entry_dni = tk.Entry(form_cliente)
        self.entry_dni.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Botón para enviar el formulario
        button_submit = tk.Button(form_cliente, text="Enviar", command=self.abrir_ventana_principal)
        button_submit.grid(row=4, column=0, columnspan=2, pady=20)

    def centrar_ventana(self, width, height):
        # Obtener el ancho y alto de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular la posición x e y
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Establecer las dimensiones y la posición de la ventana
        self.geometry(f'{width}x{height}+{x}+{y}')

    def abrir_ventana_principal(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        dni = self.entry_dni.get()

        # Crear y mostrar VentanaPrincipal, pasándole los datos
        ventana_principal = VentanaPrincipal(nombre, apellido, dni)
        self.destroy()
        ventana_principal.mainloop()

if __name__ == "__main__":
    app = ventana1()  # Creas una instancia de la clase ventana1
    app.mainloop()    # Inicias el bucle principal de la ventana
