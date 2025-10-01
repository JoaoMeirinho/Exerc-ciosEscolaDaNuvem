unidade = input("Digite a unidade da temperatura (C para Celsius, F para Fahrenheit): ").upper()
temperatura = float(input("Digite a temperatura: "))
if unidade == 'C':
    fahrenheit = (temperatura * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f} °F")
elif unidade == 'F':
    celsius = (temperatura - 32) * 5/9
    print(f"A temperatura em Celsius é: {celsius:.2f} °C")
else:
    print("Unidade inválida. Por favor, use 'C' para Celsius ou 'F' para Fahrenheit.")
