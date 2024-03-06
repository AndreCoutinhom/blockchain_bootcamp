# Account-based
# O código faz a mesma transação de bitcoin, mas com sistema de contas habilitado

accounts = {
    "Bob": 15,
    "Alice": 0,
}

# transfer 10 Token from BOB to ALICE
accounts["Bob"] -= 10
accounts["Alice"] += 10

print(accounts)
