from django.db import models

class Evento(models.Model):
    titolo=models.CharField(max_length=100)
    data=models.DateField()
    descrizione=models.TextField()
    partecipanti=models.IntegerField()

    def __str__(self):
        return self.titolo+ " " +self.data
    
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventi"


