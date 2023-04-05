import requests

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/1?formato=json"
resposta = requests.get(url)
cotacao = float(resposta.json()[0]['valor'])
print(f'A cotação do dólar hoje é R$ {cotacao:.2}')

print(type(cotacao))

fatu = 1000
print(f'Faturamento: {fatu:.2f}')


