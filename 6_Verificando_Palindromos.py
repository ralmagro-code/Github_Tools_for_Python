# 6 - Verificando Palíndromos
# Descrição: Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

# Entrada de uma palavra pelo usuário
palavra = input("Por favor, digite uma palavra para verificar se é um palíndromo: ")

# Convertendo a palavra para minúsculas (para evitar problemas)
palavra_min = palavra.lower()
# Invertendo a palavra digitada
palavra_invertida = palavra_min[::-1]

# Estrutura de decisão verifica se a palavra original é igual à palavra invertida
if palavra_min == palavra_invertida:
    print(f'A palavra "{palavra}" é um palíndromo.')
else:
    print(f'A palavra "{palavra}" não é um palíndromo.')
