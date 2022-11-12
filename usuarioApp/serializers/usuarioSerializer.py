from rest_framework import serializers
from usuarioApp.models.usuario import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nombres', 'apellidos', 'ciudad', 'password', 'departamento', 'direccion', 'email', 'telefono']