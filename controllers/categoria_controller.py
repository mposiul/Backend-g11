from flask_restful import Resource, request
from flask import send_file
from werkzeug.utils import secure_filename
from os import path
# universal unique identifier
from uuid import uuid4

class ImagenesController(Resource):
    def post(self):
        # Si nosotros queremos enviar informacion por el form data, ahora utilizaremos la propiedad 'form'
        print(request.form)
        # Para obtener las llaves que contenmgan archivos 'files'
        print(request.files)
        imagen = request.files.get('imagen')
        print(imagen.filename)
        # Save sirve para guardar la imagen, pero utilizamos 
        nombre_seguro = secure_filename(uuid4().hex + '-' + imagen.filename)

        imagen.save(path.join('imagenes', nombre_seguro))

        return {
            'message': 'Categoria creada exitosamente'
        }
    
    def get(self, nombre):
        try:
            return send_file(path.join('imagenes', nombre))
        except FileNotFoundError:
            return send_file(path.join('imagenes', 'not_found.png'))
