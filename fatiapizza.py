# Criando a lista de pizzas favoritas
my_pizzas = ['margherita', 'calabresa', 'pepperoni']

# Criando uma cópia da lista de pizzas favoritas
friend_pizzas = my_pizzas.copy()

# Adicionando uma nova pizza à lista original
my_pizzas.append('quatro queijos')
my_pizzas.pop(1) 

# Adicionando uma pizza diferente à lista friend_pizzas
friend_pizzas.append('frango com catupiry')

# Exibindo as duas listas
print("Minhas pizzas favoritas são:")
print(my_pizzas)
#for pizza in my_pizzas:
#    print("- " + pizza)

print("\nAs pizzas favoritas de meu amigo são:")
print(friend_pizzas)
#for pizza in friend_pizzas:
#    print("- " + pizza)