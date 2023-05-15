'''Crie um novo arquivo .py:
1. Elabore um algoritmo que use uma list comprehension para gerar uma lista dos cubos dos dez
primeiros números ímpares.'''

# Usando list comprehension para gerar uma lista dos cubos 
# dos dez primeiros números ímpares
cubos = [i ** 3 for i in range(1, 20, 2)] 

# Imprimindo a lista de cubos
print(cubos)