print('Python na Escola de Programação da Alura\n')

nome = ('Murilo S.K. de Moraes')
idade = 26
print(f'Meu nome é {nome} e tenho {idade} anos')

print("""
A
L
U
R
A
""")

pi = 3.14159
pi_arredondado = round(pi,2)
print(f'O valor arrendodado de pi é {pi_arredondado}\n')


numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")



idade = int(input("Digite sua idade: "))
if 0 < idade <= 12:
    print("Criança")
elif 12 < idade <= 18:
    print("Adolescente")
elif idade > 18:
    print("Adulto")
else: 
    print("Valor inválido!")


usuario_correto = "alura"
senha_correta = "alura123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")



x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")



lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_de_nomes = ['emy','gui','lais','mari']
lista_de_anos = [1999,2023]


lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in lista_de_numeros:
    print(numero)



soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)



for i in range(10, 0, -1):
    print(i)



numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")



lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")



lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


pessoa = {'nome': 'Felipe', 'idade': 30, 'cidade': 'São Paulo'}


# Atualização de Idade
pessoa['idade'] = 31

# Adicionando Profissão
pessoa['profissao'] = 'Engenheiro'

# Remoção de Elemento
del pessoa['cidade']


numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)


pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")


frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
