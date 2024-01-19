nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

print('Olá,', nome, 'você tem', idade, 'anos.')
print('Olá, {}! Você tem {} anos.' .format(nome, idade))
print(f'Olá, {nome}! Você tem {idade} anos.')