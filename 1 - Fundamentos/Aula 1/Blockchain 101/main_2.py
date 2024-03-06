# ETHEREUM SEED TO ADDRESS
# Em criptografia de chave pública, uma chave privada gerada por uma função hash se torna o meio exclusivo de acesso para comando da chave pública.

from eth_account import Account

seed = "jump skull butter topic bronze member feed wait flee oven deer rabbit"

Account.enable_unaudited_hdwallet_features()
account = Account().from_mnemonic(mnemonic=seed)

print(account.key.hex())
print(account.address)

# Após definir a chave privada em "seed", a chave pública é gerada logo após.
