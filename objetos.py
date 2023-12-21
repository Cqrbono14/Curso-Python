class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def obtener_informacion(self):
        return f'Nombre: {self.nombre}, Salario: {self.salario}'
    
    def aumentar_salario(self, porcentaje):
        aumento = self.salario * (porcentaje / 100)
        self.salario += aumento
        return f'¡Aumento del {porcentaje}% aplicado!, Nuevo salario: {self.salario}'

# Crear instancias de la clase Empleado
empleado1 = Empleado('Juan', 20000)
empleado2 = Empleado('Maria', 30000)

