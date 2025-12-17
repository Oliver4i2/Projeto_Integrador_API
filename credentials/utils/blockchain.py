import hashlib
import json
from dataclasses import dataclass, field
from time import time

def sha256(data: str) -> str:
    """Retorna o hash SHA-256 de uma string."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

@dataclass
class Block:
    index: int
    timestamp: float
    data: dict
    previous_hash: str
    nonce: int = 0
    hash: str = field(init=False)

    def __post_init__(self):
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        """Calcula o hash do bloco com base nos seus atributos."""
        payload = {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
        }
        return sha256(json.dumps(payload, sort_keys=True))

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Cria o primeiro bloco da cadeia (genesis)."""
        genesis = Block(index=0, timestamp=time(), data={'genesis': True}, previous_hash='0')
        self.chain.append(genesis)

    @property
    def last_block(self) -> Block:
        """Retorna o último bloco da cadeia."""
        return self.chain[-1]

    def add_block(self, data: dict) -> Block:
        """Adiciona um novo bloco à cadeia com os dados fornecidos."""
        block = Block(
            index=len(self.chain),
            timestamp=time(),
            data=data,
            previous_hash=self.last_block.hash
        )
        self.chain.append(block)
        return block

# Instância única da blockchain para uso no app
blockchain = Blockchain()

