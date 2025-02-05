from django.urls import path
from voti_app.views import view_a,view_b,view_c,view_d

app_name = 'voti_app'

urlpatterns=[
    path('lista_materie',view_a,name="lista_materie"),
    path('lista_voti',view_b,name="lista_voti"),
    path('media_studenti',view_c,name="media_studenti"),
    path('max_min',view_d,name="max_min"),
]