#Importaciones
from rest_framework.response import Response
from rest_framework.views import APIView
from inmueble_list_app.api.serializers import EdificacionSerializer, EmpresaSerializer, ComentarioSerializer
from rest_framework.views import status
from inmueble_list_app.models import Comentarios, Edificacion, Empresa
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from inmueble_list_app.api.permissions import AdminOrReadOnly

class ComentariosCreate(generics.CreateAPIView):
    serializer_class = ComentarioSerializer
    
    def get_queryset(self):
        return Comentarios.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        inmueble = Edificacion.objects.get(pk=pk)
        
        user = self.request.user
        comentario_queryset = Comentarios.objects.filter(edificacion = inmueble, comentario_user = user)

        if comentario_queryset.exists():
            raise ValidationError("El usuario ya escribio un comentario para este inmueble")
        
        if inmueble.number_calificacion == 0:
            inmueble.avg_calificacion = serializer.validated_data['calificacion']
        else:
            inmueble.avg_calificacion = (serializer.validated_data['calificacion'] + inmueble.avg_calificacion) /2
            
        inmueble.number_calificacion = inmueble.number_calificacion + 1
        inmueble.save() 
            
        serializer.save(edificacion=inmueble, comentario_user=user)
#Generic Class 
class ComentariosListAV(generics.ListCreateAPIView):
    #queryset = Comentarios.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comentarios.objects.filter(edificacion=pk)
        
    
class ComentariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentarioSerializer

    
# Obtiene la lista de datos de las empresas creadas
class EmpresaListAV(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True, context = {'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtiene la lista de datos de las empresas creadas indiviualmente
class EmpresaDetailAV(APIView):
    def get(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializaer = EmpresaSerializer(empresa)
        return Response(serializaer.data)
    
    def put(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmpresaSerializer(empresa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    def delete(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Obtiene la lista de datos de los edificacions
class EdificacionListAV(APIView):
    
    def get(self, request):
        edificacions = Edificacion.objects.all()
        serializer = EdificacionSerializer(edificacions, many=True, context = {'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EdificacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#obtiene los datos de los edificacions individualmente
class EdificacionDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'error': 'Edificacion no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializaer = EdificacionSerializer(edificacion)
        return Response(serializaer.data)
    
    def put(self, request, pk):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'error': 'Edificacion no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EdificacionSerializer(edificacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    def delete(self, request, pk):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'error': 'Edificacion no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        edificacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)