sigla = input('Digite a sigla:')
if (sigla=='ba'):
    estado='Bahia'
elif (sigla=='se'):
    estado='Sergipe'
elif (sigla=='al'):
    estado='Alagoas'
    
elif (sigla=='pb'):
    estado='Paraiba'
elif (sigla=='pe'):
    estado='Pernambuco'
elif (sigla=='rn'):
    estado='Rio Grande do Norte'
elif (sigla=='ce'):
    estado='Ceara'
elif (sigla=='pi'):
    estado='piaui'
elif (sigla=='ma'):
    estado='Maranhão'    
else:
    estado = 'Desconhecido'

print('O estado é ' + estado)
