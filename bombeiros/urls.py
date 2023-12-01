from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from core.views import MyTokenObtainPairView, RegistroPacienteViewSet, registrarocorrencias, RegistroUsuarioViewSet, AnamneseGestacional, AnamneseEmergenciaMedica, OcorrenciaTipo, ProblemasEncontrados, AvaliacaoGlassGOW, AvaliacaoGlassGOW_Kids, Sinais_e_Sintomas, Sinais_Vitais, SinaisSintomas, localizacao_dos_traumas, Queimadura, Vitimia, DecisaoTransporteObjetosRecolhidos, Procedimentos_efetuados, Materiais, AvaliacaodacinematicaeObsImportantes

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = routers.DefaultRouter()
router.register(r'registroPaciente', RegistroPacienteViewSet)
router.register(r'registroUsuario', RegistroUsuarioViewSet)
router.register(r'registroEmergenciaMedica', AnamneseEmergenciaMedica)
router.register(r'registroOcorrenciaTipo', OcorrenciaTipo)
router.register(r'registroAnamneseGestacional', AnamneseGestacional)
router.register(r'registroProblemasEncontrados', ProblemasEncontrados)
router.register(r'registroAvaliacaoGlassGOW', AvaliacaoGlassGOW)
router.register(r'registroAvaliacaoGlassGOW_Kids', AvaliacaoGlassGOW_Kids)
router.register(r'registroSinais_e_Sintomas', Sinais_e_Sintomas)
router.register(r'registroSinais_Vitais', Sinais_Vitais)
router.register(r'registroSinaisSintomas', SinaisSintomas)
router.register(r'registrolocalizacao_dos_traumas', localizacao_dos_traumas)
router.register(r'registroQueimadura', Queimadura)
router.register(r'registroVitimia', Vitimia)
router.register(r'registroDecisaoTransporteObjetosRecolhidos',
                DecisaoTransporteObjetosRecolhidos)
router.register(r'registroProcedimentos_efetuados', Procedimentos_efetuados)
router.register(r'registroMateriais', Materiais)
router.register(r'registroAvaliacaodacinematicaeObsImportantes', AvaliacaodacinematicaeObsImportantes)
router.register(r'registroOcorrencias', registrarocorrencias)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"),
         name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path('', include(router.urls)),
]
