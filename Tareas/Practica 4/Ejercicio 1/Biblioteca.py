class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

    def mostrar_pagina(self):
        print(f"Página {self.numero}: {self.contenido}")

class Libro:
    def __init__(self, titulo, isbn, contenidos_paginas):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = [Pagina(i + 1, cont) for i, cont in enumerate(contenidos_paginas)]

    def leer(self):
        print(f"--- Leyendo: {self.titulo} ---")
        for p in self.paginas:
            p.mostrar_pagina()

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_info(self):
        print(f"Autor: {self.nombre} | Nacionalidad: {self.nacionalidad}")

class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrar_info(self):
        print(f"Estudiante: {self.nombre} | Código: {self.codigo}")

class Prestamo:
    def __init__(self, estudiante, libro):
        self.estudiante = estudiante
        self.libro = libro
        self.fecha_prestamo = "10/05/2026"
        self.fecha_devolucion = "24/05/2026"

    def mostrar_info(self):
        print(f"PRÉSTAMO: Libro '{self.libro.titulo}' entregado a {self.estudiante.nombre}")

class Biblioteca:
    class Horario:
        def __init__(self, dias, apertura, cierre):
            self.dias = dias
            self.apertura = apertura
            self.cierre = cierre

        def mostrar_horario(self):
            print(f"Horario: {self.dias} de {self.apertura} a {self.cierre}")

    def __init__(self, nombre, dias_atencion, hora_ap, hora_ci):
        self.nombre = nombre
        self.libros = []
        self.autores = []
        self.horario = self.Horario(dias_atencion, hora_ap, hora_ci)
        self.prestamos_activos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def prestar_libro(self, estudiante, libro):
        nuevo_prestamo = Prestamo(estudiante, libro)
        self.prestamos_activos.append(nuevo_prestamo)
        print(f"Sistema: Préstamo registrado para {estudiante.nombre}")

    def mostrar_estado(self):
        print(f"\n======= ESTADO DE: {self.nombre} =======")
        self.horario.mostrar_horario()
        print(f"Libros en inventario: {len(self.libros)}")
        print(f"Autores registrados: {len(self.autores)}")
        print(f"Préstamos activos: {len(self.prestamos_activos)}")

    def cerrar_biblioteca(self):
        print(f"\nCerrando la biblioteca {self.nombre}...")
        self.prestamos_activos.clear()
        print("La biblioteca está cerrada. Los registros de préstamos han sido finalizados.")