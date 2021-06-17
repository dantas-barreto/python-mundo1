n1 = int(input('Digite um valor: '))
print(type(n1))
n2 = int(input('Digite outro valor: '))
print(type(n2))
soma = n1 + n2
#print('A soma entre', n1, 'e', n2, 'vale', soma)
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
print(str(soma).isnumeric())