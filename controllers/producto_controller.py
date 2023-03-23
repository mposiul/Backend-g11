from flask_restful import Resource, request
from database import conexion
from models.producto_model import Producto
from dtos.producto_dto  import ProductoDto
from os import path

class ProductoController(Resource):
    def post(self):
        data = request.form.to_dict()
        # TODO: validar que tengamos esa llave en el formulario llamado 'imagen'
        # TODO: validar que solo sean imegenes
        imagen = request.files.get('imagen')
        # TODO: Agregar un uuid al nombre de la imagen y sea un nombre valido
        # TODO: No recibir imagenes que pesen mas de 10mb
        data['imagen'] = imagen.filename
        try:
            dto = ProductoDto()
            data_serializada = dto.load(data)
            nuevo_producto = Producto(**data_serializada)

            conexion.session.add(nuevo_producto)
            imagen.save(path.join('imagenes', data['imagen']))

            conexion.session.commit()

            return {
                'message': 'Producto creado exitosamente'
            }
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Error al crear el producto',
                'content': error.args
            }

    def get(self):
        resultado = conexion.session
        pass