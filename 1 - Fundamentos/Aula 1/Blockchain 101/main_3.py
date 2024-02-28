from eth_account import Account

seed = "jump skull butter topic bronze member feed wait flee oven deer rabbit"

Account.enable_unaudited_hdwallet_features()
account = Account().from_mnemonic(mnemonic=seed)

print(account.key.hex())
print(account.address)

# ETHEREUM SIGNATURE (r,s,v)
# Assinaturas na blockchain ethereum criam três valores diferentes que autenticam a fonte da transação ao interpretar a chave pública e a chave privada do usuário.

tx = {
    "to": "0xF0109fC8DF283027b6285cc889F5aA624EaC1F55",
    "value": 1000000000,

    "gas": 2000000,
    "maxFeePerGas": 2000000000,
    "maxPriorityFeePerGas": 1000000000,
    "nonce": 0,
    "chainId": 1,
}

signed_tx = account.sign_transaction(tx)

print(signed_tx.r)
print(signed_tx.s)
print(signed_tx.v)
