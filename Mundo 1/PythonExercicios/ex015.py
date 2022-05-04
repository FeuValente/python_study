aluday = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))   
kmr = km * 0.15
carday = 60 * aluday
total = kmr + carday
print('O total a pagar é de R$ {}'.format(total))