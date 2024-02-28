# UTXOS (Unspent transaction output) são como notas de dinheiro digital dentro da blockchain do bitcoin.

utxos = [{"owner": "Bob", "amount": 15}]

# transfer 10 Token from BOB to ALICE
new_utxos = [
    {"owner": "Alice", "amount": 10},
    {"owner": "Bob", "amount": 5}
]
utxos = []
utxos.extend(new_utxos)

print(utxos)

# O saldo não é definido pelo número de bitcoins e sim pelo número de UTXOS, que define quanto é possível transferir e quanto foi recebido.
