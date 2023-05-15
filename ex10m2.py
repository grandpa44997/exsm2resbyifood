'''Crie uma classe Aluno que tenha os atributos nome, idade e matrícula. Em seguida, crie um objeto da classe Aluno, leia os valores de nome, 
idade e matrícula desse objeto do usuário e exiba na tela os dados do aluno cadastrado.'''

class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

# Criação do objeto da classe Aluno
aluno = Aluno('', 0, '')

# Leitura dos dados do aluno do usuário
aluno.nome = input('Digite o nome do aluno: ')
aluno.idade = int(input('Digite a idade do aluno: '))
aluno.matricula = input('Digite a matrícula do aluno: ')

# Exibição dos dados do aluno cadastrado
print('Dados do aluno cadastrado:')
print('Nome:', aluno.nome)
print('Idade:', aluno.idade)
print('Matrícula:', aluno.matricula)
