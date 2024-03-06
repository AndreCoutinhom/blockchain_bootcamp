# create a wallet
account = Account.create()

# create a transaction
tx = {
    "from": "0xfe9480cfff9106cb625104e35f5c632a8af37f2a", 
    "to": "0xF0109fC8DF283027b6285cc889F5aA624EaC1F55",
    "value": 1000000000,

    "gas": 2000000,
    "maxFeePerGas": 2000000000,
    "maxPriorityFeePerGas": 1000000000,
# gas é referente a gasolina. É como se fosse um combustível que é gasto sempre que uma transação ocorre.
    "nonce": 0,
  # O nonce é uma forma de medir o número de transações já enviadas. O sistema é relacionado ao bloqueio que bancos digitais possuem com múltiplas transações por PIX em um mesmo dia.
    "chainId": 1,
}

# sign tx
signed_tx = account.sign_transaction(tx)

# create a provider
ALCHEMY_API_KEY = "00000000000000000000000000000000"
URL = f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY}/"
web3 = Web3(Web3.HTTPProvider(URL))

# send tx
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

print(tx_hash.hex())
