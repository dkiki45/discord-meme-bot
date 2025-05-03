import random

# Início do jogo
print("Bem-vindo ao Jogo de Pedra, Papel e Tesoura!")

nome1 = input("Nome do Jogador 1: ")

# Solicitar o modo de jogo
modo = input("Escolha o modo: \n(1) vs Computador \n(2) vs Jogador\n ")
while modo not in ["1", "2"]:
    print("Opção inválida. Escolha 1 ou 2.")
    modo = input("Escolha o modo: \n(1) vs Computador \n(2) vs Jogador\n ")

# Verificar o modo escolhido e definir o nome dos jogadores
nome2 = "Computador" if modo == "1" else input("Nome do Jogador 2: ")

# Inicializar o placar e o histórico
placar = {"Jogador 1": 0, "Jogador 2": 0, "Empate": 0}
historico = []

negar_jogar_novamente = "n"
jogar_novamente = "s"
while jogar_novamente != negar_jogar_novamente:
    print("\nNova Rodada!")

    # Jogador 1 escolhe
    opcoes = {'1': 'Pedra', '2': 'Papel', '3': 'Tesoura'}
    escolha1 = input(f"\n{nome1}, escolha sua jogada: \n[1] PEDRA \n[2] PAPEL \n[3] TESOURA \nEscolha: ")
    while escolha1 not in opcoes:
        escolha1 = input(f"{nome1}, escolha inválida. [1] PEDRA, [2] PAPEL, [3] TESOURA: ")
    escolha1 = opcoes[escolha1]

    # Jogador 2 escolhe
    if nome2 == "Computador":
        escolha2 = random.choice(['Pedra', 'Papel', 'Tesoura'])
        print(f"\n{nome2} escolheu: {escolha2}")
    else:
        escolha2 = input(f"\n{nome2}, escolha sua jogada: \n[1] PEDRA \n[2] PAPEL \n[3] TESOURA \nEscolha: ")
        while escolha2 not in opcoes:
            escolha2 = input(f"{nome2}, escolha inválida. [1] PEDRA, [2] PAPEL, [3] TESOURA: ")
        escolha2 = opcoes[escolha2]

    print(f"\n{nome1} escolheu: {escolha1}")
    print(f"{nome2} escolheu: {escolha2}")

    # Determinar o vencedor
    if escolha1 == escolha2:
        vencedor = "Empate"
    elif (escolha1 == 'Pedra' and escolha2 == 'Tesoura') or \
            (escolha1 == 'Tesoura' and escolha2 == 'Papel') or \
            (escolha1 == 'Papel' and escolha2 == 'Pedra'):
        vencedor = "Jogador 1"
    else:
        vencedor = "Jogador 2"

    print("\nA rodada empatou!" if vencedor == "Empate" else f"\n{vencedor} venceu esta rodada!")

    # Atualizar placar e histórico
    placar[vencedor] += 1
    historico.append(f"{nome1} ({escolha1}) vs {nome2} ({escolha2}) → {vencedor} venceu")

    # Perguntar se o jogador quer jogar novamente
    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()

# Exibir histórico e placar final
print("\nHistórico de Partidas:")
print("\n".join(historico))
print("\nPlacar Final:")
print(f"{nome1}: {placar['Jogador 1']} vitórias")
print(f"{nome2}: {placar['Jogador 2']} vitórias")
print(f"Empates: {placar['Empate']}")
print("Obrigado por jogar! Até a próxima!")