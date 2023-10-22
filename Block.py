import hashlib
import time

class PoW:
    @staticmethod
    def validate(prev_hash:str, nonce:str, difficulty:int):
        value = hashlib.sha256((prev_hash + nonce).encode()).hexdigest()
        return value.startswith('0' * difficulty)
        # Validating with leading zero, not a good algorithm tbh


class Block:
    def __init__(self, prev_hash:str, nonce:str, difficulty:int):
        self.prev_hash = prev_hash
        self.timestamp = time.time_ns()
        self.nonce = nonce
        self.difficulty = difficulty

    def __str__(self) -> str:
        header = {
            'prev_hash': self.prev_hash,
            'timestamp': self.timestamp,
            'nonce': self.nonce,
            'difficulty': self.difficulty
        }
        return str(header)

    def validate(self) -> bool:
        return PoW.validate(self.prev_hash, self.nonce, self.difficulty)

    def get_hash(self) -> str:
        return hashlib.sha256(str(self).encode()).hexdigest()
