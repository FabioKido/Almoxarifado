from django.forms import ModelForm
from .models import Material

class materialForm(ModelForm):
    class Meta:
        model = Material
        fields = ['descricao', 'valorUnitario', 'tipo', 'imagen']
