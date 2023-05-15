import random

# Lista dos integrantes
integrantes = ["Daniel", "Gabriel", "Jaymerson", "Rodrigo"]

# Lista dos papéis
papeis = ["Pessoa Colaboradora", "Pessoa Gestora de Gente e Engajamento", 
          "Pessoa Gestora de Conhecimento", "Pessoa Cofacilitadora"]

# Sorteio aleatório dos papéis para cada integrante
sorteio = random.sample(papeis, len(papeis))

# Criação da lista final de integrantes e suas respectivas funções
lista_final = []
for i in range(len(integrantes)):
    lista_final.append(f"{integrantes[i]} - {sorteio[i]}")

# Impressão da lista final
print(lista_final)