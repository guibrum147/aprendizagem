numero = int(input('Digite o número: '))
maior = numero
menor = numero
soma = numero
contador = 1
escolha = str(input('Continuar? [S/N]: '))
escolha = escolha.upper()
while escolha == 'S':
    numero = int(input('Digite o número: '))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    soma += numero
    contador += 1
    escolha = str(input('Continuar? [S/N]: '))
    escolha = escolha.upper()
print('Dentre {} número(s), o menor foi {}, o maior foi {} e a média foi {}'.format(contador, menor, maior, (soma/contador)))
