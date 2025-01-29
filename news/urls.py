from django.urls import path
from news.views import home, articoloDetailView, listaArticoli,queryBase,giornalistaDetailView,index_root,index

app_name = 'news'

urlpatterns=[
    path('',home,name="homeview"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli"),
    path("lista_articoli", listaArticoli, name="lista_articoli"),
    path("giornalisti/<int:pk>", giornalistaDetailView, name="giornalista_detail"),
    path("queryBase", queryBase, name="queryBase"),
    path('index',index, name="index"),
    path('index_root',index_root, name="index_root"),
]
