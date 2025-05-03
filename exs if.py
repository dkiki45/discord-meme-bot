#print("Bem-vindo")
#peso_levantador = float(input("Digite seu peso lutador(kg):"))
#if peso_levantador < 50:
#    print("Categoria Palha")
#elif 50 <= peso_levantador < 60:
#    print("Categoria Pena")
#elif 60 <= peso_levantador < 76:
#    print("Categoria Leve")
#elif 76 <= peso_levantador < 88:
#    print("Categoria Pesado")
#else:
#    print("Categoria Super Pesado")

#numero1 = float(input("Digite o primeiro número: "))
#numero2 = float(input("Digite o segundo número: "))
#numero3 = float(input("Digite o terceiro número: "))
#if numero1 > numero2:
#    numero1, numero2 = numero2, numero1
#if numero1 > numero3:
#    numero1, numero3 = numero3, numero1
#if numero2 > numero3:
#    numero2, numero3 = numero3, numero2
#print("Os números em ordem crescente são:", numero1, numero2, numero3)

#from colorama import Fore, Style
#print("Bem-vindo aluno")
#while True:
#    presenca_aluno = input("Digite sua presença (0 a 100): ")
#    try:
#        presenca_aluno = float(presenca_aluno)
#        if 0 <= presenca_aluno <= 100:
#           break
#        else:
#            print("Erro! A presença deve estar entre 0 e 100. Tente novamente.")
#   except ValueError:
#       print("Erro! Digite apenas números inteiros. Tente novamente. ")
#if presenca_aluno < 70:
#    print(Fore.RED + "Reprovado por falta." + Style.RESET_ALL)
#else:
#    print(Fore.GREEN + "Aprovado por presença." + Style.RESET_ALL)
#    while True:
#        nota_aluno = input("Digite sua nota (0 a 10): ")
#        try:
#            nota_aluno = float(nota_aluno)
#            if 0 <= nota_aluno <= 10:
#                break
#            else:
#                print("Erro! A nota deve estar entre 0 e 10. Tente novamente.")
#        except ValueError:
#            print("Erro! Digite apenas números inteiros. Tente novamente. ")
#    if nota_aluno > 9:
#        conceito = "A"
#    elif nota_aluno > 8:
#        conceito = "B"
#    elif nota_aluno > 7:
#        conceito = "C"
#    elif nota_aluno > 6:
#        conceito = "D"
#    elif nota_aluno > 5:
#       conceito = "E"
#   else:
#        conceito = "F"
#    if nota_aluno > 6:
#        print(Fore.GREEN + f"Aprovado com conceito {conceito} e nota {nota_aluno}." + Style.RESET_ALL)
#    else:
#        print(Fore.RED + f"Reprovado com conceito {conceito} e nota {nota_aluno}." + Style.RESET_ALL)

#print("Bem-vindo, aluno da PUC-PR!\nVeja os horários de abertura e fechamento da faculdade.")
#while True:
#    horas = input("Digite as horas que você deseja chegar (0-23): ")
#    if horas.isdigit():
#        horas = int(horas)
#        if 0 <= horas <= 23:
#            break
#        else:
#            print("Erro! As horas devem estar entre 0 e 23.")
#    else:
#        print("Erro! Digite apenas números inteiros.")
#while True:
#   minutos = input("Agora digite os minutos que deseja chegar (0-59): ")
#
#    if minutos.isdigit():
#        minutos = int(minutos)
#
#       if 0 <= minutos <= 59:
#            break
#        else:
#            print("Erro! Os minutos devem estar entre 0 e 59.")
#    else:
#        print("Erro! Digite apenas números inteiros.")
#tempo_usuario = horas * 60 + minutos
#tempo_abertura = 7 * 60 + 30  # (7:30)
#tempo_fechamento = 23 * 60 + 10  # (23:10)
#if tempo_abertura <= tempo_usuario <= tempo_fechamento:
#    print(f"A PUC-PR está aberta no horário {horas:02d}:{minutos:02d}! :)")
#else:
#    print(f"A PUC-PR está fechada no horário {horas:02d}:{minutos:02d}. :(")
#print("\nPrograma encerrado. Até mais!")
