while True:
    numero = int(input('Digite o número: '))
    for contador in range(2,numero):
        numero *= contador
    print('O fatorial é {}'.format(numero))
