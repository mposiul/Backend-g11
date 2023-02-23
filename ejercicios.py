from pprint import pprint

# class operaciones:
#     def __init__(self, num1, num2):
#         self.op1 = num1
#         self.op2 = num2
#     def suma(self):
#         return self.op1 + self.op2
#     def resta(self):
#         return self.op1 - self.op2
#     def multiplicacion(self):
#         return self.op1 * self.op2
#     def division(self):
#         return self.__redondear(self.op1 / self.op2)
#     def __redondear(self, numero):
#         return round(numero, 2)
        
# res = operaciones(2,3)
# print(res.division())

#Crear clase usuario que reciba los datos del usuario, datos nombre, edad, dni, estatura y estado civil
# Crear metodo que nos convierta estos datos en un diccionario


class usuario:
  def __init__(self, nombre, edad, dni, estatura, estadocivil):
      self.nom = nombre
      self.ed = edad
      self.dni = dni
      self.est = estatura
      self.estciv = estadocivil
  def nomina(self):
      return {
          'nombre': self.nom,
          'edad': self.ed,
          'dni': self.dni,
          'est': self.est,
          'estciv': self.estciv
      }

usuarios = usuario('Luis', 25, 41056695, 1.70, 'Soltero')

pprint(usuarios.nomina())
