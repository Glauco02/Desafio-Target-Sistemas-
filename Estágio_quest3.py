print("3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);\n")


indice = 12
soma = 0
k = 1

while k < indice:
    k +=1
    soma += k

print(f"O resultado é: {soma}")
