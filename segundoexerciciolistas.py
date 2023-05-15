# Reutilizando o código da atividade anterior
nomes = ['João', 'Maria', 'Pedro', 'Ana', 'Lucas']

# Criando uma nova lista com mais 3 nomes
novos_nomes = ['Paula', 'Carlos', 'Mariana']

# Concatenando as duas listas
todos_nomes = nomes + novos_nomes

# Verificando se os nomes dos facilitadores estão contidos na lista
facilitadores = ['João', 'Maria', 'José']

for facilitador in facilitadores:
    if facilitador in todos_nomes:
        print(f'O nome do(a) facilitador(a) {facilitador} está na lista de todos os nomes.')
    else:
        print(f'O nome do(a) facilitador(a) {facilitador} não está na lista de todos os nomes.')
