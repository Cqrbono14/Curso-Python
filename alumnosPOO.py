# 3 atributos y 3 metodos
# Atributos: nombre, id, calificacion
# Metodos: estudiar, ir a clase, hacer tarea

class Alumno:
    def __init__ (self, nombre, id, calificacion):
        self.nombre = nombre
        self.id = id
        self.calificacion = calificacion

    def obtener_informacion(self):
        return f'Nombre: {self.nombre}, ID: {self.id}, Calificacion: {self.calificacion}'
    
    def estudiar(self, siEstudiaNoEstudia):
        if siEstudiaNoEstudia == True:
            print(f'El alumno {self.nombre} esta estudiando')
        else:
            print(f'El alumno {self.nombre} no esta estudiando')

    def ir_a_clase(self, siFueNoFue):
        if siFueNoFue == True:
            print(f'El alumno {self.nombre} fue a clase')
        else: 
            print(f'El alumno {self.nombre} no fue a clase')
    
    def hacer_tarea(self, siHaceTareaNoHaceTarea):
        if siHaceTareaNoHaceTarea == True:
            print(f'El alumno {self.nombre} esta haciendo tarea')
        else:
            print(f'El alumno {self.nombre} no esta haciendo tarea')

alumno1 = Alumno('Haniel', 1, 10)
alumno2 = Alumno('Pepe', 2, 9)

print(alumno1.obtener_informacion())
alumno1.estudiar(True)
alumno1.ir_a_clase(False)
alumno1.hacer_tarea(True)

print(alumno2.obtener_informacion())
alumno2.estudiar(False)
alumno2.ir_a_clase(True)
alumno2.hacer_tarea(False)