salario = float(input('Digite o salário: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('quem ganhava R${} passa a ganhar R${} agora.'.format(salario, novo))
