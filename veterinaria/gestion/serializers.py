from rest_framework.serializers import ModelSerializer
from .models import Usuario, Mascota

class RegistroUsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class MascotasSerializer(ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

    # https://www.django-rest-framework.org/api-guide/relations/#generic-relationships
    def to_representation(self, instance):
        print(instance.foto.url)
        representacion = super().to_representation(instance)
        representacion['foto'] = instance.foto.url
        return representacion