from django.db import models
from django.contrib.auth.models import User

class Evenement(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_evenement = models.DateTimeField()

    def __str__(self):
        return self.titre

class Participation(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('evenement', 'utilisateur')
