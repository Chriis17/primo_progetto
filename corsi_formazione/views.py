from django.shortcuts import render,get_object_or_404
from corsi_formazione.models import Corso
import datetime

#view della pagina index
def indexCorsi(request):
    return render(request,"indexCorsi.html")

#view per la pagina che stampa l'elenco corsi per data
def view_a(request):
    elenco_corsi = Corso.objects.order_by('-data_inizio')
    context={"elenco_corsi":elenco_corsi}
    return render(request,"view_a.html",context)

#view per la pagina che stampa i dettagli di un corso
def view_b(request,pk):
    corso = get_object_or_404(Corso, pk=pk)
    context={"corso": corso}
    return render(request,"view_b.html",context)

#view per la pagina che stampa l'elenco dei corsi iniziati dopo il 01/05/2025
def view_c(request):
    elenco_corsi = Corso.objects.filter(data_inizio__gt=datetime.date(2025, 5, 1))
    context={"elenco_corsi":elenco_corsi}
    return render(request,"view_c.html",context)

#view per la pagina che stampa l'elenco dei corsi con almeno 20 posti disp
def view_d(request):
    elenco_corsi = Corso.objects.filter(posti_disponibili__lte=20)
    context={"elenco_corsi":elenco_corsi}
    return render(request,"view_d.html",context)

#view per la pagina che stampa l'elenco dei corsi finiti prima del 30/04/2025
def view_e(request):
    elenco_corsi = Corso.objects.filter(data_fine__lt=datetime.date(2025, 4, 30))
    context={"elenco_corsi":elenco_corsi}
    return render(request,"view_e.html",context)

#view per la pagina che stampa le specifiche avanzate: corso con minor e corso con maggior posti disponibili e somma dei posti disponibili di tutti i corsi
def view_f(request):
    corsoMax=Corso.objects.order_by('-posti_disponibili').first()
    corsoMin=Corso.objects.order_by('posti_disponibili').first()
    
    elenco_corsi=Corso.objects.all()
    tot=0
    for corso in elenco_corsi:
        tot+=corso.posti_disponibili
    
    context={"corsoMax":corsoMax,"corsoMin":corsoMin,"totPosti":tot}
    return render(request,"view_f.html",context)

