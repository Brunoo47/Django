from django.contrib import admin
from core.models import RegistroPaciente, RegistroUsuario, AnamneseEmergenciaMedica, AnamneseGestacional, ProblemasEncontrados, AvaliacaoGlassGOW, AvaliacaoGlassGOW_Kids, Sinais_e_Sintomas, Sinais_Vitais, SinaisSintomas, localizacao_dos_traumas, Queimadura, Vitimia, DecisaoTransporteObjetosRecolhidos, Procedimentos_efetuados, Materiais, AvaliacaodacinematicaeObsImportantes, registrarocorrencia

admin.site.register(RegistroUsuario)
admin.site.register(RegistroPaciente)
admin.site.register(AnamneseEmergenciaMedica)
admin.site.register(ProblemasEncontrados)
admin.site.register(AvaliacaoGlassGOW)
admin.site.register(AvaliacaoGlassGOW_Kids)
admin.site.register(Sinais_e_Sintomas)
admin.site.register(Sinais_Vitais)
admin.site.register(localizacao_dos_traumas)
admin.site.register(Queimadura)
admin.site.register(Vitimia)
admin.site.register(DecisaoTransporteObjetosRecolhidos)
admin.site.register(Procedimentos_efetuados)
admin.site.register(SinaisSintomas)
admin.site.register(Materiais)
admin.site.register(AnamneseGestacional)
admin.site.register(AvaliacaodacinematicaeObsImportantes)
admin.site.register(registrarocorrencia)



