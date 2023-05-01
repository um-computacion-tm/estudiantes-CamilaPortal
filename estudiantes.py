##########################
##
##  ACA VA LA CLASE
##
##########################
class Persona:
    def __init__(self, param_nombre, param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_clase(self):
        self.asistencia += 1

class Profesor(Persona):
    def __init__(self, param_nombre, param_email, legajo_empleado):
        self.legajo_empleado = legajo_empleado
        super().__init__(param_nombre, param_email)

class Alumno(Persona):
    def __init__(self, param_nombre, param_email, numero_alumno):
        self.numero_alumno = numero_alumno
        self.materias_cursando = []
        super().__init__(param_nombre, param_email)

    def cursando(self, materia):
        self.materias_cursando.append(materia)

class Materia:
    def __init__(self, param_codigo, param_materia, param_carga):
        self.codigo = param_codigo
        self.materia = param_materia
        self.carga = param_carga


materia1 = Materia(2340, "Analisis Numerico", "5hs")
print("MATERIA")
print(materia1)
print("codigo de materia: ")
print(materia1.codigo)
print("nombre de materia: ")
print(materia1.materia)
print("carga horaria: ")
print(materia1.carga)

materia2 = Materia(2809, "Programación", "4hs")

alumna_maria = Alumno("Maria Jose", "mj2000@gmail.com", 12345678)
print('ALUMNO')
print(alumna_maria)
print("el nombre es: ")
print(alumna_maria.nombre)
print("el email es: ")
print(alumna_maria.email)

alumna_maria.cursando(materia1.materia)
alumna_maria.cursando(materia2.materia)

print("cursando: ")
print(alumna_maria.materias_cursando)



profesor_pepe = Profesor("Pepe", "jose@um.edu.ar", 9876543)
print("PROFESOR:")
print(profesor_pepe)
print("el nombre es: ")
print(profesor_pepe.nombre)
print("el email es: ")
print(profesor_pepe.email)
#print("su asistencia es: ")
#print(profesor_pepe.asistencia)

print("EL PROFESOR FUE A CLASE...")
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()

print("su asistencia es: ")
print(profesor_pepe.asistencia)

# profesor_pepe.cambiar_nombre("JOSE!")