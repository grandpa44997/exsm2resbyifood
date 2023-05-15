'''Criar uma classe simples em Python para representar um produto. 
A classe deve ter dois atributos: "nome" e "preco". Em seguida, 
criar um objeto dessa classe com o nome "Arroz" e o preço "5.99".'''

# cria classe produto
class Produto:
    # cria atributos da classe
    def __init__(self, nome, preco):
        # atributo nome
        self.nome = nome
        # atributo preço
        self.preco = preco

# cria objeto produto e atributo nome e preço
arroz = Produto("Arroz", 5.99)
# imprime os atributos do produto criado
print(f"Nome: {arroz.nome} | Preço: R${arroz.preco:.2f}")
