# 4 - Verificando Números Pares e Ímpares
# Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
# Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

numero = int(input("Por favor, digite um número inteiro: "))  # Usuário dá entrada em um número inteiro

if numero % 2 == 0:  # Estrutura de controle verifica se o número é par pelo resto da divisão por 2
    print("O número {} é par.".format(numero))
else:
    print("O número {} é ímpar.".format(numero))

