import uuid

class Asignacion:
    def __init__(self, claveProd=None, precio=None, claveDepto=None):
        self.claveProd = claveProd
        self.precio = precio
        self.claveDepto = claveDepto

    def Asignacion(self, prodEnDepto):
        self.claveProd = prodEnDepto.claveProd
        self.precio = prodEnDepto.precio
        self.claveDepto = prodEnDepto.claveDepto

    def guardarEnArchivo(self, file_path):
        try:
            with open(file_path, "a") as file:
                file.write(f"{self.claveProd}, {self.precio}, {self.claveDepto}\n")
                return True
        except Exception as e:
            print(f"Error al guardar en el archivo: {e}")
            return False
        

    def get_clave_prod(self):
        return self.clave_prod

    def get_nombre(self):
        return self.nombre

    def get_proveedor(self):
        return self.proveedor
