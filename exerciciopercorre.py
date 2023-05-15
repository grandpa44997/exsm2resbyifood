'''em python screver um algoritmo que:
1. Cria duas listas de dez posições e;
2. Faça a multiplicação dos elementos de mesmo índice, colocando
o resultado em uma terceira lista, que deve ser mostrada como
saída.'''

lista01 = [1,2,3,4,5,6,7,8,9,10]
lista02 = [1,2,3,4,5,6,7,8,9,10]
lista_saida = lista01 * lista02

for i in range(len(lista_saida)):
  print(lista_saida[i])