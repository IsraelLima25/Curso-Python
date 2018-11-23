#trabalhando com arquivos

'''
arq = open('meu_arquivo.txt','w')
arq.write('novo\n')
arq.write('outra linha')
arq.close()
'''

'''
with para não necessita usar o close obrigatoriamente, pois o mesmo já
fecha o arquivo, tanto para escrever quanto para lê.
with 'meu_arquivo.txt' as arq:
    for linha in arq.readlines():
    print(linha)
'''        

arq = open('meu_arquivo.txt','r')
for linha in arq.readlines():
    print(linha)
    
arq.close()

dicio ={}
arq = open('dados.txt','r')
for linha in arq.readlines:
    dados = linha[:-1].split(',')
    chave = dicio[0]
    chave = dicio[1]
    valor = int(dados[1])
    dicio[chave] = valor
    arq.close()
    
print(dicio)
