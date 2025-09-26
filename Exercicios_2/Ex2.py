nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
pct_desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))
valor_desconto = preco_produto * (pct_desconto / 100)
preco_final = preco_produto - valor_desconto
print(f"Produto: {nome_produto} \n Valor do desconto: R$ {valor_desconto:.2f} \n Preço final: R$ {preco_final:.2f}Bon")