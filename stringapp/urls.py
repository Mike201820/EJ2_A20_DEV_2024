# stringapp/urls.py
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from .views import max_f_value, get_all_calculations

urlpatterns = [
    path('max_f_value/', max_f_value, name='max_f_value'),
    path('calculations/', get_all_calculations, name='get_all_calculations'),
    path('docs/', include_docs_urls(title="doc APi"))
]

