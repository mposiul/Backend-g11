class persona:
  estatura = 1.80
  peso = 80
  signo_zodiacal = 'Virgo'

  def sumar(self, *args):
    x = 0
    for num in args:
      x += num
    return x
  
  def saludar(self, nombre):
    return (f'Hola {nombre}')


pers1 = persona()
pers2 = persona()

pers1.peso = 70
pers2.peso = 50

print(pers1.peso)
print(pers2.peso)

print(f'El resultado es {pers1.sumar(1,2,3,4,5)}')

saludo = pers1.saludar('Luis')
print(saludo)