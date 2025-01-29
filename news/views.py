from django.shortcuts import render, get_object_or_404
from news.models import Articolo, Giornalista

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context={"articolo": articolo}
    return render(request, "articolo_detail.html", context)

# Create your views here.
def listaArticoli(request,pk=None):
    if pk==None:
        articoli= Articolo.objects.all()
    else:
        articoli = Articolo.objects.filter(giornalista_id=pk)
    context={
            "articoli": articoli,
    }
    return render(request, "lista_articoli.html", context)

"""def home(request):
    a=""
    g=""
    for art in Articolo.objects.all():
        a += (art.titolo + "<br>")
    
    for gio in Giornalista.objects.all():
        g += (gio.nome + "<br>")
    response = "Articoli:<br>" + a + "<br>Giornalisti:<br>" + g

    return HttpResponse("<h1> Homepage news! </h1>")
"""
"""
def home(request):
    a=[]
    g=[]
    for art in Articolo.objects.all():
        a.append(art.titolo)
    
    for gio in Giornalista.objects.all():
        g.append(gio.nome)

    response = str(a) + "<br>" + str(g)
    print(response)
    
    return HttpResponse("<h1>"+ response +"</h1>")
"""
def home(request):
    
    articoli=Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti":giornalisti}
    print(context)
    
    return render(request,"homepage_news.html", context)

