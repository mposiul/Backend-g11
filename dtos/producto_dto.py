from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.producto_model import Producto

class ProductoDto(SQLAlchemyAutoSchema):
    class Meta:
        # Sirve para indicar a mi DTO que ahora queremos que tmb reconozca las columnas que sean FK
        include_fk = True
        model = Producto
