from supermercado.menu import Menu

class MenuAsignacionProds(Menu):
    def __init__(self):
        super().__init__()
        self.options = [
            "Dar de alta a un producto en un depto",
            "Dar de baja a un producto en un depto",
            "Regresar"
        ]

    def get_option(self):
        return self.display_menu()