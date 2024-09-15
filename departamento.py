import uuid

class Departamento:
    def __init__(self, claveDepto=None, nombre=None, jefe=None):
        self.claveDepto = claveDepto
        self.nombre = nombre
        self.jefe = jefe

    def guardar_en_archivo(self, file_path):
        try:
            with open(file_path, 'a') as file:
                file.write(f"{self.claveDepto}, {self.nombre}, {self.jefe}\n")
                return True
        except IOError as e:
            print("Error al guardar en el archivo: {e}")
            return False

#Generamos los metodos getter y setter de la clase.
    def get_claveDepto(self):
        return self.claveDepto

    def get_nombre(self):
        return self.nombre
    
    def get_jefe(self):
        return self.jefe
    
    def set_claveDepto(self, claveDepto):
        self.claveDepto = claveDepto
        
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def set_jefe(self, jefe):
        self.jefe = jefe
    