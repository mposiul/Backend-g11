def saludar(nombre):
    saludo = 'Hola {}'.format(nombre)
    print(saludo)


saludar('Luis')


def saludar_varios(*args):
    print(args)
    for nombre in args:
        print(f'Hola {nombre}')


def informacion_usuario(**kwargs):
    # kwargs > keyboard arguments o se le pasan parametros por llaves
    print(kwargs)
    # .get('llave') -> devolver el valor si es que existe la llave, sino existe devolvera none
    print(kwargs.get('estatura', 'No hay'))
    try:
        print(kwargs['estatura'])
    except:
        print('no existe la llave estatura')


informacion_usuario(nombre='Eduardo', Edad=30,
                    estado_civil='soltero', estatura=1.70)
informacion_usuario(nombre='Pamela', apellido='Juarez',
                    nacionalidad='Colombiana', fecha_nacimiento='31/06/1999')

# saludar_varios('Luis','Omar','Edison','Christian')
# saludar_varios('Pedro','Luis')
# Recivir dos valores y realizar la division ( dividendo / divisor) y retornar su resultado


def dividir(dividendo, divisor):
    # si la division sa err dar division incorrecta
  resultado = dividendo / divisor
  return resultado


res = dividir(6, 3)
print(f'El resultado de la division es {res}')

res = dividir(6, 3)
print(f'El resultado de la division es {res}')


def dividir_a(dividendo, divisor):
  try:
    resultado = dividendo / divisor
    return resultado
  except ZeroDivisionError:
    return 'No puede haber division entre 0'
  except TypeError:
    return 'Las divisiones solo son entre numeros'
  except:
    return 'error desconocido'


res = dividir_a(4, 'b')
print(res)
