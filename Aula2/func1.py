#empacotamento
def somar(*args):
    resultado=0
    for num in args:
        resultado += num
    return resultado

def funcao(outro,**kwargs):
    print(outro)
    print(kwargs['nome'])
    print(kwargs['cidade'])
#chamda da função    
funcao('234',cidade='ssa', nome='lc')


def listadepalavras(args):
    for l in args:
        resultado=l
        print(resultado)

def imprimir_letras(palavra):
    for p in palavra:
        print(p)
        
    

palavra = "abacate"
imprimir_letras(palavra)


'''

def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b
    

op = input("Operação")

escolha = int(op)

if  escolha==1:
    vl1 = input("Valor 1")
    vl2 = input("Valor 2")
    x = int(vl1)
    y = int(vl2)
    resultado = somar(x,y)
    print(resultado)
elif escolha==2:
     vl1 = input("Valor 1")
     vl2 = input("Valor 2")
     x = int(vl1)
     y = int(vl2)   
     resultado = subtrair(x,y)
     print(resultado)
         
elif escolha==3:
     vl1 = input("Valor 1")
     vl2 = input("Valor 2")
     x = int(vl1)
     y = int(vl2)
     resultado = multiplicar(x,y)
     print(resultado)

elif escolha==4:
     vl1 = input("Valor 1")
     vl2 = input("Valor 2")
     x = int(vl1)
     y = int(vl2)   
     resultado = dividir(x,y)
     print(resultado)
else:
     print("Valor Desconhecido")
    
'''


         



    
