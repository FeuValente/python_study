nome = str(input('Qual é seu nome? '))
if nome == 'Alfeu':
    print('Que nome lindo você tem!')
else: 
   print('Seu nome é tão normal! ')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média é: {}'.format(m))
if m >= 6.0:
    print('Sua média foi boa!')
else: 
    print('Sua média foi ruim! Estude mais!!')