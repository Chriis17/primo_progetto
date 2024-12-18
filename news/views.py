from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista

def home(request):
    return render(request,"homepage.html")

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context={"articolo": articolo}
    return render(request, "articolo_detail.html", context)

# Create your views here.
