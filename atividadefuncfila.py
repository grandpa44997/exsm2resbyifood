'''Crie um novo arquivo .py e implemente 3 novas funções conforme abaixo:
1. Uma função que acrescenta uma quantidade X de elementos a fila;
2. Uma função que verifica a quantidade de elementos na fila;
3. Uma função que verifica se a fila está vazia ou não.'''

# Criando uma fila vazia
fila = []

# Função que acrescenta uma quantidade X de elementos a fila
def adiciona_elementos_fila(fila, quantidade):
    # 
    for i in range(1, quantidade+1):
        fila.append(i)

# Função que verifica a quantidade de elementos na fila
def verifica_tamanho_fila(fila):
    return len(fila)

# Função que verifica se a fila está vazia ou não
def verifica_fila_vazia(fila):
    # Se a fila estiver vazia, retorna True
    if len(fila) == 0:
        return True
    else:
        return False
