#nome = input("Digite seu nome:")
#print("É um prazer conhecer você {}!".format(nome))


#n = input("Digite algo: ")
#print(n.isnumeric())

#numero1 = float(input("Digite um número:"))
#numero2 = float(input("Digite mais um número:"))
#print(f"A soma de {numero1} + {numero2} é igual a ", numero1 + numero2 )

#n = input("Digite algo: ")
#print(n.isnumeric())
#print(n.isalnum())
#print(n.isalpha())
#print(n.isascii())
#print(n.isnumeric())
#print(n.isdecimal())
#print(n.isspace())

#n = int(input("Digite um número: "))
#print(f"Analisando o valor {n}, seu antecessor é {n-1} e o seu sucessor é {n+1}.")

#n = float(input("Digite um número: "))
#print(f"O dobro de {n} é {n*2:.2f}.")
#print(f"O triplo de {n} é {n*3:.2f}." )
#print(f"A raiz de quadrada de {n} é igual {n**(1/2):.2f}.")

#nota1 = float(input("Digite a sua primeira nota: "))
#nota2 = float(input("Digite a sua segunda nota: "))
#media_aritmetica = (nota1 + nota2) / 2
#print(f"Média do aluno igual à: {media_aritmetica:.2f}")

#num = int(input("Digite um número para ver a tabuada: "))
#print("{} x {} = {}". format(num, 1, num*1))
#print("{} x {} = {}". format(num, 2, num*2))
#print("{} x {} = {}". format(num, 3, num*3))
#print("{} x {} = {}". format(num, 4, num*4))
#print("{} x {} = {}". format(num, 5, num*5))
#print("{} x {} = {}". format(num, 6, num*6))
#print("{} x {} = {}". format(num, 7, num*7))
#print("{} x {} = {}". format(num, 8, num*8))
#print("{} x {} = {}". format(num, 9, num*9))
#print("{} x {} = {}". format(num, 10, num*10))

#real = float(input("Quando de dinheiro você tem na sua conta? " "R$"))
#dolar = real/5.80
#print(f"Com R${real:.2f} você irá obter U${dolar:.2f}. ")

#class Cachorro:
#    def __init__(self, nome, comida, sono):
#        self.nome = nome
#        self.comida = comida
#        self.sono = sono
#
#    def comer(self):
#        if self.comida > 0:
#            self.comida -= 1
#            print(f"{self.nome} comeu! Comida restante: {self.comida}")
#        else:
#            print(f"{self.nome} não tem mais comida!")
#
#    def dormir(self):
#        if not self.sono:
#            self.sono = True
#            print(f"{self.nome} está agora dormindo.")
#        else:
#            print(f"{self.nome} já está dormindo!")
#
#    def alimentar(self, quantidade):
#        self.comida += quantidade
#        print(f"{self.nome} agora tem {self.comida} unidades de comida.")
#
#    def status(self):
#            # Verifica o estado de sono
#            status_sono = "dormindo" if self.sono else "acordado"
#            # Exibe as informações do cachorro
#            print(f"{self.nome} está {status_sono}. Comida restante: {self.comida}")
#
#cachorro_1 = Cachorro("Marlon", 3, False)
#cachorro_2 = Cachorro("Robson", 1, True)
#
#cachorro_1.comer()
#cachorro_1.status()
#cachorro_2.dormir()
#cachorro_2.comer()
#cachorro_2.alimentar(2)
#cachorro_2.status()

#from datetime import datetime
#def show_date() -> None:
#    print(f"O horário agr é esse: {datetime.now()} ")
#show_date()

#print("A Bomba vai explodir!!!")
#import time
#for i in range(5):
#    print(5 - i, end="\n")
#    time.sleep(1)
#print("BUUMMM!!!")






