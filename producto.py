import uuid

class Producto:
    def __init__(self, clave_prod=None, nombre=None, proveedor=None):
        self.clave_prod = clave_prod
        self.nombre = nombre
        self.proveedor = proveedor

    def guardar_en_archivo(self, file_path):
        try:
            with open(file_path, 'a') as file:
                file.write(f"{self.clave_prod}, {self.nombre}, {self.proveedor}\n")
            return True
        except IOError as e:
            print(f"Error al guardar en el archivo: {e}")
            return False

    # Métodos getter y setter
    def get_clave_prod(self):
        return self.clave_prod

    def get_nombre(self):
        return self.nombre

    def get_proveedor(self):
        return self.proveedor

    def set_clave_prod(self, clave_prod):
        self.clave_prod = clave_prod

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_proveedor(self, proveedor):
        self.proveedor = proveedor
