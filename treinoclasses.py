# Define a classe "ApplicationState"
class ApplicationState:
  
  # Define o construtor da classe com uma propriedade chamada "isLoggedIn" definida como False
  def __init__(self):
    self.isLoggedIn = False
    
  # Define o método estático "getAppState()" que retorna uma única instância da classe usando o padrão Singleton
  @staticmethod
  def getAppState():
    # Verifica se a instância já foi criada antes de criar uma nova
    if not hasattr(ApplicationState, "instance"):
      ApplicationState.instance = ApplicationState()
    return ApplicationState.instance
  
# Cria uma instância da classe "ApplicationState" usando o método estático "getAppState()"
appState1 = ApplicationState.getAppState()

# Imprime o valor da propriedade "isLoggedIn" da instância "appState1", que é False
print(appState1.isLoggedIn)

# Cria outra instância da classe "ApplicationState" usando o método estático "getAppState()"
# Como o padrão Singleton garante que apenas uma instância da classe seja criada, essa nova instância é a mesma que a anterior
appState2 = ApplicationState.getAppState()

# Define o valor da propriedade "isLoggedIn" na instância "appState1" como True
appState1.isLoggedIn = True

# Imprime o valor da propriedade "isLoggedIn" da instância "appState1", que agora é True
print(appState1.isLoggedIn)

# Imprime o valor da propriedade "isLoggedIn" da instância "appState2", que também é True, pois ambas as instâncias compartilham a mesma propriedade "isLoggedIn" devido ao uso do padrão Singleton
print(appState2.isLoggedIn)
