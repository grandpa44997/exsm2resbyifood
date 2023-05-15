lista = []

# Lê 15 números
for i in range(15):# Isso é um contador
    lista.append(int(input(f"Digite o {i+1}º número: ")))

# Remove elementos ímpares
lista = [x for x in lista if x % 2 == 0]# Utilizando list comprehension
'''Compreensões de lista fornece uma maneira concisa de criar uma lista. 
Aplicações comuns são criar novas listas onde cada elemento é o resultado de 
alguma operação aplicada a cada elemento de outra sequência ou iterável, ou 
criar uma subsequência de elementos que satisfaçam uma certa condição. (N.d.T. 
o termo original em inglês é list comprehensions, muito utilizado no Brasil; 
também se usa a abreviação listcomp).
A expressão [x for x in lista if x % 2 == 0] significa que cada elemento x da 
lista original será verificado para verificar se é par ou ímpar. Se x for par 
(o resto da divisão por 2 é zero), o elemento é adicionado à nova lista. Caso 
contrário, o elemento é ignorado.'''

# Ordena a lista em ordem crescente
#lista.sort()
# Ordena a lista em ordem decrescente
lista.sort(reverse=True)

# Exibe o maior e o menor valor
print("Maior valor:", lista[0])
print("Menor valor:", lista[-1])
print(lista)