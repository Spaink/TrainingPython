def gera_nome_convite(nome_convidado):
    posicao_final = len(nome_convidado)
    posicao_inicial = posicao_final - 4
    parte1 = nome_convidado[0:4]
    parte2 = nome_convidado[posicao_inicial:posicao_final]
    return parte1 + ' ' + parte2

def envia_convite(nome_convidado):
    nome_formatado = gera_nome_convite(nome_convidado)
    print "Enviando convite para %s" %(nome_formatado)

def processa_convite(nome_convidado):
    nome_formatado = gera_nome_convite(nome_convidado)
    envia_convite(nome_formatado)

def cadastrar(nomes):
   print 'Digite o nome:'
   nome = raw_input()
   nomes.append(nome)
 

def remover(nomes):
    print 'Informe o nome que quer remover:'
    nome = raw_input()
    nomes.remove(nome)
    