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

   # Campo para a imagem do veículo
    imagem = models.ImageField(upload_to='veiculos/', null=True, blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)  # Tipo do veículo (carro ou moto)
    cor = models.CharField(max_length=255)  # Cor do veículo
    marca = models.CharField(max_length=255)  # Marca do veículo
    modelo = models.CharField(max_length=255)  # Modelo do veículo
    ano_fabricacao = models.PositiveIntegerField()  # Ano de fabricação do veículo
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)  # Estado do veículo (novo ou usado)
    km_rodados = models.PositiveIntegerField()  # Quilometragem rodada do veículo
    passagem_leilao = models.BooleanField(default=False)  # Se possui passagem por leilão
    formas_pagamento = models.CharField(max_length=10, choices=PAGAMENTO_CHOICES)  # Formas de pagamento

    def __str__(self):
        return self.modelo
