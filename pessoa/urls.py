from django.urls import path
from .views import ListaPessoa


urlpatterns = [
    path('', ListaPessoa.as_view(), name='pessoa.index')

]
