#Implementar funcao para CRUD em arquivo

def criar(chave,valor):
    if not (chave in dicio):
        dicio[chave] = valor        
    else:
        print("Esta chave já existe")             

def ler(chave):
    if chave in dicio:
        print('Valor inserido é' + dicio[chave])
    else:
        print('Chave não encontrada')

def atualizar(chave,valor):
    if chave in dicio:
       dicio[chave] = valor
       print('valor atualizado')
    else:
        print('Chave não encontrada')

def deletar(chave):
    if (chave in dicio):
        del(dicio[chave])
    else:
        print('Chave não encontrada')

def listar():
    for chave in dicio.keys():
        print(chave,dicio[chave])
        
    
dicio = {}


while True:    
    
    comand = input("Digite o comando")
    if(comand=='c'):
        chav = input("Digite a chave")
        vlr = input("Digite o valor")
        criar(chav,vlr)
    elif comand=='r':
        chave = input("Digite a chave")
        ler(chave)
    elif comand=='u':
        chav = input("Digite a chave")
        vlr = input("Digite o valor")
        atualizar(chav,vlr)
        
    elif comand=='d':
        chav = input("Digite a chave")
        deletar(chav)

    elif comand=='l':
        listar()                 
            
    elif comand=='s':
        break

print(dicio)

        
