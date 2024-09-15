from supermercado.menu import Menu

class MenuProductos(Menu):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base
        self.options = [
            "Dar de alta a un producto",
            "Consultar productos",
            "Dar de baja a un producto",
            "Regresar"
        ]

    def get_option(self):
        return self.display_menu()  # Muestra el menú y devuelve la opción seleccionada
