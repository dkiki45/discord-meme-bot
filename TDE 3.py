# ex - 1

#contador = 1

#while contador <= 99:
#    print(f'{contador}')
#    contador += 2

# ex - 2

#contador = 50

#while contador >= 0:
#    print(f'{contador}')
#    contador -= 5

# ex - 3

#contador = -100

#while contador <=100:
#    print(f'{contador}')
#    contador += 10

# ex - 4

#contador = 2

#while contador < 100:
#    if contador % 4 == 0:
#        print(contador)
#    contador += 1

# ex - 5

#numero_escolha = int(input('Digite um número: '))
#contador = 1

#while contador <= numero_escolha:
#    print(contador)
#    contador += 2

# ex - 6

#polegadas = int(input('Digite o número de polegadas (1-20): '))

#while polegadas < 1 or polegadas > 20:
#    polegadas = int(input('Digite um número válido (1-20): '))

#centimetros = polegadas * 2.54
#print(f'O número de polegadas que você digitou em centímetros é: {centimetros:.2f} cm.')

# ex - 7

#contador = 20

#while contador <= 160:
#    metros = contador * 1000
#    milhas = metros / 1609.344
#    print(f'{contador} km = {milhas:.0f} milhas' )
#    contador += 10

# ex - 8

#soma = 0
#quantidade = 10
#contador = 1

#print("Digite 10 números inteiros:")

#while contador <= quantidade:
#    numero = int(input(f"Digite o {contador}º número: "))
#    soma += numero
#    contador += 1

#media = soma / quantidade

#print(f"\nSoma dos números: {soma}")
#print(f"Média aritmética: {media:.2f}")

# ex - 9

#li = lf = 0

#while li >= lf:
#    li = int(input("Limite inicial (li): "))
#    lf = int(input("Limite final (lf): "))
#    if lf <= li:
#        print("Inicial deve ser menor que final.\n")

#print(f"\nMúltiplos de 3 entre {li} e {lf} (aberto):")
#contador = li + 1
#while contador < lf:
#     if contador % 3 == 0:
#        print(contador)
#    contador += 1

# ex - 10

#cot_dolar = 5.20
#cot_euro = 5.60
#cot_libra = 6.30

#contador = 0

#while contador < 1 or contador > 3:
#    contador = int(input("Digite o código da moeda (1 a 3): "))
#    if contador < 1 or contador > 3:
#        print("Código inválido. Tente novamente: ")

#valor_estrangeiro = float(input("Digite o valor que deseja comprar na moeda escolhida: "))

#if contador == 1:
#    valor_em_reais = valor_estrangeiro * cot_dolar
#    nome = "Dólar"
#elif contador == 2:
#    valor_em_reais = valor_estrangeiro * cot_euro
#    nome = "Euro"
#else:
#    valor_em_reais = valor_estrangeiro * cot_libra
#    nome = "Libra"

#if valor_em_reais < 1000:
#    comissao = valor_em_reais * 0.05
#else:
#    comissao = valor_em_reais * 0.03

#total = valor_em_reais + comissao

#print(f"\nVocê escolheu: {nome}")
#print(f"Valor em reais: R$ {valor_em_reais:.2f}")
#print(f"Comissão: R$ {comissao:.2f}")
#print(f"Total a pagar: R$ {total:.2f}")

# ex - 11

#contador = 1

#while contador <= 10:
#    tabuada = 1
#    while tabuada <= 10:
#        print(f'{contador} x {tabuada} = {contador * tabuada}')
#        tabuada += 1
#    contador += 1






