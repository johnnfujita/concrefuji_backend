from rest_framework import serializers
from .models import Empresa, Obra, CPGroup, CP
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'username', 
            'password', 
            'token'
        )
        
    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance

class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = [
            'id',
            'cnpj',
            'name'
        ]

    

class ObraSerializer(serializers.ModelSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='name')
    class Meta:
        model = Obra
        fields = [
            'id',
            'address',
            'name',
            'manager',
            'cidade',
            'empresa'
        ]

    

class CPSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = CP
        fields = [
            'id',
            'cp_group',
            'carga',
            'idade_rompimento',
            'data_rompimento'            
        ]
        read_only_fields = ('cp_group',)

class CPGroupSerializer(serializers.ModelSerializer):
    obra = serializers.SlugRelatedField(queryset=Obra.objects.all(), slug_field='name')
    cps = CPSerializer(many=True)
    class Meta:
        model = CPGroup
        fields = [
            'id',
            'tipo_cp',
            'numero_cp',
            'obra',
            'nota_fiscal',
            'hora_da_usina',
            'hora_da_moldagem',
            'traco',
            'abatimento',
            'local_da_aplicacao',
            'cps',
            'aprovado'
        ]

    def create(self, validated_data):
        cps = validated_data.pop('cps')
        cp_group = CPGroup.objects.create(**validated_data)
        for cp in cps:
            CP.objects.create(**cp, cp_group=cp_group)
        return cp_group

    def update(self, instance, validated_data):
        cps = validated_data.pop('cps')
        instance.tipo_cp = validated_data.get('tipo_cp', instance.tipo_cp)
        instance.obra = validated_data.get('obra', intance.obra)                
        instance.nota_fiscal, = validated_data.get('nota_fiscal', instance.nota_fiscal)
        instance.hora_da_usina = validated_data.get('hora_de_usina', instance.hora_da_usina)
        instance.hora_da_moldagem = validated_data.get('hora_de_moldagem', instance.hora_da_moldagem)
        instance.traco = validated_data.get('traco', instance.traco)
        instance.abatimento = validated_data.get('abatimento', instance.abatimento)
        instance.local_da_aplicacao = validated_data.get('local_da_aplicacao', local_da_aplicacao)
        instance.save()
        keep_cps = []
        existing_cps_ids = [cp.id for cp in instance.cps]
        for cop in cops:
            if "id" in cop.keys():
                if CP.objects.filter(id=cop["id"]).exists():
                    c = CP.objects.get(id=cop["id"])
                    c.carga = cop.get('carga', c.carga)
                    c.idade_rompimento = cop.get('idade_rompimento', c.idade_rompimento)
                    keep_cps.append(c.id)
                else:
                    continue
            else:
                c = CP.objects.create(**cop, cp_group=instance)
                keep_cps.append(c.id)
        for cps in instance.cps:
            if cp.id not in keep_cps:
                cp.delete()
        return instance