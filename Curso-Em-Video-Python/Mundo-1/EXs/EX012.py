preço = float(input('Digite o preço do produto: R$'))
novo = preço - (preço*0.05)
print('O produto com 5% de desconto fica por R${:.2f}'.format(novo))