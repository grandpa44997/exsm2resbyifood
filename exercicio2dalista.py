# Criação das duas listas de tamanho igual
lista01 = [2, 4, 6, 8, 10]
lista02 = [1, 3, 5, 7, 9]

# Criação da lista vazia para armazenar a fusão das duas primeiras
novaLista = []

# Laço de repetição para percorrer todos os índices das listas originais
for i in range(len(lista01)):
    # Adiciona o elemento da primeira lista na nova lista
    novaLista.append(lista01[i])
    # Adiciona o elemento correspondente da segunda lista na nova lista
    novaLista.append(lista02[i])

# Verifica qual das listas é maior e adiciona os elementos restantes da lista maior na nova lista
if len(lista01) > len(lista02):
    novaLista += lista01[len(lista02):]
else:
    novaLista += lista02[len(lista01):]

# Imprime a lista final intercalada na tela
print("Lista final intercalada:", novaLista)
print("Para referência lista1:", lista01)
print("e lista2",lista02)
