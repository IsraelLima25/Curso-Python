#coding: utf-8

txt = input('Informe o número a ser descoberto: ')
escondido = int(txt)
if escondido >= 0 and escondido <= 100:
    inferior = 0
    superior = 100
    vezes = 0    
    while True:
        vezes += 1
        txt = input('Faça uma tentativa: ')
        tentativa = int(txt)
        if tentativa < inferior or tentativa > superior:
            print('Você perdeu! Número fora da faixa.')
            break
        elif tentativa < escondido:
            print('É maior.')
            inferior = tentativa
        elif tentativa > escondido:
            print('É menor.')
            superior = tentativa
        else:
            print('Você acertou! Foram ' + str(vezes) + ' tentativas.')
            break            
else:
    print('Número tem que ser de zero a cem.')
