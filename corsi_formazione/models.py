from django.db import models
from datetime import datetime

# Modello Corso

class Corso(models.Model):
    titolo=models.CharField(max_length=20)
    descrizione=models.TextField()
    data_inizio=models.DateField(default=datetime.now(),blank=True)
    data_fine=models.DateField(default=datetime.now(),blank=True)
    posti_disponibili=models.IntegerField(default=0)

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name = "Corso"
        verbose_name_plural = "Corsi"
    
