while 1 == 1:
    ctr = 0
    ctd = 2
    numero = int(input('Digite o número: '))
    if numero > 1:
	    while ctr == 0 and ctd <= numero**1/2:
	        if numero%ctd == 0:
	            ctr = 1
	        ctd += 1
	    if ctr == 0:
	        print('É um número primo')
	    else:
	        print('Não é um número primo')
    else:
    	print('Não é um número primo')
