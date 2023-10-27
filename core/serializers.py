from core.models import RegistroPaciente, RegistroUsuario, OcorrenciaTipo, ProblemasEncontrados, AvaliacaoGlassGOW, AvaliacaoGlassGOW_Kids, Sinais_e_Sintomas, Sinais_Vitais, localizacao_dos_traumas, Queimadura, Vitimia, DecisaoTransporteObjetosRecolhidos, Procedimentos_efetuados, SinaisSintomas, Materiais, AnamneseEmergenciaMedica, AnamneseGestacional, AvaliacaodacinematicaeObsImportantes
from rest_framework import serializers


class RegistroPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroPaciente
        fields = '__all__'


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroUsuario
        fields = '__all__'


class OcorrenciaTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OcorrenciaTipo
        fields = '__all__'


class ProblemasEncontradosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemasEncontrados
        fields = '__all__'


class AvaliacaoGlassGOWSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliacaoGlassGOW
        fields = '__all__'


class AvaliacaoGlassGOW_KidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliacaoGlassGOW_Kids
        fields = '__all__'


class Sinais_e_SintomasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinais_e_Sintomas
        fields = '__all__'


class Sinais_VitaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinais_Vitais
        fields = '__all__'


class localizacao_dos_traumasSerializer(serializers.ModelSerializer):
    class Meta:
        model = localizacao_dos_traumas
        fields = '__all__'


class QueimaduraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queimadura
        fields = '__all__'


class VitimiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitimia
        fields = '__all__'


class DecisaoTransporteObjetosRecolhidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecisaoTransporteObjetosRecolhidos
        fields = '__all__'


class Procedimentos_efetuadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimentos_efetuados
        fields = '__all__'


class SinaisSintomasSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinaisSintomas
        fields = '__all__'


class MateriaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materiais
        fields = '__all__'


class AnamneseEmergenciaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnamneseEmergenciaMedica
        fields = '__all__'


class AnamneseGestacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnamneseGestacional
        fields = '__all__'


class AvaliacaodacinematicaeObsImportantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliacaodacinematicaeObsImportantes
        fields = '__all__'
