from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class ManejoUsuario(BaseUserManager):
    def create_superuser(self, correo, nombre, apellido, password, tipoUsuario):
        # este metodo se mandara llamar cuando en la terminal se ponga python manage.py createsuperuser
        if not correo:
            raise ValueError('El usuario debe tener un correo')

        # normalize_email => sirve para llevar todo el correo a minusculas y ademas le quita espacios en blanco y verifica si los caracteres son validos
        correo_normalizado = self.normalize_email(correo)

        nuevo_usuario = self.model(correo = correo_normalizado, nombre = nombre, apellido = apellido, tipoUsuario = tipoUsuario)

        # generamos el hash de nuestra password
        nuevo_usuario.set_password(password)
        nuevo_usuario.is_superuser = True
        nuevo_usuario.isstaff = True
        nuevo_usuario.save()

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.TextField(null=True)
    correo = models.EmailField(max_length=100, unique=True, null=False)
    password = models.TextField(null=False)
    # CharField => varchar(Limite)
    # TextField => 
    tipoUsuario = models.TextField(choices=[('ADMIN','ADMIN'),('CLIENTE','CLIENTE')], db_column='tipo_usuario')

    # campos netamente de auth_user
    # is_staf => sirve para indicar al panel administrativo que el usuario no pertenece al grupo de usuarios que pueden acceder
    is_staff = models.BooleanField(default=False)
    # is_active => sirve para indicar que el usuario esta activo y por ende puede ingresar al panel administrativo
    is_active = models.BooleanField(default=True)

    # si queremos ingresar al panel administrativo tenemos que indicar que columna usara para pedir el nombre de usuario
    USERNAME_FIELD = 'correo'
    # cuando querramos crear un superusuario por el terminal tendremos que indiocar que atributos son los que nos debe solicitar
    # el correo no va porque ya esta definido en USERNAME_FIELD y si lo volvemos a pener nos dara un eror, y el password es ya solicitado de manera automatica
    REQUIRED_FIELDS = ['nombre', 'apellido','tipoUsuario'] 

    objetcs = ManejoUsuario()
    class Meta:
        db_table = 'usuarios'