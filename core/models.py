from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class RegistroPaciente(models.Model):
    titulo = models.CharField(max_length=100)
    pacienteNome = models.CharField(max_length=100, blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=9, blank=True, null=True)
    cpfOrRg = models.CharField(max_length=11, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    acompanhanteNome = models.CharField(max_length=100, blank=True, null=True)
    acompanhanteIdade = models.IntegerField(blank=True, null=True)
    descricao = models.TextField()
    localOcorrencia = models.CharField(max_length=100)
    publicadoEm = models.DateTimeField(default=timezone.now)
    criadoPor = models.ForeignKey(User, on_delete=models.CASCADE)
    equipe = models.CharField(max_length=100)


class RegistroUsuario(models.Model):
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()


class OcorrenciaTipo(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    deslizamento_desmoronamento = models.BooleanField(default=False)
    desabamento = models.BooleanField(default=False)
    queda_altura = models.BooleanField(default=False)
    queda_moto = models.BooleanField(default=False)
    queda_bicicleta = models.BooleanField(default=False)
    causa_animal = models.BooleanField(default=False)
    afogamento = models.BooleanField(default=False)
    atropelamento = models.BooleanField(default=False)
    esportivo = models.BooleanField(default=False)
    trabalho = models.BooleanField(default=False)
    transporte = models.BooleanField(default=False)
    emergencia_medica = models.BooleanField(default=False)
    suicidio = models.BooleanField(default=False)
    agressao = models.BooleanField(default=False)
    choque = models.BooleanField(default=False)
    domestico = models.BooleanField(default=False)
    intoxicacao = models.BooleanField(default=False)
    transferencia = models.BooleanField(default=False)
    outro = models.TextField(null=True)


class ProblemasEncontrados(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    psiquiatrico = models.BooleanField(default=False)
    respiratorio = models.BooleanField(default=False)
    diabeticos = models.BooleanField(default=False)
    obstetrico = models.BooleanField(default=False)
    outro = models.TextField(null=True)


class AvaliacaoGlassGOW(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    nenhuma = models.BooleanField(default=False)
    espontanea = models.BooleanField(default=False)
    comando_verbal = models.BooleanField(default=False)
    estimulo_boloroso = models.BooleanField(default=False)
    confuso = models.BooleanField(default=False)
    orientado = models.BooleanField(default=False)
    palavras_inapropriadas = models.BooleanField(default=False)
    palavras_incompreensiveis = models.BooleanField(default=False)
    obdece_comandos = models.BooleanField(default=False)
    localiza_a_dor = models.BooleanField(default=False)
    movimento_de_retirada = models.BooleanField(default=False)
    extensao_normal = models.BooleanField(default=False)


class AvaliacaoGlassGOW_Kids(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    nenhuma = models.BooleanField(default=False)
    espontanea = models.BooleanField(default=False)
    comando_verbal = models.BooleanField(default=False)
    estimulo_boloroso = models.BooleanField(default=False)
    orientado = models.BooleanField(default=False)
    nenhuma = models.BooleanField(default=False)
    palavras_inapropriadas = models.BooleanField(default=False)
    palavras_incompreensiveis = models.BooleanField(default=False)
    obdece_comandos = models.BooleanField(default=False)
    localiza_a_dor = models.BooleanField(default=False)
    movimento_de_retirada = models.BooleanField(default=False)
    extensao_normal = models.BooleanField(default=False)
    ausencia_flacida_hipotonia = models.BooleanField(default=False)
    nenhuma = models.BooleanField(default=False)


class Sinais_e_Sintomas(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    abdomen_sensivel_rigido = models.BooleanField(default=False)
    afundamento_cranio = models.BooleanField(default=False)
    agitacao = models.BooleanField(default=False)
    amnesia = models.BooleanField(default=False)
    apineia = models.BooleanField(default=False)
    angina_peito = models.BooleanField(default=False)
    bradicardia = models.BooleanField(default=False)
    bradipneia = models.BooleanField(default=False)
    bronco_aspirado = models.BooleanField(default=False)
    cefaleia = models.BooleanField(default=False)
    cianose = models.CharField(max_length=100)
    convulsao = models.BooleanField(default=False)
    desvio_traqueia = models.BooleanField(default=False)
    dor_local = models.BooleanField(default=False)
    edema = models.CharField(max_length=100)
    enfisema_subcutaneo = models.BooleanField(default=False)
    estase_jugular = models.BooleanField(default=False)
    face_palida = models.BooleanField(default=False)
    hemorragia = models.CharField(max_length=100)
    hipertensao = models.BooleanField(default=False)
    hipotensao = models.BooleanField(default=False)
    nauseas_vomitos = models.BooleanField(default=False)
    nasorogia = models.BooleanField(default=False)
    obito = models.BooleanField(default=False)
    otorreia = models.BooleanField(default=False)
    otorragia = models.BooleanField(default=False)
    ovace = models.BooleanField(default=False)
    parada = models.CharField(max_length=100)
    priaprismo = models.BooleanField(default=False)
    prurido_na_pele = models.BooleanField(default=False)
    pupilas = models.CharField(max_length=100)
    sede = models.BooleanField(default=False)
    sinal_de_battle = models.BooleanField(default=False)
    sinal_de_guaxinim = models.BooleanField(default=False)
    sudorese = models.BooleanField(default=False)
    taquipneia = models.BooleanField(default=False)
    taquicardia = models.BooleanField(default=False)
    tontura = models.BooleanField(default=False)
    outro = models.TextField()


class Sinais_Vitais(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    pressao_arterial1 = models.TextField()
    pressao_arterial2 = models.TextField()
    pulso = models.CharField(max_length=100)
    respiracao = models.CharField(max_length=100)
    saturação = models.CharField(max_length=100)
    hgt = models.CharField(max_length=100)
    temperatura = models.CharField(max_length=100)
    profissao1 = models.BooleanField(default=False)
    profissao2 = models.BooleanField(default=False)
    profissao3 = models.BooleanField(default=False)
    profissao4 = models.BooleanField(default=False)


class localizacao_dos_traumas(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    local = models.CharField(max_length=100)
    lado = models.CharField(max_length=100)
    face = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)


class Queimadura(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    grau = models.CharField(max_length=100)


class Vitimia(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    sentada = models.BooleanField(default=False)
    semiDeitada = models.BooleanField(default=False)
    ciclista = models.BooleanField(default=False)
    condutor_moto = models.BooleanField(default=False)
    gestante = models.BooleanField(default=False)
    pass_banco_da_frente = models.BooleanField(default=False)
    pass_moto = models.BooleanField(default=False)
    condutor_carro = models.BooleanField(default=False)
    clinico = models.BooleanField(default=False)
    trauma = models.BooleanField(default=False)
    pass_banco_de_tras = models.BooleanField(default=False)
    pedestre = models.BooleanField(default=False)


class DecisaoTransporteObjetosRecolhidos(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    critico = models.BooleanField(default=False)
    Potencialmente_instavel = models.BooleanField(default=False)
    instavel = models.BooleanField(default=False)
    estavel = models.BooleanField(default=False)
    objetos_recolhidos = models.TextField()


class Procedimentos_efetuados(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    procedimento_efetuado = models.TextField()
    aspiracao = models.BooleanField(default=False)
    avaliacao_digital = models.BooleanField(default=False)
    avaliacao_dirigida = models.BooleanField(default=False)
    avaliacao_continua = models.BooleanField(default=False)
    chave_de_rautek = models.BooleanField(default=False)
    canula_de_guedel = models.BooleanField(default=False)
    desobstrucao_de_vva = models.BooleanField(default=False)
    emprego_de_dea = models.BooleanField(default=False)
    gerenciamento_de_riscos = models.BooleanField(default=False)
    limpeza_de_ferimentos = models.BooleanField(default=False)
    curativos = models.BooleanField(default=False)
    compressivo = models.BooleanField(default=False)
    encravamento = models.BooleanField(default=False)
    ocular = models.BooleanField(default=False)
    queimadura = models.BooleanField(default=False)
    simples = models.BooleanField(default=False)
    tres_pontos = models.BooleanField(default=False)
    rolamento_sento_e_oitenta = models.BooleanField(default=False)
    tomada_de_decisao = models.BooleanField(default=False)
    tratado_de_choque = models.BooleanField(default=False)
    uso_de_canula = models.BooleanField(default=False)
    uso_colar = models.CharField(max_length=100)
    uso_ked = models.BooleanField(default=False)
    uso_ttf = models.BooleanField(default=False)
    ventilacao_de_suporte = models.BooleanField(default=False)
    oxigenioterapia = models.CharField(max_length=100)
    reanimador = models.CharField(max_length=100)
    meios_auxiliares = models.CharField(max_length=100)


class SinaisSintomas(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    imobilizacoes = models.CharField(max_length=100)
    maca_sobre_rodas = models.BooleanField(default=False)
    maca_rigida = models.BooleanField(default=False)
    ponte = models.BooleanField(default=False)
    retirado_capacete = models.BooleanField(default=False)
    rcp = models.BooleanField(default=False)
    rolamento_noventa_graus = models.BooleanField(default=False)
    outro = models.TextField()


class Materiais(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    ataduras = models.CharField(max_length=100)
    cateter_tp_oculos = models.BooleanField(default=False)
    kits = models.CharField(max_length=100)
    luvas_desc = models.BooleanField(default=False)
    manta_aluminizada = models.BooleanField(default=False)
    pas_do_dea = models.BooleanField(default=False)
    sonda_aspiracao = models.BooleanField(default=False)
    soro_fisiologico = models.BooleanField(default=False)
    telas_pap = models.CharField(max_length=100)
    base_estabiliza_colar = models.BooleanField(default=False)
    coxins_estabiliza = models.BooleanField(default=False)
    ked = models.CharField(max_length=100)
    ttf = models.CharField(max_length=100)
    tirante_aranha = models.BooleanField(default=False)
    tirate_cabeca = models.BooleanField(default=False)
    canula = models.BooleanField(default=False)


class AnamneseEmergenciaMedica(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    digite = models.TextField()
    aconteceu_outras_vezes = models.BooleanField(default=False)
    quanto_tempo_aconteceu = models.TextField()
    possui_problema_de_saude = models.BooleanField(default=False)
    quais = models.TextField()
    aleegico_a_alguma_coisa = models.BooleanField(default=False)
    se_sim_especifique = models.TextField()
    injeriu_alimento_ou_liquido = models.BooleanField(default=False)
    que_horas1 = models.CharField(max_length=100)
    que_horas2 = models.CharField(max_length=100)


class AnamneseGestacional(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    periodo_da_gestacao = models.TextField()
    fez_pre_natal: models.BooleanField(default=False)
    nome_do_medico = models.TextField()
    existe_probabilidade_de_complicacoes = models.BooleanField(default=False)
    primeiro_filho = models.BooleanField(default=False)
    quantos = models.TextField()
    que_horas_iniciaram_as_contracoes = models.TextField()
    duracao = models.TextField()
    intervalo = models.TextField()
    pressao_na_regiao_ou_vontade_de_evacuar = models.BooleanField(
        default=False)
    ouve_ruptura_da_bolsa = models.BooleanField(default=False)
    foi_feito_inspecao_visual = models.BooleanField(default=False)
    parto_foi_realizado = models.BooleanField(default=False)
    sexo_do_bebe = models.BooleanField(default=False)


class AvaliacaodacinematicaeObsImportantes(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    disturbio_de_comportamento = models.BooleanField(default=False)
    encontrado_capacete = models.BooleanField(default=False)
    para_brisas_avariado = models.BooleanField(default=False)
    caminhando_na_cena = models.BooleanField(default=False)
    painel_avariado = models.BooleanField(default=False)
    volante_torcido = models.BooleanField(default=False)
    obs = models.TextField()


class registrarocorrencia(models.Model):
    registroId = models.ForeignKey(
        RegistroPaciente, null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    acompanhante = models.BooleanField(default=False)
    local_da_ocorrencia = models.CharField(max_length=100)
    m = models.CharField(max_length=100)
    s1 = models.CharField(max_length=100)
    s2 = models.CharField(max_length=100)
    s3 = models.CharField(max_length=100)
    demandante = models.CharField(max_length=100)
    equipe = models.CharField(max_length=100)
    registroOcorrenciaTipo = models.ForeignKey(
        OcorrenciaTipo, null=True, on_delete=models.CASCADE)
    registroProblemasEncontrados = models.ForeignKey(
        ProblemasEncontrados, null=True, on_delete=models.CASCADE)
