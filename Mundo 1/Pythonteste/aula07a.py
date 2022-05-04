#Operadores Aritiméticos

# +  Adição
# -  Subtração
# *  Multiplicação
# /  Divisão
# ** Potenciação     pow(x,y)= x**y
# // Divisão Inteira     Dividir sempre com resultado inteiro
# %  Resto da divisão    Retorna o resto da divisão
# == Igualdade
# != Diferente
# > Maior que
# < Menor que
# >= Maior ou igual
#  Ordem de Precedência
# 1° ()
# 2° **
# 3° * / // %
# 4° + -


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é: {}, \n o produto é: {}, \n a divisão é: {}'.format(s, m, d))
print('A divisão inteira é: {} e a potencia é: {}'.format(di, e))