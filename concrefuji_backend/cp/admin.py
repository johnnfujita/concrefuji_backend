from django.contrib import admin
from .models import Empresa, CP, CPGroup, Obra
# Register your models here.
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['name', 'cnpj','created' ]

@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):
    list_display = ['empresa','name', 'manager', 'address', 'cidade', 'created', 'is_active']
    list_filter = ['empresa', 'cidade']

class CPInline(admin.TabularInline):
    model = CP
   

@admin.register(CPGroup)
class CPGroupAdmin(admin.ModelAdmin):
    list_display = ['tipo_cp', 'created', 'obra', 'numero_cp', 'nota_fiscal', 'hora_da_usina', 'hora_da_moldagem', 'traco', 'abatimento', 'local_da_aplicacao', 'aprovado']
    list_filter = ['obra', 'aprovado', 'tipo_cp',  'local_da_aplicacao']
    list_editable = ['aprovado']
    inlines = [CPInline]