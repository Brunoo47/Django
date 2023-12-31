from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import render
from rest_framework import viewsets
from core.serializers import RegistroPacienteSerializer, RegistroUsuarioSerializer, OcorrenciaTipoSerializer, ProblemasEncontradosSerializer, AvaliacaoGlassGOWSerializer, AvaliacaoGlassGOW_KidsSerializer, Sinais_e_SintomasSerializer, Sinais_VitaisSerializer, localizacao_dos_traumasSerializer, QueimaduraSerializer, VitimiaSerializer, DecisaoTransporteObjetosRecolhidosSerializer, Procedimentos_efetuadosSerializer, SinaisSintomasSerializer, MateriaisSerializer, AnamneseEmergenciaMedicaSerializer, AnamneseGestacionalSerializer, AvaliacaodacinematicaeObsImportantesSerializer, registrarocorrenciaSerializer
from core.models import RegistroPaciente, RegistroUsuario, OcorrenciaTipo, ProblemasEncontrados, AvaliacaoGlassGOW, AvaliacaoGlassGOW_Kids, Sinais_e_Sintomas, Sinais_Vitais, localizacao_dos_traumas, Queimadura, Vitimia, DecisaoTransporteObjetosRecolhidos, Procedimentos_efetuados, SinaisSintomas, Materiais, AnamneseEmergenciaMedica, AnamneseGestacional, AvaliacaodacinematicaeObsImportantes, registrarocorrencia

class RegistroUsuarioViewSet(viewsets.ModelViewSet):
    queryset = RegistroUsuario.objects.all()
    serializer_class = RegistroUsuarioSerializer


class RegistroPacienteViewSet(viewsets.ModelViewSet):
    queryset = RegistroPaciente.objects.all()
    serializer_class = RegistroPacienteSerializer


class OcorrenciaTipo(viewsets.ModelViewSet):
    queryset = OcorrenciaTipo.objects.all()
    serializer_class = OcorrenciaTipoSerializer


class ProblemasEncontrados(viewsets.ModelViewSet):
    queryset = ProblemasEncontrados.objects.all()
    serializer_class = ProblemasEncontradosSerializer


class AvaliacaoGlassGOW(viewsets.ModelViewSet):
    queryset = AvaliacaoGlassGOW.objects.all()
    serializer_class = AvaliacaoGlassGOWSerializer


class AvaliacaoGlassGOW_Kids(viewsets.ModelViewSet):
    queryset = AvaliacaoGlassGOW_Kids.objects.all()
    serializer_class = AvaliacaoGlassGOW_KidsSerializer


class Sinais_e_Sintomas(viewsets.ModelViewSet):
    queryset = Sinais_e_Sintomas.objects.all()
    serializer_class = Sinais_e_SintomasSerializer


class Sinais_Vitais(viewsets.ModelViewSet):
    queryset = Sinais_Vitais.objects.all()
    serializer_class = Sinais_VitaisSerializer


class localizacao_dos_traumas(viewsets.ModelViewSet):
    queryset = localizacao_dos_traumas.objects.all()
    serializer_class = localizacao_dos_traumasSerializer


class Queimadura(viewsets.ModelViewSet):
    queryset = Queimadura.objects.all()
    serializer_class = QueimaduraSerializer


class Vitimia(viewsets.ModelViewSet):
    queryset = Vitimia.objects.all()
    serializer_class = VitimiaSerializer


class DecisaoTransporteObjetosRecolhidos(viewsets.ModelViewSet):
    queryset = DecisaoTransporteObjetosRecolhidos.objects.all()
    serializer_class = DecisaoTransporteObjetosRecolhidosSerializer


class Procedimentos_efetuados(viewsets.ModelViewSet):
    queryset = Procedimentos_efetuados.objects.all()
    serializer_class = Procedimentos_efetuadosSerializer


class SinaisSintomas(viewsets.ModelViewSet):
    queryset = SinaisSintomas.objects.all()
    serializer_class = SinaisSintomasSerializer


class Materiais(viewsets.ModelViewSet):
    queryset = Materiais.objects.all()
    serializer_class = MateriaisSerializer


class AnamneseEmergenciaMedica(viewsets.ModelViewSet):
    queryset = AnamneseEmergenciaMedica.objects.all()
    serializer_class = AnamneseEmergenciaMedicaSerializer


class AnamneseGestacional(viewsets.ModelViewSet):
    queryset = AnamneseGestacional.objects.all()
    serializer_class = AnamneseGestacionalSerializer


class AvaliacaodacinematicaeObsImportantes(viewsets.ModelViewSet):
    queryset = AvaliacaodacinematicaeObsImportantes.objects.all()
    serializer_class = AvaliacaodacinematicaeObsImportantesSerializer

class registrarocorrencias(viewsets.ModelViewSet):
    queryset = registrarocorrencia.objects.all()
    serializer_class = registrarocorrenciaSerializer
    
    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = registrarocorrencia.objects.filter(id=id)
        return queryset


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['id'] = self.user.id
        data['email'] = self.user.email
        data['is_superuser'] = self.user.is_superuser

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
