#ex1

#vetor = []
#contador = 0

#while contador < 10:
#    valor = int(input(f"Digite o valor para a posição {contador}: "))
#    vetor.append(valor)
#    contador += 1

#contador = 0
#print("\nValores no vetor:")
#while contador < 10:
#    print(f"Posição {contador}: {vetor[contador]}")
#    contador += 1

#ex2

text = input('Write something: ')
vowels = ['a', 'e', 'i', 'o', 'u']
counter = 0
index = 0

while index < len(text):
    if text[index].lower() in vowels:
        counter += 1
    index += 1

print(f"Number of vowels: {counter}")


