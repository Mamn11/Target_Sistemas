import xml.etree.ElementTree as ET

# Inicializa a lista de dias com faturamento
dias_com_faturamento = []

# Faz a leitura do arquivo XML
try:
    tree = ET.parse('faturamento.xml')
    root = tree.getroot()
except FileNotFoundError:
    print("Arquivo faturamento.xml não encontrado.")
    exit()
except ET.ParseError:
    print("Erro ao ler o arquivo XML.")
    exit()

# Filtra os dias com faturamento
for dia in root.findall('dia'):
    try:
        dia_numero = int(dia.find('dia').text)
        valor = float(dia.find('valor').text)
        if valor > 0:
            dias_com_faturamento.append({'dia': dia_numero, 'valor': valor})
    except (ValueError, AttributeError):
        print(f"Erro ao processar o dia: {ET.tostring(dia, encoding='unicode')}")

# Calcula o faturamento médio
try:
    if dias_com_faturamento:
        media_mensal = sum(dia['valor'] for dia in dias_com_faturamento) / len(dias_com_faturamento)
    else:
        media_mensal = 0
except ZeroDivisionError:
    print("Nenhum dia com faturamento encontrado.")
    media_mensal = 0

# Calcula o faturamento mínimo e máximo
try:
    if dias_com_faturamento:
        min_faturamento = min(dia['valor'] for dia in dias_com_faturamento)
        max_faturamento = max(dia['valor'] for dia in dias_com_faturamento)
    else:
        min_faturamento = max_faturamento = 0
except ValueError:
    print("Não há dados suficientes para calcular o mínimo ou máximo faturamento.")
    min_faturamento = max_faturamento = 0

# Conta o número de dias com faturamento acima da média
try:
    if dias_com_faturamento:
        dias_acima_media = sum(1 for dia in dias_com_faturamento if dia['valor'] > media_mensal)
    else:
        dias_acima_media = 0
except TypeError:
    print("Erro ao calcular o número de dias acima da média.")
    dias_acima_media = 0

# Imprime os resultados
print("Menor valor de faturamento:", min_faturamento)
print("Maior valor de faturamento:", max_faturamento)
print("Número de dias acima da média:", dias_acima_media)
