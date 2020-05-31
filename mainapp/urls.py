from django.urls import path, include
from .views import Index, AddProduct, file_output, download


app_name = 'product'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('addnew/', AddProduct.as_view(), name='add'),
    path('outputfile', file_output, name='output'),
    path('downloadfile', download, name='download')
]