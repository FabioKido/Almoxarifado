from django.urls import path
from .views import newMateriais

urlpatterns = [
    path('', newMateriais, name="newMateriais"),
]
