from django.db import models

class Veiculo(models.Model):
    TIPO_CHOICES = (
        ('carro', 'Carro'),
        ('moto', 'Moto'),
    )

    ESTADO_CHOICES = (
        ('novo', 'Novo'),
        ('usado', 'Usado'),
    )

    PAGAMENTO_CHOICES = (
        ('avista', 'À Vista'),
        ('parcelado', 'Parcelado'),
    )

   
    imagem = models.ImageField(upload_to='veiculos/', null=True, blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)  
    cor = models.CharField(max_length=255)  
    marca = models.CharField(max_length=255)  
    modelo = models.CharField(max_length=255)  
    ano_fabricacao = models.PositiveIntegerField()  
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)  
    km_rodados = models.PositiveIntegerField()  
    passagem_leilao = models.BooleanField(default=False)  
    formas_pagamento = models.CharField(max_length=10, choices=PAGAMENTO_CHOICES)  

    def __str__(self):
        return self.modelo
