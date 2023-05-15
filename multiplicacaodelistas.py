a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

saida = []

for i in range(len(a)):
    saida.append(a[i]*b[i]) 
    
print('<Saída: >', saida)



'''result = [num1*num2 for num1, num2 in zip(a,b)]

 

print('<Saída: >', result)'''