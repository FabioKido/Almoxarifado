from django.contrib import admin
from .models import Endereco
from .models import Telefone
from .models import Fornecedor
from .models import Departamento
from .models import Requisitante

# Register your models here.

admin.site.register(Endereco)
admin.site.register(Telefone)
admin.site.register(Fornecedor)
admin.site.register(Departamento)
admin.site.register(Requisitante)
