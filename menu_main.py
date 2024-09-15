from supermercado.menu import Menu

class MenuMain(Menu):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base
        self.options = [
            "Productos",
            "Departamentos",
            "Asignación de productos a un Depto.",
            "Precios",
            "Salir"
        ]

    def get_option(self):
        return self.display_menu()  # Muestra el menú y devuelve la opción seleccionada
