# -*- coding: UTF - 8 -*-

class Perfil(object):
    'Classe Padrão para perfis de Usuário'

    def  __init__(self,nome,telefone,empresa):
        if (len(nome) < 3):
            raise ArgumentoInvalidoErro('Nome deve ter pelo menos 3 caracteres')
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0
    
    def curtir(self):
        self.__curtidas += 1

    def obter_curtidas(self):
        return self.__curtidas

    @classmethod
    def gerar_perfis(classe,nome_arquivo):
        arquivo = open(nome_arquivo,'r')
        perfis = []
        for linha in arquivo:
            valores = linha.split(',')
            if(len(valores) is not 3):
                raise ValueError('Uma linha do %s deve ter pelo menos 3 valores' % nome_arquivo)
            perfis.append(classe(*valores))
        arquivo.close()
        return perfis    


    def imprimir(self):
        print 'Nome: %s, Telefone: %s, Empresa: %s, Curtidas: %s' %(self.nome,self.telefone,self.empresa,self.__curtidas)

class Perfil_Vip(Perfil):
    'Classe Padão para perfil de Usuário Vip'

    def __init__(self,nome,telefone,empresa,apelido = ''):
        super(Perfil_Vip,self).__init__(nome,telefone,empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(Perfil_Vip,self).obter_curtidas() * 10.0

class ArgumentoInvalidoErro(Exception):
    def __init__(self,mensagem):
        self.mensagem = mensagem

    def __str__(self):
        return repr(self.mensagem)

class Data(object):
    'Classe para formatar Datas'

    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprimir(self):
        print '%s / %s / %s' %(self.dia, self.mes, self.ano)

class Pessoa(object):
    'Classe para calcular o IMC'

    def __init__(self,nome,peso,altura):
        self.nome = nome 
        self.peso = float(peso)
        self.altura = float(altura)

    def imprimir(self):
        IMC = self.peso/(self.altura**2)
        print 'IMC de %s é %s' %(self.nome,IMC)       


