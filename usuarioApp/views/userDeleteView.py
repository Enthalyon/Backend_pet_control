from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from usuarioApp.models.usuario import User
from usuarioApp.serializers.usuarioSerializer import UsuarioSerializer

class UserDeleteView(generics.RetrieveAPIView):
    permission_classes =[IsAuthenticated]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None
    
    def delete(self, request, *args, **kwargs ):
        branch_instance= self.get_object(kwargs['pk'])
        if not branch_instance:
            return Response(
                {"res":"Usuario con el id no existe"},
                status=status.HTTP_400_BAD_REQUEST
            )
        branch_instance.delete()
        return Response(
            {"res":"El usuario fue eliminado!"},
            status=status.HTTP_200_OK   
            )