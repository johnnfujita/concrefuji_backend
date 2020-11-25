from django.db import models


class Empresa(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    cnpj = models.CharField(max_length=18, blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Obra(models.Model):
    address = models.CharField(max_length=255, blank=False, default='')
    name = models.CharField(max_length=60, blank=False, null=False)
    empresa = models.ForeignKey(Empresa, related_name='obras', on_delete=models.CASCADE, blank=False, null=False)
    manager = models.CharField(max_length=60, blank=False, default='')
    cidade = models.CharField(max_length=100, blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Entidade corpo de prova 
class CPGroup(models.Model):
    CONCRETO = 'CON'
    GRAUTE = 'GRA'
    ARGAMASSA = 'ARG'
    CP_TYPES_CHOICES = [
        (CONCRETO, 'Concreto'),
        (GRAUTE, 'Graute'),
        (ARGAMASSA, 'Argamassa')
    ]

    tipo_cp = models.CharField(
        max_length=3,
        choices=CP_TYPES_CHOICES,
        default=CONCRETO
    )
    created = models.DateTimeField(auto_now_add=True)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, null=False, blank=False)
    numero_cp = models.PositiveIntegerField(null=False, blank=False)
    nota_fiscal = models.CharField(max_length=50, blank=False, default='')
    hora_da_usina = models.DateTimeField()
    hora_da_moldagem = models.DateTimeField()
    traco = models.DecimalField(decimal_places=3, max_digits=5)
    abatimento = models.PositiveIntegerField()
    local_da_aplicacao = models.CharField(max_length=255, blank=False, default='')
    aprovado = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'obraid-{self.obra}-cpid-{self.numero_cp}'

    @property
    def cps(self):
        return self.cp_set.all()

class CP(models.Model):
    cp_group = models.ForeignKey(CPGroup, on_delete=models.CASCADE, related_name='cps', null=False, blank=False)
    carga = models.DecimalField(decimal_places=3, max_digits=5, blank=True, null=True)
    idade_rompimento = models.PositiveSmallIntegerField(null=False, blank=False)
    data_rompimento = models.DateTimeField()

def __str__(self):
    return f'{self.cp_group}-cpgroup-{self.idade_rompimento}-idade'
    
