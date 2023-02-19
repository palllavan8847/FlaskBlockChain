# """
# This module is used to define block chain api's
# """
#
# import json
# #from main import app
# from flask import request
# #from blockchain import BlockChain
#
# #blockchain = BlockChain()
#
#
# @app.route('/chain', methods=['GET'])
# def get_chain():
#     chain_data = []
#     for block in blockchain.chain:
#         chain_data.append(block.__dict__)
#     return json.dumps({"length": len(chain_data), "chain": chain_data})
#
#
# @app.route('/transaction', methods=['POST'])
# def add_transaction():
#     data = request.json['transaction_data']
#     blockchain.add_transaction(data)
#     return json.dumps({"success": True})
#
#
# @app.route('/process_pending_transaction', methods=['GET'])
# def process_pending_transaction():
#     if blockchain.block_mine():
#         return json.dumps({"success": True})
#     return json.dumps({"success": False, "message": "No pending transaction data"})
