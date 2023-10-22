from flask import Flask
from Blockchain import Blockchain
from BlockMiner import BlockMiner

class BlockchainNode(object):
    def __init__(self, blockchain:Blockchain):
        self.blockchain = blockchain
        self.miner = BlockMiner(blockchain)
        self.app = Flask(__name__)
        self.init_endpoints()
    
    def init_endpoints(self):
        def add_endpoint(url:str, endpoint:str, view_func, methods=['GET']):
            self.app.add_url_rule(url, endpoint, view_func, methods=methods)
        
        add_endpoint('/get_chain', 'get_chain', self.get_chain)
        add_endpoint('/get_state', 'get_state', self.get_state)


    def run(self, host, port):
        self.app.run(host, port)
    
    def get_chain(self):
        return str(self.blockchain)

    def get_state(self):
        resp = '<h2>Blockchain State</h2><br>'
        resp += f'Difficulty: {self.blockchain.difficulty}<br>'
        resp += f'Total Blocks: {len(self.blockchain.chain)}<br>'
        resp += f'Chain Validation: {self.blockchain.validate_chain()}<br>'
        return resp

