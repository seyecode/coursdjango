from django.db import models

# Create your models here.

class Etudiant(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=70)
    age = models.IntegerField()
    ecole = models.CharField(max_length=20)