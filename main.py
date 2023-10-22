from Blockchain import Blockchain
from BlockchainNode import BlockchainNode

blockchain = Blockchain()
blockchain.create_genesis_block('Hello Blockchain!')

node = BlockchainNode(blockchain)
node.miner.mine_background()
node.run('127.0.0.1', 5000)
