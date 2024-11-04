import json

def calcular_faturamento():
    with open('faturamento.json', 'r') as file:
        dados = json.load(file)

    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_da_media = len([v for v in valores if v > media_mensal])

    print(f"Menor valor de faturamento diário: {menor_valor}")
    print(f"Maior valor de faturamento diário: {maior_valor}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

calcular_faturamento()
