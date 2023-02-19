"""
This file holds the block chain functionality
"""

from block import Block
from utils import get_current_timestamp


class BlockChain:

    mining_difficulty = 2  # proof of work or stake difficulty
    block_length = 5  # max transactions a block can hold

    def __init__(self, *args):
        self.chain = []
        self.pending_transaction_list = []
        self.failed_transaction_list = []
        self.create_initial_block()

    @staticmethod
    def create_initial_block():
        """
        This function is used to create the first ever block obj
        :return: Default block obj
        """

        block_dict = {
            'index': 0,
            'transaction_list': [],
            'timestamp': get_current_timestamp(),
            'previous_hash': 0,
            'nonce': '0'
        }
        return Block(**block_dict)

    def get_latest_block(self):
        """
        This function is used to get the latest block added to chain
        :return: latest added block
        """

        return self.chain[-1]

    def generate_matching_hash(self, block):
        """
        This function is used to verify the transaction status
        :return: hash value
        """

        hash_value = block.generate_hash()
        while not hash_value.startswith('0' * self.mining_difficulty):
            block.nonce += 1
            hash_value = block.generate_hash()
        return hash_value

    def add_transaction(self, transaction_data):
        """
        This function is used to add the transaction data the pending transaction list
        :return: hash value
        """
        self.pending_transaction_list.append(transaction_data)

    def verify_hash(self, block, current_hash):
        """
        :param block: Block object
        :param current_hash: block object current hash value
        :return: Bool
        """

        if not current_hash.startswith('0' * self.mining_difficulty):
            return False
        if block.generate_hash() == current_hash:
            return False
        return True

    def block_mine(self):
        """
        This function is used to add the successful block to the block chain
        :return: bool or transaction length
        """

        if not self.pending_transaction_list:
            return False

        transaction_length = len(self.pending_transaction_list)
        last_block = self.get_latest_block()
        for transaction_obj in self.pending_transaction_list[:self.block_length]:
            block_dict = {
                'index': last_block.index + 1,
                'transaction_list': transaction_obj,
                'timestamp': get_current_timestamp(),
                'previous_hash': last_block.hash,
                'nonce': '0'
            }
            block_obj = Block(**block_dict)
            current_hash = self.generate_matching_hash(block_obj)
            if not self.verify_hash(block_obj, current_hash):
                self.failed_transaction_list.append(block_obj)
                continue
            block_obj.current_hash = current_hash
            self.add_block_to_chain(block_obj)

        self.pending_transaction_list = []
        return transaction_length

    def add_block_to_chain(self, block_obj):
        """
        This function is used to add the block obj to the chain
        :param block_obj:
        :return:
        """

        self.chain.append(block_obj)
