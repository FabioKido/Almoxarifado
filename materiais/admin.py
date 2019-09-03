from django.contrib import admin
from .models import Unidade
from .models import Categoria
from .models import Material

# Register your models here.

admin.site.register(Unidade)
admin.site.register(Categoria)
admin.site.register(Material)
