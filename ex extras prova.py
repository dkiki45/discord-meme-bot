#print("Enter the values for the three sides of a triangle:")

#side1 = float(input("Value for A: "))
#side2 = float(input("Value for B: "))
#side3 = float(input("Value for C: "))

# Check if it's a valid triangle using the triangle inequality theorem
#if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
#    print("This is a triangle!")

    # Determine the type of triangle
#    if side1 == side2 == side3:
#        print("It is an equilateral triangle.")
#    elif side1 == side2 or side1 == side3 or side2 == side3:
#        print("It is an isosceles triangle.")
#    else:
#        print("It is a scalene triangle.")
#else:
#    print("This is not a triangle!")

#from datetime import datetime

# Ask for birth date
#birth_year = int(input("Enter your birth year: "))
#birth_month = int(input("Enter your birth month (1 to 12): "))
#birth_day = int(input("Enter your birth day (1 to 31): "))

#today = datetime.now()

# Convert birth date and current date into total days
#birth_total_days = (birth_year * 365) + (birth_month * 30) + birth_day
#today_total_days = (today.year * 365) + (today.month * 30) + today.day

# Calculate total lived days
#total_days = today_total_days - birth_total_days

# Convert to years, months, and days (approximate)
#years = total_days // 365
#months = (total_days % 365) // 30
#days = (total_days % 365) % 30

#print(f"You have lived approximately {years} years, {months} months and {days} days.")


# Heights in centimeters
#francisco_height = 150  # 1.50 meters = 150 cm
#sara_height = 110       # 1.10 meters = 110 cm

# Annual growth in cm
#francisco_growth = 2
#sara_growth = 3

# Year counter
#years = 0

# Loop until Sara becomes taller than Francisco
#while sara_height <= francisco_height:
#    sara_height += sara_growth
#    francisco_height += francisco_growth
#    years += 1

# Show the result
#print(f"It will take {years} years for Sara to become taller than Francisco.")
#print(f"At that time, Francisco will be {francisco_height} cm tall. And Sara will be {sara_height} cm tall.")


# Ask for input values
#hourly_rate = float(input("Enter the hourly rate (value per class hour): "))
#hours_taught = int(input("Enter the number of hours taught in the month: "))
#inss_discount_percent = float(input("Enter the INSS discount percentage (e.g., 11 for 11%): "))

# Calculate gross salary
#gross_salary = hourly_rate * hours_taught

# Calculate discount amount
#inss_discount = (inss_discount_percent / 100) * gross_salary

# Calculate net salary
#net_salary = gross_salary - inss_discount

# Print the result
#print(f"The net salary of the teacher is: ${net_salary:.2f}")


#custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))

#porcentagem_distribuidora = 28 / 100
#impostos = 45 / 100

# Cálculo do custo final
#valor_distribuidora = custo_fabrica * porcentagem_distribuidora
#valor_impostos = custo_fabrica * impostos
#custo_carro_novo = custo_fabrica + valor_distribuidora + valor_impostos

#print(f"O valor final do carro novo será de R$ {custo_carro_novo:.2f}")

#carros_vendido = int(input('Digite quantos carros você vendeu: '))
#comissao_por_carro = int(input('Digite o valor que você recebe por carro vendido: R$ '))
#valor_vendas = int(input('Digite o valor total de suas vendas: R$ '))

#calculo_salario = salario_fixo + (comissao_por_carro * carros_vendido) + (valor_vendas * 5/100)

#print(f'O seu salário final esse mês é de {calculo_salario:.2f} R$.')

#numero_conta_cliente = input('Digite o número da sua conta: ')
#saldo = float(input('Digite o seu saldo bancário: R$ '))
#debito = float(input('Digite quanto você tem de débito: R$ '))
#credito = float(input('Digite quanto você tem de crédito: R$ '))

#saldo_atual = saldo - debito + credito

#print(f'\nNúmero da conta: {numero_conta_cliente}')
#print(f'Saldo atual: R$ {saldo_atual:.2f}.')

#if saldo_atual <= 0:
#    print('Saldo Negativo')
#else:
#    print('Saldo Positivo')

#usuario = int(input('Digite seu usuário: '))

#codigo_usuario = 1234
#codigo_senha = 9999

#if usuario == codigo_usuario:
#    senha = int(input('Digite sua senha: '))
#    if senha != codigo_senha:
#        print('\nSenha Incorreta')
#    else:
#        print('\nAcesso Permitido.')
#else:
#    print('\nUsuário Inválido')

#print('Sistema de aposentadoria da Empresa X.')

#numero_empregado = input('Digite seu código da empresa: ')
#ano_nascimento = int(input('Digite o ano que você nasceu: '))
#ano_ingresso_empresa = int(input('Digite o ano que voce ingressou na empresa: '))

#ano_atual = 2025

#idade = ano_atual - ano_nascimento
#tempo_empresa = ano_atual - ano_ingresso_empresa

#print(f'\nCódigo Empregado: {numero_empregado}')
#print(f'Idade: {idade} anos. ')
#print(f'Tempo de Empresa: {tempo_empresa} anos ')

#if idade >= 65 or tempo_empresa >= 30 or (idade >= 60 and tempo_empresa >= 25):
#    print('Requerer Aposentadoria!')
#else:
#    print('Não Requerer.')


#troco_reais = float(input("Digite o valor do troco em reais (ex: 1.37): R$ "))

#while troco_reais <= 0:
#    print("Por favor, insira um valor maior que zero.")
#    troco_reais = float(input("Digite o valor do troco em reais (ex: 1.37): R$ "))

# Converte para centavos e arredonda para evitar problemas com frações
#troco_centavos = int(round(troco_reais * 100))

#moedas_25 = troco_centavos // 25
#troco_centavos %= 25

#moedas_10 = troco_centavos // 10
#troco_centavos %= 10

#moedas_5 = troco_centavos // 5
#troco_centavos %= 5

#moedas_1 = troco_centavos

#print("\nQuantidade de moedas para o troco:")
#print(f"Moedas de R$ 0.25: {moedas_25}")
#print(f"Moedas de R$ 0.10: {moedas_10}")
#print(f"Moedas de R$ 0.05: {moedas_5}")
#print(f"Moedas de R$ 0.01: {moedas_1}")



