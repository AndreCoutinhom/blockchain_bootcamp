# Abaixo a função hash é criada usando outra biblioteca

import keccaky

data = "nearx"
output_decoded = keccaky.hash_it(data)

print(output_decoded)

# Usando bibliotecas diferentes, percebemos que cada função hash produz um resultado diferente.
