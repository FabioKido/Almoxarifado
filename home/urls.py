from django.urls import path
from .views import home, Logout_View

urlpatterns = [
    path('', home, name="home"),
    #path('logout/', Logout_View, name='logout'),
]
