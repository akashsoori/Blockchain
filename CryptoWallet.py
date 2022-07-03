import os
import blocksmith

kg = blocksmith.KeyGenerator()
key = kg.generate_key()

print(key)

address = blocksmith.EthereumWallet.generate_address(key)
print(address) 
