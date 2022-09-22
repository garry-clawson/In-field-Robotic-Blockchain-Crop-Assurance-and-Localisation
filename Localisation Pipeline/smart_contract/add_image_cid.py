import json
from web3 import Web3, HTTPProvider

# Contract address - normally this would be via a QR code scan but here we hard code it - 0x78C5b42F655e91eaEc8f44873e6A25eaFDE17dD9
addressValue = input("Enter your Ethereum ImageStore contract address: ")

image_CID = input("Enter the CID of the image: ") #this will be given to you in the IPFS stage

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'

# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))

# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]

# Path to the compiled contract JSON file
# The ImageStore.json is from our compiled ImageStore.sol contract code
compiled_contract_path = 'build/contracts/ImageStore.json'

# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = addressValue

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

# Fetch deployed contract reference
# and create object
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

# Call contract function (this is not persisted to the blockchain) but just an action on it (it still costs Gas though)
ListSize = contract.functions.getListSize().call()
#print(type(ListSize))
print("List size: ", ListSize)

# Get the last item in the list (htis is hardcoded and is the CID 
# result of the uploaded image to IPFS) in the addItem() call function
# Call contract function (this is not persisted to the blockchain)
#ListSize = ListSize - 1 # Array starts at 0 but list starts at 1
#ListItem = contract.functions.getListItem(ListSize).call()
#print("List Item: ", ListItem)

# executes addItem function and persists data to the blockchain
# The value appended is the CID of the template image that was returned to us from IPFS
tx_hash = contract.functions.addItem(image_CID).transact()
# waits for the specified transaction (tx_hash) to be confirmed
# (included in a mined block)
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
#Prints the transaction hash for later reference if needed (i.e. we can confirm that the transaction  occured)
print('CID added: ', image_CID)
print('tx_hash: {}'.format(tx_hash.hex()))
