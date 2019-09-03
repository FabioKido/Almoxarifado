from rest_framework.serializers import ModelSerializer
from requisitar.models import RequisicaoMateriais

class RequisicaoMateriaisSerializer(ModelSerializer):
    class Meta:
        model = RequisicaoMateriais
        fields = ('id', 'dataRegistro', 'condicao', 'observacoes', 'aprovado')
