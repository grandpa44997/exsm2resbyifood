tupla = (1,2,3,4,5)
print(len(tupla))

tuplaReversa = tupla[::-1]
print(tuplaReversa)

separador = "-"
novaTuplaStr = separador.join(str(elemento) for elemento in tuplaReversa)
print("Elementos da nova tupla separados por '-':", novaTuplaStr)