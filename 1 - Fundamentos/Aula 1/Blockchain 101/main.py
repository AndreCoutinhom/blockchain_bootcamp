import hashlib

data = "nearx"
data_encoded = data.encode()

output = hashlub.sha256(data_encoded)
output_decoded = output.hexdigest()

print(output_decoded)

# O código acima codifica a palavra "nearx" em uma sequência pseudoaleatória. A sequência continuará sendo a mesma não importa quantas vezes o código seja acionado. A menos que a palavra tenha seu valor de caracteres alterados, o código gerado continuará sendo o mesmo.
# O tamanho da string também não altera o número de caracteres da sequência codificada, ou seja, o resultado do hash é fixo em tamanho de saída.
