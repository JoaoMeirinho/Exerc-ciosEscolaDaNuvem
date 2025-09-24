nome_produto = input("Digite o nome do produto: ")
preco_produto = input("Digite o preço do produto: ")
preco_produto = float(preco_produto)
quantidade = input("Digite a quantidade comprada: ")
quantidade = int(quantidade)
total = preco_produto * quantidade
print("O total a pagar é R$", total)