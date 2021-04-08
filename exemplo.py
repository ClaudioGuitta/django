no models

class ControleMeta(models.Model):

    TIPO_CHOICE = (
        ("Recolhimento","Recolhimento"),
        ("Lentidão","Lentidão"),
        ("Telefone","Telefone"),
        ("Configuração Estruturada","Configuração Estruuturada"),
        ("Los","Los"),
        ("Sinal Irregular","Sinal Irregular"),
        ("Sinal Irregular Interno","Sinal Irregular Interno"),
        ("Alteração de Cômodo","Alteração de Cômodo"),
        ("Alteração de Endereço","Alteração de Endereço"),
        ("Alteração de Endereço. Tel", "Alteração de Endereço. Tel"),
        ("Cabo de Rede", "Cabo de Rede"),
        ("Instalação Internet", "Instalação Internet"),
        ("Instalação Telefonica", "Instalação Telefonica"),
        ("Instalação Internet + Tel.", " Instalação Internet + Tel."),
        ("Troca de ONU", "Troca de ONU"),

    )

    tipo = models.CharField("Tipo", max_length=255, choices=TIPO_CHOICE)
    pontuacao = models.DecimalField(null=True,blank=True,max_digits = 10,decimal_places=1)
    obs = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to="media/%Y/%m/%D", null=True,blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now)
    cod_client = models.IntegerField('código do cliente',null=False,blank=False)

    def __str__(self):
        return self.tipo



na view

class ControleMeta(models.Model):

    TIPO_CHOICE = (
        ("Recolhimento","Recolhimento"),
        ("Lentidão","Lentidão"),
        ("Telefone","Telefone"),
        ("Configuração Estruturada","Configuração Estruuturada"),
        ("Los","Los"),
        ("Sinal Irregular","Sinal Irregular"),
        ("Sinal Irregular Interno","Sinal Irregular Interno"),
        ("Alteração de Cômodo","Alteração de Cômodo"),
        ("Alteração de Endereço","Alteração de Endereço"),
        ("Alteração de Endereço. Tel", "Alteração de Endereço. Tel"),
        ("Cabo de Rede", "Cabo de Rede"),
        ("Instalação Internet", "Instalação Internet"),
        ("Instalação Telefonica", "Instalação Telefonica"),
        ("Instalação Internet + Tel.", " Instalação Internet + Tel."),
        ("Troca de ONU", "Troca de ONU"),

    )

    tipo = models.CharField("Tipo", max_length=255, choices=TIPO_CHOICE)
    pontuacao = models.DecimalField(null=True,blank=True,max_digits = 10,decimal_places=1)
    obs = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to="media/%Y/%m/%D", null=True,blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now)
    cod_client = models.IntegerField('código do cliente',null=False,blank=False)

    def __str__(self):
        return self.tipo


no template

    {% for lista in pts %}
        {{lista.usuario.user_name}}{{lista.pontuacao}}
    {% endfor %}
