# 2 - Repetindo Textos
# Descrição: Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

texto = input("Por favor, digite a string que deseja repetir: ") # Entrada da string do usuário
numero = int(input("Por favor, digite o número de vezes que deseja repetir a string: ")) # Entrada do número inteiro do usuário

texto_repetido = (texto + " ") * numero # Realizando a repetição com espaçamento patra não ficar confuso...

print(texto_repetido) # Imprimindo o resultado