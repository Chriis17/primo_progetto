from django.urls import path
from .views import view_a

app_name = 'eventi_scolastici'

urlpatterns=[
    path('view_a',view_a,name="view_a"),
]