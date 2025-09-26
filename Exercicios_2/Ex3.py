qtd_notas = int(input("Digite a quantidade de notas a serem inseridas: "))
notas = []

for i in range(qtd_notas):
    notas.append(float(input(f"Digite a {i + 1}° nota: ")))
media = sum(notas) / qtd_notas

for i, nota in enumerate(notas):
    print(f"Nota {i + 1}: {nota:.2f}")
print(f"Média: {media:.2f}")