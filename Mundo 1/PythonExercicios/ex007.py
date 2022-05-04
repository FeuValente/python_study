nota = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota + nota2) / 2
print('Sua média é {}'.format(media))
if media > 5:
    print('Aprovado')
else:
    print('Reprovado')