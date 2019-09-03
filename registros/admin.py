from django.contrib import admin
from .models import PedidoCompra
from .models import RecepcaoMateriais
from .models import RequisicaoMateriais
from .models import RetiradasMateriais
from .models import DevolucaoMateriais

# Register your models here.

admin.site.register(PedidoCompra)
admin.site.register(RecepcaoMateriais)
admin.site.register(RequisicaoMateriais)
admin.site.register(RetiradasMateriais)
admin.site.register(DevolucaoMateriais)
