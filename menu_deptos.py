from supermercado.menu import Menu

class MenuDeptos(Menu):
    def __init__(self):
        super().__init__()
        self.options = [

            "Dar de alta un nuevo departamento",
            "Consultar los departamentos",
            "Dar de baja un departamento",
            "Regresar"
        ]
    
    def get_option(self):
        return self.display_menu()