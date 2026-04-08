#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]

app = Flask(__name__)

# /contract/<id> route
@app.route('/contract/<int:contract_id>', methods=['GET'])
def get_contract(contract_id):
    contract = next((c for c in contracts if c['id'] == contract_id), None)
    if contract:
        # Return only the contract_information as plain text
        return contract["contract_information"], 200
    else:
        return {"error": "Contract not found"}, 404

# /customer/<customer_name> route
@app.route('/customer/<customer_name>', methods=['GET'])
def get_customer(customer_name):
    if customer_name.lower() in customers:
        return '', 204
    else:
        return {"error": "Customer not found"}, 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
