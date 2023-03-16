from flask import Flask
from flask_migrate import Migrate
from database import conexion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
conexion.init_app

Migrate(app, conexion)

if __name__=='__main__':
    app.run(debug=True)