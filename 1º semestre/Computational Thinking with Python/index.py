#  A Linha abaixo exibe uma mensagem de boas vinda do usiaurio
print("Bem vindo ao sistema do Caio!")  
# A linha abaixo solicita ao usuario que digite seu nome
nome = input("Digite seu nome: ")
# A linha abaixo exibe uma mensagem de boas vindas ao usuario
print("que legal vc está aki, " + nome + "!")


print("Calculador de idade")
# Perguntar o ano de nascimento
ano_nacimento = int(input("Digite o ano de nascimento: "))
# Calcular a idade
idade = 2025 - ano_nacimento
#  A melhor forma de exibir uma variavel é com o f
print(f"Sua idade é: {idade} anos")
