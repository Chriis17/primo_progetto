from django.urls import path
from seconda_app.views import es_if,if_else_elif,index,index_root

app_name="seconda_app"
urlpatterns=[
    path('es_if',es_if,name='es_if'),
    path('if_else_elif',if_else_elif,name='if_else_elif'),
    path('index',index, name="index"),
    path('index_root',index_root, name="index_root"),
]