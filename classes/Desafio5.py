num1 = float(input("Digite o primeiro número: "));
num2 = float(input("Digite o segundo número: "));

soma = num1 + num2;
subtracao = num1 - num2;
divisao = num1 / num2;
multiplicacao = num1 * num2;
exponenciacao = num1 ** num2;

print('A soma de {} + {} é: {}' .format(num1, num2, soma))
print('A subtracao de {} - {} é: {}' .format(num1, num2, subtracao))
print('A divisao de {} / {} é: {}' .format(num1, num2, divisao))
print('A multiplicacao de {} * {} é: {}' .format(num1, num2, multiplicacao))
print('A exponenciacao de {} ** {} é: {}' .format(num1, num2, exponenciacao))