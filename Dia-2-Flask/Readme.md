#Entornos virtuales Python
## Crear entorno virtual
```
py -m venv venv
```

# Activar el entorno virtual
```
source ./venv/Scripts/activate
```

## Activar entorno virtual
```
Para cmd -> venv\Scripts\activate
Para gitbash -> source ./venv/Scripts/activate
```

## Desactivar el entorno virtual
```
deactivate
```

## Instalar Flask
```
pip install Flask
```

## Verificar que Flask haya sido instalado
```
pip freeze
```

## Listar las librerias en el archivo `requirements.txt`
```
pip freeze > requirements.txt
```

## Instalar las librerias que estan listadas en nuestro archivo requirements.txt
```
pip install -r requirements.txt
```