import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry  # Importar DateEntry de tkcalendar

class VentanaPrincipal(tk.Tk):

    def __init__(self, nombre, apellido, dni):
        super().__init__()
        self.title("Ventana Principal")

        # Llamada para centrar la ventana
        self.centrar_ventana(1200, 400)  # Ajusta el tamaño de la ventana según lo necesites

        # Crear el frame para mostrar datos
        self.info_frame = tk.Frame(self, bg="lightgrey", padx=10, pady=10)
        self.info_frame.pack(padx=10, pady=10, fill="x", side="top")

        # Mostrar los datos recibidos en el frame, uno al lado del otro
        tk.Label(self.info_frame, text="Datos del cliente ", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=2, sticky='w')
        tk.Label(self.info_frame, text=f"Nombre: {nombre} {apellido}", font=("Arial", 12)).grid(row=0, column=1, padx=5, pady=2, sticky="w")
        tk.Label(self.info_frame, text=f"DNI: {dni}", font=("Arial", 12)).grid(row=0, column=3, padx=5, pady=2, sticky="w")

        # Crear el frame para el formulario
        form_frame = tk.Frame(self)
        form_frame.pack(padx=10, pady=10, fill="both", expand=True, side="left")

        # Crear el formulario
        tk.Label(form_frame, text="Empresa:").grid(row=0, column=0, padx=10, pady=10)
        self.empresa_entry = tk.Entry(form_frame)
        self.empresa_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Desde:").grid(row=1, column=0, padx=10, pady=10)
        self.desde_entry = DateEntry(form_frame, date_pattern='yyyy-mm-dd')  # Usar DateEntry para la fecha "Desde"
        self.desde_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Hasta:").grid(row=2, column=0, padx=10, pady=10)
        self.hasta_entry = DateEntry(form_frame, date_pattern='yyyy-mm-dd')  # Usar DateEntry para la fecha "Hasta"
        self.hasta_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Régimen Previsional:").grid(row=3, column=0, padx=18, pady=5)
        self.tipo_trabajo = ttk.Combobox(form_frame, values=["Construcción", "Civil", "Aceria/Forja", "Aviación","Carne","Ceguera","Chofer Tr. Carga Aut.", "Chofer T Carga RD","Chofer Taxista","Electricidad","Embarcadero","Estibador","Futbolista Prof.", "Gas/Petroleo","Malvinas", "Mineria/ Forja y Fragua", "Panadero, Arriero, Refineria","Peon Rural","Portuario","Telefonista","Telegrafo","Temporario Veraneio","Trato de enfermedades","Vidrio"], )
        self.tipo_trabajo.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(form_frame, text="Agregar", command=self.on_agregar).grid(row=4, column=1, padx=20, pady=5)

        # Crear el frame para la tabla
        table_frame = tk.Frame(self)
        table_frame.pack(padx=10, pady=10, fill="both", expand=True, side="right")

        # Crear la tabla
        columns = ("Empresa", "Desde", "Hasta", "Regimen Previsional", "Dias trabajados")
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings")

        # Definir el ancho de las columnas después de crear la tabla
        self.table.column("Empresa", width=150)
        self.table.column("Desde", width=100)
        self.table.column("Hasta", width=100)
        self.table.column("Regimen Previsional", width=150)
        self.table.column("Dias trabajados", width=120)

        # Encabezados de las columnas
        self.table.heading("Empresa", text="Empresa")
        self.table.heading("Desde", text="Desde")
        self.table.heading("Hasta", text="Hasta")
        self.table.heading("Regimen Previsional", text="Regimen Previsional")
        self.table.heading("Dias trabajados", text="Dias trabajados")

        # Empaquetar la tabla en el frame de la tabla
        self.table.pack()

        # Inicializar la variable de días trabajados
        self.total_dias = 0

        # Crear un frame adicional para colocar la etiqueta


        # Etiqueta para mostrar el total de días trabajados
        self.total_label = tk.Label(table_frame, text=f"Total de días trabajados: {self.total_dias}",font=("Arial", 14, "bold"), pady=25)
        self.total_label.pack()

    def centrar_ventana(self, width, height):
        # Obtener el ancho y alto de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular la posición x e y
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Establecer las dimensiones y la posición de la ventana
        self.geometry(f'{width}x{height}+{x}+{y}')

    def on_agregar(self):
        empresa = self.empresa_entry.get()
        desde = self.desde_entry.get()
        hasta = self.hasta_entry.get()
        regimen = self.tipo_trabajo.get()

        dias_trabajados = self.calcular_dias(desde, hasta)

        self.table.insert("", "end", values=(empresa, desde, hasta, regimen, dias_trabajados))

        self.total_dias += dias_trabajados
        self.total_label.config(text=f"Total de días trabajados: {self.total_dias}")

    def calcular_dias(self, desde_str, hasta_str):
        formato = "%Y-%m-%d"
        try:
            desde = datetime.strptime(desde_str, formato)
            hasta = datetime.strptime(hasta_str, formato)
            diferencia = hasta - desde
            return diferencia.days
        except ValueError:
            return 0

if __name__ == "__main__":
    app = VentanaPrincipal("Octavio", "Rosales", "44958309")
    app.mainloop()
