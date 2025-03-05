#  Url completa
url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
# print(url)

# Url Base
indece_interrogacao = url.find('?')
url_base = url[:indece_interrogacao]
# print(url_base)

# Paremetro da Url
url_parametro = url[indece_interrogacao+1:]
print(url_parametro)


parametro_busca = 'moedaDestino'
indice_parametro = url_parametro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametro[indice_valor:]

print(valor)

url.le