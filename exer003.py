import json

def processar_faturamento(dados_faturamento):
    dias_com_faturamento = [dia["faturamento"] for dia in dados_faturamento if dia["faturamento"] > 0]

    menor_faturamento = min(dias_com_faturamento)

    maior_faturamento = max(dias_com_faturamento)

    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_da_media = sum(1 for dia in dias_com_faturamento if dia > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

def ler_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        dados_faturamento = json.load(f)
    return dados_faturamento

caminho_arquivo = "faturamento.json"

dados_faturamento = ler_arquivo_json(caminho_arquivo)

menor_faturamento, maior_faturamento, dias_acima_da_media = processar_faturamento(dados_faturamento)

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
