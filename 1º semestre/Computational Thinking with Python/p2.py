# Programa 1

# Uma universidade realizará uma competição academica. Para está compeção, só poderão participar alunos com idade maior de idades. Faça um programa que solicite o RM e a iddde do aluno, informe se ele poderá ou não participar da competição. Caso o aluno menor e imforma ter autorização dos pais, exiba a mensagem "Você não pode participar da competição". Caso contrario, o cadastro n sera realizado.

# Solicitar o RM do aluno
rm = input("Digite o RM do aluno: ")

# Solicitar a idade do aluno
idade = int(input("Digite a idade do aluno: "))

# Verificar se o aluno é maior que 18 anos
if idade >= 18:
    print(f"Seu cadastro foi realizado com sucesso! Seu Rm {rm}")
else: 
    # Verificar se o aluno tem autorização dos pais
    autorizacao = input("Você tem autorização dos pais? (s/n): ").lower()
    if autorizacao == "s":
        print(f"Seu cadastro foi realizado com sucesso! Seu Rm {rm}")
        print("Mais imformações serão enviadas para o dos seu responsável")

    # Caso o aluno não tenha autorização dos pais
    else:
        print("Você não pode participar da competição")

# Programa 2

#Uma empresa de telefonia está realizando uma promoção, onde os clientes podem recebe
# bônus para navegação na internet com base em uma pontuação.
# 1000 pontos -> 3gb de bônus
# 500 pontos -> 1,5gb de bônus
# 200 pontos -> 500mb de bônus

#Crie um programa que receba o número de pontos e informe ao cliente quantos bônus ele receberá.

pontuação = int(input("Digite a pontuação: "))

if pontuação >= 1000:
    print("Você ganhou 3gb de bônus")
elif pontuação >= 500:
    print("Você ganhou 1,5gb de bônus")
elif pontuação >= 200:
    print("Você ganhou 500mb de bônus")
else:
    print("Você não ganhou bônus")

# Programa 3

#Para acessar um sistema, o usuário deve digitar o username darth_vader e a senha 1138
#Crie um script que receba e valide estas informações de acesso

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario.lower() == "darth_vader" and senha == "1138":
    print("Acesso permitido")
else:
    print("Acesso negado")

# Programa 4

#Durante o aniversário de sua fundação, uma loja está presenteando clientes da seguinte=
# forma:
#Todas as compras de valor superior a R$1000, concedem um desconto de 10%.
#Clientes selecionados receberam o cupom FESTA, que também gera 10% de desconto na hora da compra, não importando o valor.
#0s descontos não são cumulativos.
#Escreva um script em python que receba um cupom e o valor de uma compra do usuário e
# informe o valor da compra

valor_compra = float(input("Digite o valor da compra: "))
cupom = input("Digite o cupom: ")

if valor_compra >= 1000 or cupom == "FESTA":
    print("Você ganhou 10% de desconto")
    valor_compra = valor_compra * 0.9
else:
    print("Você não ganhou desconto")
print(f"Valor da compra: R${valor_compra:.2f}")

# Programa 5

#Uma lanchonete trabalha com diversos combos de lanches, conforme a tabela abaixo
#COMBO 1 -Hambúrguer R$12.50
#COMBO 2 Cheeseburguer R$15,00
#COMBO 3 X-Bacon R$17,50
#Crie um programa que receba o número de um combo e exiba o nome do lanche e o preço correspondente I

nomero_do_combo = int(input("Digite o número do combo: "))

match nomero_do_combo:
    case 1:
        print("Hambúrguer")
        valor_doprato = 12.50
    case 2:
        print("Cheeseburguer")
        valor_doprato = 15.00
    case 3:
        print("X-Bacon")
        valor_doprato = 17.50
    case _:
        print("Combo não encontrado")
        valor_doprato = 0


print(f"O combo desejado é o {nomero_do_combo} e custa R${valor_doprato}")