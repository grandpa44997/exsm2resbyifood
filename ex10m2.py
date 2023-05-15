'''Crie uma classe Aluno que tenha os atributos nome, idade e matrícula. 
Em seguida, crie um objeto da classe Aluno, leia os valores de nome, idade 
e matrícula desse objeto do usuário e exiba na tela os dados do aluno 
cadastrado.'''
# Criação da classe Aluno
class Aluno:
    # construtor da classe Aluno
    def __init__(self, nome, idade, matricula):
        # atributo nome
        self.nome = nome
        # atributo idade
        self.idade = idade
        # atributo matrícula
        self.matricula = matricula

# Criação do objeto da classe Aluno
aluno = Aluno('', 0, '')

# Leitura dos dados do aluno do usuário
aluno.nome = input('Digite o nome do aluno: ')
aluno.idade = int(input('Digite a idade do aluno: '))
aluno.matricula = input('Digite a matrícula do aluno: ')

# Exibição dos dados do aluno cadastrado
print('Dados do aluno cadastrado:')
print('Nome:', aluno.nome) # print e acesso ao atributo nome
print('Idade:', aluno.idade) # print e acesso ao atributo idade
print('Matrícula:', aluno.matricula) # print e acesso ao atributo matrícula
