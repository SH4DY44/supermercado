from supermercado.menu import Menu

class MenuPrecios(Menu):
    def __init__(self):
        super().__init__()
        self.options = [
            "Asignar precio a un producto",
            "Consultar productos y precios de un departamento",
            "Regresar"
        ]
    
    def get_option(self):
        return self.display_menu()