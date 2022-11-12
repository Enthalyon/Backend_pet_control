from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated


from usuarioApp.models.usuario import User
from usuarioApp.serializers.usuarioSerializer import UsuarioSerializer

class ActualizarUsuarioView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User()
    serializer_class = UsuarioSerializer
    
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None
    
    def put (self, request, *args, **kwargs):
        usuario_instancia = self.get_object(kwargs['pk'])
        if not usuario_instancia:
            return Response (
                {'El usuario no existe.'},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer = UsuarioSerializer(instance= usuario_instancia, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    