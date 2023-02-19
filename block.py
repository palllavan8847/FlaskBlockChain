"""
This module holds the block functionality
"""

# For each block need transaction data, timestamp, previous hash
# Block chain holds all the block data
# Transaction need to verified before adding to block

import json
from hashlib import sha256


class Block:

    mining_difficulty = 2

    def __init__(self, **kwargs):
        self.index = kwargs['index']
        self.transaction_list = kwargs['transaction_list']
        self.timestamp = kwargs['timestamp']
        self.previous_hash = kwargs['previous_hash']
        self.nonce = kwargs['nonce']
        self.current_hash = '0'

    def generate_hash(self):
        """
        This function is used to hash the transaction value
        :return: hash value
        """

        return sha256(json.dumps(self.__dict__)).hexdigest()

