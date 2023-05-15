'''Criar uma classe simples em Python para representar um produto. 
A classe deve ter dois atributos: "nome" e "preco". Em seguida, 
criar um objeto dessa classe com o nome "Arroz" e o preço "5.99".'''

# Criação da classe Produto
class Produto:
    # Método construtor da classe Produto, que recebe dois parâmetros: nome e preço
    def __init__(self, nome, preco):
        # Atribuição do parâmetro nome ao atributo nome da instância
        self.nome = nome
        # Atribuição do parâmetro preco ao atributo preco da instância
        self.preco = preco

# Criação de um objeto da classe Produto, atribuindo os valores "Arroz" e 5.99 aos parâmetros nome e preco, respectivamente
arroz = Produto("Arroz", 5.99)

# Impressão na tela do nome e do preço do objeto criado
# O símbolo de cifrão ($) é utilizado para indicar o início de uma expressão formatada
# O ".2f" na expressão formatada significa que o valor deve ser apresentado com duas casas decimais
print(f"Nome: {arroz.nome} | Preço: R${arroz.preco:.2f}")
