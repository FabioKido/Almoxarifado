from rest_framework.viewsets import ModelViewSet
from requisitar.models import RequisicaoMateriais
from .serializers import RequisicaoMateriaisSerializer

class RequisitarViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = RequisicaoMateriais.objects.all()
    serializer_class = RequisicaoMateriaisSerializer
