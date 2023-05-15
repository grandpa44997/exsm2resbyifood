# Exemplo de montagem de burgers usando o padrão builder
class Burger:
  # Atributos
  def  __init__(self): # Construtor
    # Atributos do burger
    self.pao = None
    self.sabor = None
    self.queijo = None
    self.molho = None
  
  # Métodos de acesso aos atributos
  def setPao(self, paoEstilo):
    self.pao = paoEstilo
    
  def setSabor(self, saborTipo):
    self.sabor = saborTipo
    
  def setQueijo(self, queijoTipo):
    self.queijo = queijoTipo
    
  def setMolho(self, molhoTipo):
    self.molho = molhoTipo
    
# Classe que monta o burger
class montadorDeBurgers:
  def __init__(self): # Construtor
    self.burger = Burger() # Instancia o burger
  
  # Métodos de acesso aos atributos  
  def addPao(self, paoEstilo):
    self.burger.setPao(paoEstilo)
    return self
  
  def addSabor(self, saborTipo):
    self.burger.setSabor(saborTipo)
    return self
  
  def addQueijo(self, queijoTipo):
    self.burger.setQueijo(queijoTipo)
    return self
  
  def addMolho(self, molhoTipo):
    self.burger.setMolho(molhoTipo)
    return self
  
  # Método que monta o burger
  def montar(self):
    return self.burger
  
# montagem do Burger
burger = montadorDeBurgers() \
          .addPao('Integral') \
          .addSabor('Carne') \
          .addQueijo('Cheddar') \
          .addMolho('Tomate') \
          .montar() # Monta o burger
