from pprint import pprint

class Usuario:
    def __init__(self, nombre, edad, dni, estatura, estado_civil) -> None:
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.estatura = estatura
        self.estado_civil = estado_civil
      
    def convertirDiccionario(self):
        return {
            'nombre': self.nombre,
            'edad': self.edad,
            'dni': self.dni,
            'estatura': self.estatura,
            'estado_civil': self.estado_civil
        }
    
usuario = Usuario('Paolo', 25, 77337722, 1.80, 'soltero')

pprint(usuario.convertirDiccionario())