peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print("Abaixo do peso")
elif imc > 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc > 24.9 and imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")