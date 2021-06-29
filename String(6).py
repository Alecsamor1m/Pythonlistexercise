#6.Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

vogais = ['a', 'e', 'i', 'o', 'u']
x = str(input("Digita algo ai puto"))
counteresp = 0
countervog = 0
for a in range(0, len(vogais)):
    for i in x:
        if vogais[a] == i:
            countervog = countervog + 1
for i in x:
  if i == ' ':
    counteresp = counteresp + 1

print(counteresp, countervog)
