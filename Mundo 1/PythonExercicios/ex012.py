preco = float(input('Digite o preço do produto: '))
desconto = preco * 0.05
print('O produto custa R${:.2f} e com 5% de desconto custa R${:.2f}'.format(preco, preco - desconto))