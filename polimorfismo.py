# Clase padre persona, atributos nombre, edad y sexo
# Clase hijo empleado, atributos salario, horario laboral, metodo trabajar
# Clase hijo estudiante, atributos calificaciones, cantidad de materias, metodo estudiar

class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def obtener_informacion(self):
        pass

class Empleado(Persona):
    def __init__(self, nombre, edad, sexo, salario, horario_laboral):
        super().__init__(nombre, edad, sexo)
        self.salario = salario
        self.horario_laboral = horario_laboral
    
    def obtener_informacion(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}, Salario: {self.salario}, Horario laboral: {self.horario_laboral}'
    
    def trabajar(self, siTrabajaNoTrabaja):
        if siTrabajaNoTrabaja == True:
            print(f'El empleado {self.nombre} esta trabajando')
        else:
            print(f'El empleado {self.nombre} no esta trabajando')

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, calificaciones, cantidad_materias):
        super().__init__(nombre, edad, sexo)
        self.calificaciones = calificaciones
        self.cantidad_materias = cantidad_materias
    
    def obtener_informacion(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}, Calificaciones: {self.calificaciones}, Cantidad de materias: {self.cantidad_materias}'
    
    def estudiar(self, siEstudiaNoEstudia):
        if siEstudiaNoEstudia == True:
            print(f'El estudiante {self.nombre} esta estudiando')
        else:
            print(f'El estudiante {self.nombre} no esta estudiando')

empleado1 = Empleado('Juan', 25, 'Masculino', 20000, '8:00 a 17:00')
alumno1 = Estudiante('Haniel', 20, 'Masculino', [10, 9, 8, 10, 10], 5)

print(empleado1.obtener_informacion())
empleado1.trabajar(True)
print(alumno1.obtener_informacion())
alumno1.estudiar(True)
