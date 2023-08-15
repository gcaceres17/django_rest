from rest_framework import serializers
from inmueble_list_app.models import Comentarios, Edificacion, Empresa

class ComentarioSerializer(serializers.ModelSerializer):
    comentario_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comentarios
        fields = '__all__'


class EdificacionSerializer(serializers.ModelSerializer):
    comentariolist = ComentarioSerializer(many=True, read_only = True)
    class Meta:
        model = Edificacion
        fields = '__all__'



class EmpresaSerializer(serializers.ModelSerializer):
    #edificacionlist = EdificacionSerializer(many=True, read_only = True)
    edificacionlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='edificacion-detail'
    )
    class Meta:
        model = Empresa
        fields = '__all__'


