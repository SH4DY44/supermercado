import tkinter as tk
import os
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from supermercado.menu_productos import MenuProductos
from supermercado.menu_deptos import MenuDeptos
from supermercado.menuAsignacionProds import MenuAsignacionProds
from supermercado.menuPrecios import MenuPrecios
from supermercado.producto import Producto
from supermercado.lectorDeArchivo import LectorDeArchivo
from supermercado.departamento import Departamento
from supermercado.asignacion import Asignacion

class SupermercadoUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Supermercado")
        self.title_label = ttk.Label(root, text='Bienvenido al Sistema de Supermercado', font=('Helvetica', 16, 'bold'), background='#FAFAFA', foreground='#212121')
        self.title_label.pack(pady=10)
        self.root.geometry("600x400")

        # Estilos
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12, 'bold'), padding=10, background='#4CAF50', foreground='#FFFFFF')
        self.style.configure('TLabel', font=('Helvetica', 14), background='#FFFFFF', foreground='#333333')
        self.style.configure('TFrame', background='#FFFFFF')
        self.style.configure('TButton', background='#4CAF50', foreground='#F5F5F5')
        self.style.map('TButton', background=[('active', '#45a049')])

        self.menu_productos = MenuProductos()
        self.menu_deptos = MenuDeptos()
        self.menu_asignacionProds = MenuAsignacionProds()
        self.menu_precios = MenuPrecios()

        # Crear el marco principal
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(expand=True, fill='both')

        # Cargar y mostrar la imagen de la tienda
        self.load_image()

        # Crear los botones de la pantalla principal
        self.create_main_buttons()

    def load_image(self):
        try:
            ruta_imagen = "/home/shady-lb/Escritorio/python/supermercado/tienda.jpg"
            self.image = Image.open(ruta_imagen)
            self.image = self.image.resize((200, 150))
            self.photo = ImageTk.PhotoImage(self.image)
            self.label = ttk.Label(self.main_frame, image=self.photo)
            self.label.pack(side="top", anchor="n", pady=10)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

    def create_main_buttons(self):
        self.clear_window()

        self.load_image()
        
        # Título de bienvenida
        
        # Botón de Entrar
        btn_entrar = ttk.Button(self.main_frame, text="Entrar", command=self.show_menu)
        btn_entrar.pack(side="left", expand=True, padx=20, pady=20)

        # Botón de Salir
        btn_salir = ttk.Button(self.main_frame, text="Salir", command=self.root.quit)
        btn_salir.pack(side="right", expand=True, padx=20, pady=20)

    def show_menu(self):
        self.clear_window()

        # Título de Supermercado
        titulo = ttk.Label(self.main_frame, text="Supermercado", font=("Helvetica", 16, 'bold'))
        titulo.pack(pady=10)

        # Opciones del menú
        btn_productos = ttk.Button(self.main_frame, text="Productos", command=self.productos)
        btn_productos.pack(fill='x', padx=20, pady=5)

        btn_deptos = ttk.Button(self.main_frame, text="Departamentos", command=self.deptos)
        btn_deptos.pack(fill='x', padx=20, pady=5)

        btn_asignacionProds = ttk.Button(self.main_frame, text="Asignación de Productos", command=self.asignacionProds)
        btn_asignacionProds.pack(fill='x', padx=20, pady=5)

        btn_precios = ttk.Button(self.main_frame, text="Precios", command=self.precios)
        btn_precios.pack(fill='x', padx=20, pady=5)

        # Botón de Regresar
        btn_regresar = ttk.Button(self.main_frame, text="Regresar", command=self.create_main_buttons)
        btn_regresar.pack(fill='x', padx=20, pady=20)

    def productos(self):
        self.clear_window()

        options = self.menu_productos.options

        for option in options:
            if option == "Dar de alta a un producto":
                ttk.Button(self.main_frame, text=option, command=self.alta_producto).pack(fill='x', pady=5)
            elif option == "Consultar productos":
                ttk.Button(self.main_frame, text=option, command=self.consultar_productos).pack(fill='x', pady=5)
            elif option == "Dar de baja a un producto":
                ttk.Button(self.main_frame, text=option, command=self.baja_producto).pack(fill='x', pady=5)
            elif option == "Regresar":
                ttk.Button(self.main_frame, text=option, command=self.show_menu).pack(fill='x', pady=5)

    def alta_producto(self):
        self.clear_window()

        ttk.Label(self.main_frame, text="Nombre del Producto:").pack(pady=5)
        nombre_entry = ttk.Entry(self.main_frame)
        nombre_entry.pack(pady=5)

        ttk.Label(self.main_frame, text="Nombre del Proveedor:").pack(pady=5)
        proveedor_entry = ttk.Entry(self.main_frame)
        proveedor_entry.pack(pady=5)

        def guardar_producto():
            nombre_producto = nombre_entry.get()
            nombre_proveedor = proveedor_entry.get()
            clave_producto = self.genera_clave_prod()

            if not nombre_producto or not nombre_proveedor:
                messagebox.showerror("Error", "Debe ingresar nombre del producto y proveedor.")
                return
            producto = Producto(clave_producto, nombre_producto, nombre_proveedor)

            if producto.guardar_en_archivo("Productos.txt"):
                messagebox.showinfo("Producto Guardado", f"Producto '{nombre_producto}' guardado con éxito")
                self.productos()
            else:
                messagebox.showerror("Error", "Hubo un error al guardar el producto.")

        # Contenedor para botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=5, fill='x')

        guardar_button = ttk.Button(button_frame, text="Guardar", command=guardar_producto)
        guardar_button.pack(side='left', padx=5)

        regresar_button = ttk.Button(button_frame, text="Regresar", command=self.productos)
        regresar_button.pack(side='right', padx=5)

    def consultar_productos(self):
        self.clear_window()

        lector = LectorDeArchivo("Productos.txt")
        lineas = lector.leer_archivo()

        if lineas:
            for linea in lineas:
                ttk.Label(self.main_frame, text=linea).pack(pady=2)
        else:
            ttk.Label(self.main_frame, text="No hay productos registrados.").pack(pady=2)

        ttk.Button(self.main_frame, text="Regresar", command=self.productos).pack(pady=5)

    def baja_producto(self):
        self.clear_window()

        ttk.Label(self.main_frame, text="Clave del Producto:").pack(pady=5)
        clave_entry = ttk.Entry(self.main_frame)
        clave_entry.pack(pady=5)

        def eliminar_producto():
            try:
                clave_producto = int(clave_entry.get())

                lector = LectorDeArchivo("Productos.txt")
                productos_string = lector.leer_archivo()
                productos = self.extraer_datos_producto(productos_string)

                encontrado = False
                indice = -1

                for i, producto in enumerate(productos):
                    if producto.get_clave_prod() == clave_producto:
                        encontrado = True
                        indice = i
                        break

                if encontrado:
                    productos.pop(indice)
                    self.actualizar_productos(productos)
                    messagebox.showinfo("Producto Eliminado", "El producto fue dado de baja con éxito.")
                    self.productos()
                else:
                    messagebox.showerror("Error", "No se encontró un producto con la clave proporcionada.")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido para la clave del producto.")

        # Contenedor para botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=5, fill='x')

        eliminar_button = ttk.Button(button_frame, text="Eliminar", command=eliminar_producto)
        eliminar_button.pack(side='left', padx=5)

        regresar_button = ttk.Button(button_frame, text="Regresar", command=self.productos)
        regresar_button.pack(side='right', padx=5)

    def genera_clave_prod(self):
        clave = 1
        productos = self.extraer_datos_producto(LectorDeArchivo("Productos.txt").leer_archivo())

        if productos:
            clave = productos[-1].get_clave_prod() + 1

        return clave

    def extraer_datos_producto(self, productos_string):
        productos = []
        for linea in productos_string:
            tokens = linea.strip().split(", ")
            if len(tokens) >= 3:
                try:
                    clave_prod = int(tokens[0])
                    nombre = tokens[1]
                    proveedor = tokens[2]
                    producto = Producto(clave_prod, nombre, proveedor)
                    productos.append(producto)
                except ValueError:
                    print(f"Error al convertir la clave del producto: {tokens[0]}")
            else:
                print(f"Línea ignorada por formato incorrecto: {linea}")
        return productos

    def actualizar_productos(self, productos):
        with open("Productos.txt", "w") as file:
            for producto in productos:
                file.write(f"{producto.get_clave_prod()}, {producto.get_nombre()}, {producto.get_proveedor()}\n")

#----------------------------------------------------------------
    def deptos(self):
        self.clear_window()
        options = self.menu_deptos.options
        
        for option in options:
            if option == "Dar de alta un nuevo departamento":
                ttk.Button(self.main_frame, text=option, command=self.altaDepto).pack(fill='x', pady=5)
            elif option == "Consultar los departamentos":
                ttk.Button(self.main_frame, text=option, command=self.consultar_Deptos).pack(fill='x', pady=5)
            elif option == "Dar de baja un departamento":
                ttk.Button(self.main_frame, text=option, command=self.baja_depto).pack(fill='x', pady=5)
            elif option == "Regresar":
                ttk.Button(self.main_frame, text=option, command=self.show_menu).pack(fill='x', pady=5)

    def altaDepto(self):
        self.clear_window()
        # Le pedimos los datos al usuario.
        ttk.Label(self.main_frame, text="Ingresa la clave del departamento:").pack(pady=5)
        claveDepto_entry = ttk.Entry(self.main_frame)
        claveDepto_entry.pack(pady=5)
        
        ttk.Label(self.main_frame, text="Nombre del Departamento:").pack(pady=5)
        nombreDepto_entry = ttk.Entry(self.main_frame)
        nombreDepto_entry.pack(pady=5)
        
        ttk.Label(self.main_frame, text="Nombre del Responsable del departamento:").pack(pady=5)
        jefe_entry = ttk.Entry(self.main_frame)
        jefe_entry.pack(pady=5)

        def guardar_depto():
            claveDepto = claveDepto_entry.get()
            nombreDepto = nombreDepto_entry.get()
            jefe = jefe_entry.get()
            
            # Validar que los campos no estén vacíos
            if not claveDepto or not nombreDepto or not jefe:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return
            
            departamento = Departamento(claveDepto, nombreDepto, jefe)
            
            # Guardar en deptos.txt
            if departamento.guardar_en_archivo("deptos.txt"):
                # Especificar la ruta donde se creará la carpeta
                ruta_departamentos = "/home/shady-lb/Escritorio/python/supermercado/departamentos"
                
                # Crear la carpeta "departamentos" si no existe
                if not os.path.exists(ruta_departamentos):
                    os.makedirs(ruta_departamentos)
                
                # Generar el archivo para productos
                nombre_archivo_productos = f"{ruta_departamentos}/{claveDepto}ProductosDepto.txt"
                with open(nombre_archivo_productos, "w") as file:
                    file.write("Productos del departamento:\n")  
                
                messagebox.showinfo("Departamento Guardado", f"Departamento '{nombreDepto}' guardado con éxito")
                self.deptos()  # Regresar al menú de departamentos
            else:
                messagebox.showerror("Error", "Hubo un error al guardar el departamento.")
        
        # Contenedor para botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=5, fill='x')

        guardar_button = ttk.Button(button_frame, text="Guardar", command=guardar_depto)
        guardar_button.pack(side='left', padx=5)

        regresar_button = ttk.Button(button_frame, text="Regresar", command=self.deptos)
        regresar_button.pack(side='right', padx=5)

    def consultar_Deptos(self):
        self.clear_window()
        lector = LectorDeArchivo("deptos.txt")
        lineas = lector.leer_archivo()
            
        if lineas:
            for linea in lineas:
                tk.Label(self.main_frame, text=linea).pack(pady=2)
        else:
            ttk.Label(self.main_frame, text="No hay departamentos registrados.").pack(pady=2)
            
        ttk.Button(self.main_frame, text="Regresar", command=self.deptos).pack(pady=5)

    def baja_depto(self):
        self.clear_window()  # Limpiar la ventana antes de mostrar la interfaz de baja
        
        ttk.Label(self.main_frame, text="Clave del departamento:").pack(pady=5)
        clave_entry = ttk.Entry(self.main_frame)
        clave_entry.pack(pady=5)

        def eliminar_depto():
            clave_depto = clave_entry.get().strip()  # Obtener la clave y eliminar espacios en blanco

            # Especificar la ruta donde se almacenan los archivos de productos
            ruta_departamentos = "/home/shady-lb/Escritorio/python/supermercado/departamentos"
            archivo_productos = f"{ruta_departamentos}/{clave_depto}ProductosDepto.txt"
            
            if not os.path.exists(archivo_productos):
                messagebox.showerror("Error", f"No hay un departamento con la clave {clave_depto}.")
                return
            
            # Eliminar el archivo del departamento
            os.remove(archivo_productos)
            
            # Eliminar el departamento de deptos.txt
            lector = LectorDeArchivo("deptos.txt")
            deptos_string = lector.leer_archivo()
            departamentos = self.extraer_datos_deptos(deptos_string)
            
            encontrado = False
            indice = -1
            
            for i, departamento in enumerate(departamentos):
                if departamento.claveDepto == clave_depto:
                    encontrado = True
                    indice = i
                    break
            
            if encontrado:
                departamentos.pop(indice)  # Eliminar el departamento de la lista
                self.actualizar_deptos(departamentos)  # Actualizar el archivo deptos.txt
                messagebox.showinfo("Departamento Eliminado", f"Departamento con clave {clave_depto} eliminado con éxito.")
                self.deptos()  # Regresar al menú de departamentos
            else:
                messagebox.showerror("Error", f"No se encontró el departamento con la clave {clave_depto}.")

        # Contenedor para botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=5, fill='x')

        eliminar_button = ttk.Button(button_frame, text="Eliminar", command=eliminar_depto)
        eliminar_button.pack(side='left', padx=5)

        regresar_button = ttk.Button(button_frame, text="Regresar", command=self.deptos)
        regresar_button.pack(side='right', padx=5)

    def extraer_datos_deptos(self, deptos_string):
        departamentos = []
        for linea in deptos_string:
            tokens = linea.strip().split(", ")
            if len(tokens) >= 3:
                clave_depto = tokens[0]  # Mantener como string
                nombre_depto = tokens[1]
                jefe = tokens[2]
                departamento = Departamento(clave_depto, nombre_depto, jefe)
                departamentos.append(departamento)
        return departamentos

    def actualizar_deptos(self, deptos):
        with open("deptos.txt", "w") as file:
            for departamento in deptos:
                file.write(f"{departamento.claveDepto}, {departamento.nombre}, {departamento.jefe}\n")

#----------------------------------------------------------------
    def asignacionProds(self):
        self.clear_window()
        options = ["Dar de alta a un producto en un depto", "Dar de baja a un producto en un depto", "Regresar"]

        for option in options:
            if option == "Dar de alta a un producto en un depto":
                ttk.Button(self.main_frame, text=option, command=self.altaProductoEnDepto).pack(fill='x', pady=5)
            elif option == "Dar de baja a un producto en un depto":
                ttk.Button(self.main_frame, text=option, command=self.bajaProductoEnDepto).pack(fill='x', pady=5)
            elif option == "Regresar":
                ttk.Button(self.main_frame, text=option, command=self.show_menu).pack(fill='x', pady=5)

    def altaProductoEnDepto(self):
        self.clear_window()  # Limpiar la ventana actual

        # Solicitar la clave del departamento
        ttk.Label(self.main_frame, text="Clave del departamento:").pack(pady=5)
        claveDepto_entry = ttk.Entry(self.main_frame)
        claveDepto_entry.pack(pady=5)

        # Solicitar la clave del producto
        ttk.Label(self.main_frame, text="Clave del producto:").pack(pady=5)
        claveProd_entry = ttk.Entry(self.main_frame)
        claveProd_entry.pack(pady=5)

        # Contenedor para botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=5)

        # Botón para guardar la asignación
        guardar_button = ttk.Button(button_frame, text="Guardar", command=lambda: self.guardar_asignacion(claveDepto_entry.get(), claveProd_entry.get()))
        guardar_button.pack(side='left', padx=5)

        # Botón para regresar
        regresar_button = ttk.Button(button_frame, text="Regresar", command=self.asignacionProds)
        regresar_button.pack(side='right', padx=5)

    def guardar_asignacion(self, claveDepto, claveProd):
        # Validar que los campos no estén vacíos
        if not claveDepto or not claveProd:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Verificar existencia del archivo del departamento
        nombre_archivo = f"/home/shady-lb/Escritorio/python/supermercado/departamentos/{claveDepto}ProductosDepto.txt"
        if not self.existeProductosDepto(nombre_archivo):
            messagebox.showerror("Error", f"No existe el departamento con la clave {claveDepto}.")
            return

        # Verificar existencia del producto
        if not self.producto_existe(int(claveProd)):
            messagebox.showerror("Error", f"No se encontró el producto con la clave {claveProd}.")
            return

        # Verificar si el producto ya está asignado al departamento
        if self.producto_asignado(int(claveProd), nombre_archivo):
            messagebox.showerror("Error", f"El producto con clave {claveProd} ya está asignado al departamento {claveDepto}.")
            return

        # Crear la asignación
        asignacion = Asignacion(int(claveProd), -1, claveDepto)  # Precio se establece en -1

        # Guardar la asignación en el archivo
        if asignacion.guardarEnArchivo(nombre_archivo):
            messagebox.showinfo("Éxito", f"El producto con clave {claveProd} ha sido asignado al departamento con clave {claveDepto} exitosamente.")
            self.asignacionProds()  # Redirigir al menú de asignación
        else:
            messagebox.showerror("Error", "Hubo un error al guardar la asignación.")

    def existeProductosDepto(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r'):
                return True  # El archivo existe
        except FileNotFoundError:
            return False  # El archivo no existe

    def producto_existe(self, claveProd):
        lector = LectorDeArchivo("Productos.txt")
        productos_string = lector.leer_archivo()
        productos = self.extraer_datos_producto(productos_string)

        for producto in productos:
            if producto.get_clave_prod() == claveProd:  # Usar el método para obtener la clave
                return True

        return False

    def extraer_datos_producto(self, productos_string):
        productos = []
        for linea in productos_string:
            tokens = linea.strip().split(", ")
            if len(tokens) >= 3:
                try:
                    clave_prod = int(tokens[0])
                    nombre = tokens[1]
                    proveedor = tokens[2]
                    producto = Producto(clave_prod, nombre, proveedor)
                    productos.append(producto)
                except ValueError:
                    print(f"Error al convertir la clave del producto: {tokens[0]}")
        return productos

    def producto_asignado(self, claveProd, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as file:
                lineas = file.readlines()
                for linea in lineas:
                    tokens = linea.strip().split(", ")
                    if len(tokens) > 0:
                        try:
                            if int(tokens[0]) == claveProd:  # Convertir a int solo si es válido
                                return True  
                        except ValueError:
                            continue  
        except FileNotFoundError:
            return False  

        return False  # El producto no está asignado
    
    def bajaProductoEnDepto(self):
        self.clear_window()  # Limpiar la ventana actual

        # Solicitar la clave del departamento
        ttk.Label(self.main_frame, text="Clave del departamento:").pack(pady=5)
        claveDepto_entry = ttk.Entry(self.main_frame)
        claveDepto_entry.pack(pady=5)

        # Solicitar la clave del producto a eliminar
        ttk.Label(self.main_frame, text="Clave del producto a dar de baja:").pack(pady=5)
        claveProd_entry = ttk.Entry(self.main_frame)
        claveProd_entry.pack(pady=5)

        # Contenedor para botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=5)

        # Botón para eliminar el producto
        eliminar_button = ttk.Button(button_frame, text="Eliminar", command=lambda: self.eliminar_producto(claveDepto_entry.get(), claveProd_entry.get()))
        eliminar_button.pack(side='left', padx=5)

        # Botón para regresar
        regresar_button = ttk.Button(button_frame, text="Regresar", command=self.asignacionProds)
        regresar_button.pack(side='right', padx=5)

    def eliminar_producto(self, claveDepto, claveProd):
        # Validar que las claves no estén vacías
        if not claveDepto or not claveProd:
            messagebox.showerror("Error", "Todas las claves son obligatorias.")
            return

        # Verificar si el departamento existe
        nombre_archivo = f"/home/shady-lb/Escritorio/python/supermercado/departamentos/{claveDepto}ProductosDepto.txt"
        if not self.existeProductosDepto(nombre_archivo):
            messagebox.showerror("Error", f"No existe el departamento con la clave {claveDepto}.")
            return

        # Leer los productos del departamento
        try:
            with open(nombre_archivo, 'r') as file:
                lineas = file.readlines()

            # Buscar y eliminar el producto
            encontrado = False
            with open(nombre_archivo, 'w') as file:
                for linea in lineas:
                    tokens = linea.strip().split(", ")
                    if len(tokens) > 0:
                        try:
                            if int(tokens[0]) == int(claveProd):  # Comparar con la clave del producto
                                encontrado = True  # Marcamos que encontramos el producto
                                continue  # No escribir esta línea en el archivo
                        except ValueError:
                            continue  # Ignorar líneas que no se pueden convertir a int
                    file.write(linea)  # Escribir la línea de vuelta si no es la que se elimina

            if encontrado:
                messagebox.showinfo("Éxito", f"El producto con clave {claveProd} ha sido dado de baja del departamento con clave {claveDepto} exitosamente.")
                self.asignacionProds()  # Redirigir al menú de asignación
            else:
                messagebox.showerror("Error", f"No se ha encontrado el producto con la clave {claveProd} en el departamento {claveDepto}.")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al intentar eliminar el producto: {e}")
    #----------------------------------------------------------------
    def precios(self):
        self.clear_window()
        options = self.menu_precios.options

        for option in options:
            if option == "Asignar precio a un producto":
                ttk.Button(self.main_frame, text=option, command=self.asignarPrecio).pack(fill='x', pady=5)
            elif option == "Consultar productos y precios de un departamento":
                ttk.Button(self.main_frame, text=option, command=self.consultarPrecios).pack(fill='x', pady=5)
            elif option == "Regresar":
                ttk.Button(self.main_frame, text=option, command=self.show_menu).pack(fill='x', pady=5)

    def asignarPrecio(self):
        self.clear_window()
        # Solicitar la clave del departamento
        ttk.Label(self.main_frame, text="Clave del departamento:").pack(pady=5)
        claveDepto_entry = ttk.Entry(self.main_frame)
        claveDepto_entry.pack(pady=5)

        # Solicitar la clave del producto
        ttk.Label(self.main_frame, text="Clave del producto:").pack(pady=5)
        claveProd_entry = ttk.Entry(self.main_frame)
        claveProd_entry.pack(pady=5)

        # Solicitar el nuevo precio
        ttk.Label(self.main_frame, text="Nuevo precio:").pack(pady=5)
        precio_entry = ttk.Entry(self.main_frame)
        precio_entry.pack(pady=5)

        # Contenedor para botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=5)

        # Botón para guardar el precio
        guardar_button = ttk.Button(button_frame, text="Asignar Precio", command=lambda: self.guardar_precio(claveDepto_entry.get(), claveProd_entry.get(), precio_entry.get()))
        guardar_button.pack(side='left', padx=5)

        # Botón para regresar
        regresar_button = ttk.Button(button_frame, text="Regresar", command=self.precios)
        regresar_button.pack(side='right', padx=5)

    def guardar_precio(self, claveDepto, claveProd, nuevo_precio):
    # Validar que las claves y el precio no estén vacíos
        if not claveDepto or not claveProd or not nuevo_precio:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Verificar si el departamento existe
        nombre_archivo = f"/home/shady-lb/Escritorio/python/supermercado/departamentos/{claveDepto}ProductosDepto.txt"
        if not self.existeProductosDepto(nombre_archivo):
            messagebox.showerror("Error", f"No existe el departamento con la clave {claveDepto}.")
            return

        # Leer los productos del departamento
        try:
            with open(nombre_archivo, 'r') as file:
                lineas = file.readlines()

            # Buscar y modificar el precio del producto
            encontrado = False
            with open(nombre_archivo, 'w') as file:
                for linea in lineas:
                    tokens = linea.strip().split(", ")
                    if len(tokens) > 0:
                        try:
                            if int(tokens[0]) == int(claveProd):  # Comparar con la clave del producto
                                tokens[1] = nuevo_precio  
                                encontrado = True
                                linea = ", ".join(tokens) + "\n" 
                        except ValueError:
                            continue  
                    file.write(linea)  

            if encontrado:
                messagebox.showinfo("Éxito", "El precio se asignó con éxito.")
                self.precios()  
            else:
                messagebox.showerror("Error", "No se encontró un producto con la clave proporcionada.")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al intentar asignar el precio: {e}")




    def consultarPrecios(self):
        self.clear_window()  # Limpiar la ventana actual

        # Solicitar la clave del departamento
        ttk.Label(self.main_frame, text="Clave del departamento:").pack(pady=5)
        claveDepto_entry = ttk.Entry(self.main_frame)
        claveDepto_entry.pack(pady=5)

        # Contenedor para botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=5)

        # Botón para consultar precios
        consultar_button = ttk.Button(button_frame, text="Consultar Precios", command=lambda: self.mostrar_precios(claveDepto_entry.get()))
        consultar_button.pack(side='left', padx=5)

        # Botón para regresar
        regresar_button = ttk.Button(button_frame, text="Regresar", command=self.precios)
        regresar_button.pack(side='right', padx=5)

    def mostrar_precios(self, claveDepto):
        # Verificar si el departamento existe
        nombre_archivo = f"/home/shady-lb/Escritorio/python/supermercado/departamentos/{claveDepto}ProductosDepto.txt"
        if not self.existeProductosDepto(nombre_archivo):
            messagebox.showerror("Error", f"No existe el departamento con la clave {claveDepto}.")
            return

        # Crear una nueva ventana para mostrar los precios
        nueva_ventana = tk.Toplevel(self.main_frame)
        nueva_ventana.title("Productos y Precios")

        # Leer los productos del departamento
        try:
            with open(nombre_archivo, 'r') as file:
                lineas = file.readlines()

            # Añadir el título
            ttk.Label(nueva_ventana, text="Productos y precios:", font=('Arial', 14, 'bold')).pack(pady=10)

            if lineas:
                productos_mostrados = False  # Bandera para verificar si se mostraron productos

                for linea in lineas:
                    tokens = linea.strip().split(", ")
                    if len(tokens) >= 2:
                        clave_prod = tokens[0]
                        precio = tokens[1]
                        ttk.Label(nueva_ventana, text=f"Clave: {clave_prod}, Precio: {precio}").pack(pady=5)
                        productos_mostrados = True

                # Si no se mostraron productos, mostrar un mensaje
                if not productos_mostrados:
                    ttk.Label(nueva_ventana, text="No hay productos registrados en este departamento.").pack(pady=5)

            else:
                ttk.Label(nueva_ventana, text="No hay productos registrados en este departamento.").pack(pady=5)

            # Botón para regresar
            regresar_button = ttk.Button(nueva_ventana, text="Regresar", command=nueva_ventana.destroy)
            regresar_button.pack(pady=20)

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al intentar consultar los precios: {e}")



    #----------------------------------------------------------------
    def clear_window(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SupermercadoUI(root)
    root.mainloop()