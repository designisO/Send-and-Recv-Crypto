from dotenv import load_dotenv
load_dotenv()
import os
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545" # ganache url
web3 = Web3(Web3.HTTPProvider(ganache_url))

wallet_1 = "0xb188B44958c86d1d25A4573c5E87CF9c4D2b7026" # ganache
wallet_2 = "0x4b779bF8E9f94706B96F12Bfd28B936D0E4b2d2C" # ganache

private_key = os.environ.get('private_key') #ganche key from wallet 1

nonce = web3.eth.getTransactionCount(wallet_1)

# get nonce
# build a transaction

tx = {
    'nonce': nonce,
    'to': wallet_2,
    'value': web3.toWei(2, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('30', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
print('Crypto sent to ' + wallet_2 + ' successfully!')
print('Your balance is now: ')
print(web3.eth.getBalance(wallet_1))
print('Thanks for using my dApp - Orion3000')

# 0x5dc82187543068b04e315e6335bf660226e128e3d5596e1d2cedf7769fe919e3
# etherscan contract address

