from django.db import models

class Setor(models.Model):
    id = models.AutoField(primary_key=True)
    nome_setor = models.CharField(max_length=15)

    def __str__(self):
        return self.nome_setor
    
class Pessoa(models.Model):
    cpf = models.CharField(primary_key=True, max_length=12)
    nome_pessoa = models.CharField(max_length=25)
    idade = models.IntegerField()
    idsetor = models.ForeignKey(Setor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_pessoa
    
