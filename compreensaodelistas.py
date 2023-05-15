#Aula de list comprehension em python

#criando lista de frutas
frutas = ['maçã', 'banana', 'laranja', 'figo']

#criando lista vazia
#novaLista = []

#percorrendo a lista e removendo as frutas que não contém a letra 'a'
#for x in frutas:
  #testando se a fruta não contém a letra 'a'
#  if 'a' not in x:
    #se não tiver a letra 'a' adicionando a nova lista
#    novaLista.append(x)


novaLista = [i for i in frutas if 'a' not in i] #compreensão de lista


#printando a nova lista    
print(novaLista)

maiuscula = [i.lower() for i in frutas]

#printando lista original para comparação
print(maiuscula)