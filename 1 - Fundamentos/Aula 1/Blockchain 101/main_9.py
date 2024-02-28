# Mineração PoW
# ALGORITMO ORIGINAL DO SATOSHI NAKAMOTO

import hashlib

def proof_of_work(block_hash, difficulty=4):
    nonce = 0
    while True:
        attempt = f"{block_hash}{nonce}".encode()

        hash_attempt = hashlib.sha256(attempt).hexdigest()

        if hash_attempt.startswith("0" * difficulty):
            print(f"Nonce encontrado: {nonce}")
            print(f"Hash correspondente: {hash_attempt}")
            break
        nonce += 1


proof_of_work("0xfe9480cfff9106cb625104e35f5c632a8af37f2a160e400aaa3db9e2ece720e7", 4)

# A mineração é como diversas tentativas consecutivas de desvendar o valor de um hash.
