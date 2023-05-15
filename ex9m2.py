'''Crie uma classe Retangulo que tenha os atributos base e altura e os métodos area e perimetro. 
Em seguida, crie um objeto da classe Retangulo, leia os valores de base e altura desse objeto do 
usuário e exiba na tela a área e o perímetro do retangulo.'''

# criando a classe
class Retangulo:
    # criando o construtor da classe
    def __init__(self, base, altura):
        # atributo base
        self.base = base
        # atributo altura
        self.altura = altura

    # método para calcular a área
    def area(self):
        # retorna o valor da base multiplicado pela altura
        return self.base * self.altura

    # método para calcular o perímetro
    def perimetro(self):
        # retorna o dobro da soma da base e da altura
        return 2 * (self.base + self.altura)
