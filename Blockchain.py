import hashlib
from typing import List
from Block import Block, PoW


class Blockchain:
    difficulty = 5
    hasher = hashlib.sha256()

    def __init__(self):
        self.chain : List[Block] = []

    def create_genesis_block(self, message:str) -> None:
        self.hasher.update(message.encode())
        block = Block(prev_hash=self.hasher.hexdigest(), nonce='', difficulty=self.difficulty)
        self.chain.append(block)

    def create_block(self) -> Block:
        return Block(prev_hash=self.chain[-1].get_hash(), nonce='', difficulty=self.difficulty)

    def add_block(self, block : Block) -> bool:
        prev_hash = self.chain[-1].get_hash()
        if not self.validate_block(prev_hash, block.nonce, block.difficulty):
            return False

        self.chain.append(block)
        return True

    def validate_block(self, prev_hash:str, nonce:str, difficulty:int) -> bool:
        return PoW.validate(prev_hash=prev_hash, nonce=nonce, difficulty=difficulty)

    def validate_chain(self) -> bool:
        prev_block = self.chain[0]
        index = 1

        while index < len(self.chain):
            block = self.chain[index]
            if not self.validate_block(prev_block.get_hash(), block.nonce, block.difficulty):
                return False
            prev_block = block
            index += 1

        return True

    # def increase_difficulty(self):
    #     self.difficulty += 1

    # def decrease_difficulty(self):
    #     self.difficulty -= 1
    #     self.difficulty = 1 if self.difficulty <= 0 else self.difficulty

    # # I found it hard to figure out when to increase/decrease difficulty
    # # so I just left it as it is

    def __str__(self) -> str:
        res = {
            'chain': [str(block) for block in self.chain]
        }
        return str(res)

