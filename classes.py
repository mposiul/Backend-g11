# class vehiculo:
#     def __init__(self, color, placa, marca):
#         self.color = color
#         self.placa = placa
#         self.marca = marca

#     def verificarEstado(self, fabricacion):
#         return f'El vehiculo de color {self.color} fue fabricado en el anio {fabricacion}'
    
#     def concatenarCaracteristicas(self):
#         return f'El vehiculo con placa {self.placa} y de color {self.color} es de marca {self.marca}'

# vehiculox = vehiculo('rojo','V452','Honda')

#print(vehiculox.placa)
#print(vehiculox.verificarEstado(1998))
#print(vehiculox.concatenarCaracteristicas())

class Alumno:
  def __init__(self, nom, ed):
    self.nombre = nom
    self.edad = ed

  def __str__ (self):
    return f'Nombre : {self.nombre}, Edad : {self.edad}'
    
  def nombreEdad(self):
    return f'Nombre : {self.nombre}, Edad : {self.edad}'
    
  def mostrarNombre(self):
    return self.nombre
    
  def mostrarEdad(self):
    return self.edad
    
x = Alumno('Eduardo', 30)
y = Alumno('Luis', 40)
print (x)
print(y.nombreEdad())
print(x.mostrarNombre())
