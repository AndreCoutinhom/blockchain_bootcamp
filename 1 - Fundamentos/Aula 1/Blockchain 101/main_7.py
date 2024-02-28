# BLOCOS
# Os blocos comportam dados estruturados em diferentes hash. 
genesis = {
    "hash": "0xdc0818cf78f21a8e70579cb46a43643f78291264dda342ae31049421c82d21ae",
    "parentHash": "0x0",
    "transactions": [],
}
block1 = {
    "hash": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "parentHash": "0xdc0818cf78f21a8e70579cb46a43643f78291264dda342ae31049421c82d21ae",
    "transactions": [],
}
block2 = {
    "hash": "0x301f4a1c0cb92f3c3c4c2376143c3b0be4bff71b9554760ac6391c299ee1dea0",
    "parentHash": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "transactions": [],
}
block3 = {
    "hash": "0xfe9480cfff9106cb625104e35f5c632a8af37f2a160e400aaa3db9e2ece720e7",
    "parentHash": "0x301f4a1c0cb92f3c3c4c2376143c3b0be4bff71b9554760ac6391c299ee1dea0",
    "transactions": [],
}

blockchain = [genesis, block1, block2, block3]
# A blockchain apresenta todo o histórico de informações; de qual hash cada dado veio e em que ordem.
