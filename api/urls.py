from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('lihat-data/', views.lihatData, name='lihat-data'),
        path('buat-data/', views.buatData, name='buat-data'),
        path('ubah-data/<str:pk>/', views.ubahData, name='ubah-data'),
        path('hapus-data/<str:pk>/', views.hapusData, name='hapus-data'),
]
