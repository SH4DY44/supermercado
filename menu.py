from abc import ABC, abstractmethod

class Menu(ABC):
    def __init__(self):
        self.options = []  # Las subclases deberán inicializar las opciones

    @abstractmethod
    def get_option(self):
        """Método abstracto que debe ser implementado por las subclases."""
        pass

    def display_menu(self):
        if not self.options:
            return 0

        print()
        for i, option in enumerate(self.options):
            print(f"{i + 1}: {option}")
        print()

        while True:
            try:
                choice = int(input("Ingresa la opción deseada: "))
                if 1 <= choice <= len(self.options):
                    return choice
                else:
                    print("Opción inválida. Por favor, ingresa una opción válida.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")
