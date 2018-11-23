num='0'
while num != 'fim':
    num = input('Digite um numero:')
    if num=='fim':
        break
    elif int(num)%2==0:
        print('par')
    else:
        print('impar')


        


