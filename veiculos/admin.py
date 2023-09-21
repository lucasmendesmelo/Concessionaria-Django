from django.contrib import admin
from .models import Veiculo

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'modelo', 'ano_fabricacao', 'tipo', 'cor', 'estado', 'km_rodados', 'passagem_leilao', 'formas_pagamento', 'imagem')
    list_filter = ('tipo', 'estado', 'passagem_leilao', 'formas_pagamento')
    search_fields = ('id', 'marca', 'modelo')
    ordering = ('marca', 'modelo')

admin.site.register(Veiculo, VeiculoAdmin)
