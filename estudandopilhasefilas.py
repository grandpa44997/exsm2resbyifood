#estudando pilhas e filas

# Pilha
# Criar uma pilha vazia
pilha = []
def insereNaPilha(pilha, elemento):
    # fazendo a inserção do elemento na pilha
    return pilha.append(elemento)
  
def removeDaPilha(pilha):
    # fazendo a remoção do elemento na pilha
    return pilha.pop()

# Fila  
# Criar uma fila vazia
fila = []

# Adicionar elementos à fila
for i in range(1, 10):
    fila.append(i)

# Remover um elemento da fila
elemento_removido = fila.pop(0)
print(elemento_removido)
