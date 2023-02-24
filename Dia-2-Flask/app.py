from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Bienvenidos ami primera API con Flask :)"

@app.route("/alumno")
def alumno():
  return {
    'nombre':'eduardo',
    'edad':35,
    'promedio':18
  }

lista_alumnos = [
  {
    'Nro':'1',
    'nombre':'Luis',
    'edad':35,
    'promedio':18
  },
  {
    'Nro':'2',
    'nombre':'Omar',
    'edad':37,
    'promedio':17
  }
  ]

@app.route("/alumnos", methods=['GET', 'POST','PUT','DELETE','OPTIONS','PATCH'])
def alumnos():
  return lista_alumnos

@app.route("/alumno/<nombre>")
def buscar_alumno(nombre):
  for alumno in lista_alumnos:
    if alumno['nombre'] == nombre:
      return alumno
  return {
        'Message':'El alumno no existe...'
      }



# debug => Si realizamos algun cambio podremos verlo en tiempo real (se reiniciara el servidor)
app.run(debug=True)