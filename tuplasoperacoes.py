#Tuplas são imutáveis
nomes = ['Ana', 'João', 'Maria', 'Pedro']
# Convertendo uma lista em tupla
tupla_nomes = tuple(nomes)

# Imprimindo os itens da tupla
for nome in tupla_nomes:
    # Imprimindo o nome
    print(f"Olá, {nome}!")

# Alterando um item da tupla
nova_tupla = tuple(list(tupla_nomes)[:2] + ['Carlos'] + list(tupla_nomes)[3:]) # Criando uma nova tupla com o item 'Carlos' adicionado
print(nova_tupla)

# Usando um método de lista na tupla
indice_pedro = nova_tupla.index('Pedro') 
print(f"O nome 'Pedro' está na posição {indice_pedro} da tupla.")