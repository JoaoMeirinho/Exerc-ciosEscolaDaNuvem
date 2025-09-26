distancia_percorrida = float(input("Digite a distância percorrida em km: "))
combustivel_gasto = float(input("Digite o combustível gasto em litros: "))
consumo_medio = distancia_percorrida / combustivel_gasto
print("-----RESULTADO-----")
print(f"Distância percorrida (km): {distancia_percorrida}", distancia_percorrida)
print(f"Combustível gasto (litros): {combustivel_gasto}")
print(f"O consumo médio do veículo é: {consumo_medio:.2f} km/l")