# criando classe Burger
class Burger:
  # construtor da classe
  def __init__(self, ingredientes):
    # atributos da classe
    self.ingredientes = ingredientes
  
  # método da classe  
  def print(self):
    # imprimindo os ingredientes do burger
    print(self.ingredientes)

# criando a classe FabricaDeBurgers    
class FabricaDeBurgers:
  # método da classe
  def criarCheeseBurger(self):
    # criando o burger com os ingredientes necessários para o cheese burger
    ingredientes = ['pão', 'carne', 'queijo', 'molho']
    # retornando o burger criado
    return Burger(ingredientes)

  # método da classe
  def criarCheeseBurgerSuper(self):
    # criando o burger com os ingredientes necessários para o cheese burger super
    ingredientes = ['pão', 'carne', 'queijo', 'molho', 'presunto']
    # retornando o burger criado
    return Burger(ingredientes)

  # método da classe
  def criarVeganBurger(self):
    # criando o burger com os ingredientes necessários para o vegan burger
    ingredientes = ['pão', 'molho especial de ervas', 'Futuro Burger', 'tomate']
    # retornando o burger criado
    return Burger(ingredientes)

# criando todos os burgers
fabricaDeBurgers = FabricaDeBurgers() # instanciando a classe FabricaDeBurgers
fabricaDeBurgers.criarCheeseBurger().print() # imprimindo o burger criado
fabricaDeBurgers.criarCheeseBurgerSuper().print()
fabricaDeBurgers.criarVeganBurger().print()
