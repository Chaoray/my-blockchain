from Blockchain import Blockchain
from BlockchainNode import BlockchainNode
import logging

blockchain = Blockchain()
blockchain.create_genesis_block('Hello Blockchain!')

node = BlockchainNode(blockchain)

logging.getLogger('werkzeug').disabled = True # remove annoying flask log

node.miner.mine_background()
node.run('127.0.0.1', 5000)
