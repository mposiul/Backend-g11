from flask_restful import Resource, request
from flask import send_file
from werkzeug.utils import secure_filename
from os import path
# universal unique identifier
from uuid import uuid4
from dtos.categoria_dto import CategoriaDto
from models.categoria_model import Categoria
from database import conexion
from sqlalchemy.orm import Query

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

class CategoriasController(Resource):
    def post(self):
        mimetype_validos = ['image/svg+xml', 'image/webp', 'image/png', 'image/jpeg']
        mimetype_valido = 'image/'
        data = request.form.to_dict()
        try:
            # Vamos a recibir la imagen mediante la llave llamada imagen
            # Vamos a recibir la imagen mediante llave
            imagen = request.files.get('imagen')
            print(imagen.filename)
            if mimetype_valido not in imagen.mimetype:
                raise Exception('El archivo no es un archivo valido')

            dto = CategoriaDto()
            # Agrego a mi formulario el nombre de la imagen que me envia el cliente
            nombre = secure_filename(uuid4().hex +'-'+ imagen.filename)

            # Agrego a mi formulario el nombre de la imagen que me envioa el cliente
            # Agregamos la carpeta donde se almacena la imagen y con el nuevo nombre

            data['imagen'] = 'imagenes/' + nombre
            data_serializada = dto.load(data)

            nueva_categoria = Categoria(**data_serializada)
            conexion.session.add(nueva_categoria)

            # Gurado la imagen en nuestro servidor
            imagen.save(path.join('imagenes', nombre))
            conexion.session.commit()

            return {
                'message': 'Categoria creada exitosamente'
            }
        except Exception as error:
            return {
                'message': 'Error al crear la categoria',
                'content': error.args
            }

    def get(self):
        query = conexion.session.query(Categoria)
        resultado = query.all()
        dto = CategoriaDto()
        data = dto.dump(resultado, many=True)

        return {
            'content': data
        }
    