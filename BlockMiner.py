from Blockchain import Blockchain
import threading

class BlockMiner:
    is_mining = False

    def __init__(self, blockchain:Blockchain):
        self.blockchain = blockchain
        self.thread = None

    def mine_background(self):
        self.is_mining = True
        self.thread = threading.Thread(target=self.mine, daemon=True)
        self.thread.start()
    
    def stop(self):
        self.is_mining = False

    def mine(self):
        while self.is_mining:
            block = self.blockchain.create_block()
            assumed_nonce = 0
            block.nonce = str(assumed_nonce)

            while not block.validate():
                assumed_nonce += 1
                block.nonce = str(assumed_nonce)

            self.blockchain.add_block(block)
