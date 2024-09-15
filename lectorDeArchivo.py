class LectorDeArchivo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def leer_archivo(self):
        lectura = []
        try:
            with open(self.nombre_archivo, "r") as archivo:
                for linea in archivo:
                    lectura.append(linea.strip())
        except FileNotFoundError:
            print(f"El archivo {self.nombre_archivo} no existe.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")
        return lectura
