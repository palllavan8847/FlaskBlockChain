"""
This module will be used to initiate flask app and define api's
"""

import json
from flask import Flask, request
from blockchain import BlockChain

blockchain = BlockChain()
app = Flask(__name__)
app.run(debug=True, port=5000)


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = [block.__dict__ for block in blockchain.chain]
    return json.dumps({"length": len(chain_data), "chain": chain_data})


@app.route('/transaction', methods=['POST'])
def add_transaction():
    data = request.json['transaction_data']
    blockchain.add_transaction(data)
    return json.dumps({"success": True})


@app.route('/process_pending_transaction', methods=['GET'])
def process_pending_transaction():
    status = blockchain.block_mine()
    if status:
        return json.dumps({"success": True, "message": f"Processed {status} transactions"})
    return json.dumps({"success": False, "message": "No pending transaction data"})
