from django.urls import path
from inmueble_list_app.api.views import ComentariosListAV, ComentariosDetail, EdificacionListAV, EdificacionDetailAV, EmpresaListAV, EmpresaDetailAV, ComentariosCreate


urlpatterns = [
    path('edificacion/', EdificacionListAV.as_view(), name='list'),
    path('edificacion/<int:pk>/', EdificacionDetailAV.as_view(), name='edificacion-detail'),
    
    path('empresa/', EmpresaListAV.as_view(), name='Empresa'),
    path('empresa/<int:pk>/', EmpresaDetailAV.as_view(), name='empresa-detail'),
    
    path('edificacion/<int:pk>/comentario/', ComentariosListAV.as_view(), name='comentario-list'),
    path('edificacion/<int:pk>/comentario-create/', ComentariosCreate.as_view(), name='comentario-create'),
    path('edificacion/comentario/<int:pk>', ComentariosDetail  .as_view(), name='comentario-detail'),
]
