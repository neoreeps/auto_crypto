#!/usr/bin/env python3

import cbpro
import json
import argparse

def get_args():
    """ Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description='Crypto Tools')
    parser.add_argument('--key', required=True,
            help='CBP API Key')
    parser.add_argument('--secret', required=True,
            help='CBP API Super Secret')
    parser.add_argument('--passwd', required=True,
            help='CBP API Key Password')
    parser.add_argument('--crypto', default='BTC-USD',
            help='The crypto type to operate on.')
    parser.add_argument('--action', default='accounts',
            choices=['accounts', 'buy', 'sell', 'deposit'],
            help='The type of action to perform.')
    parser.add_argument('--amount', default=0.00,
            help='The amount to deposit, buy, or sell.')
    parser.add_argument('--currency', default='USD',
            help='The currency to use for buy/sell actions.')
    parser.add_argument('--method_id', default=None,
            help='The method ID for payment.')
    return parser.parse_args()
   

def main(cargs):
    """
    Main function, parses the arguments and executes.

    # deposits require amount, currency, and method_id
    # method_id can be obtained from get_payment_methods()

    # buying requires the form 'BTC-USD' so build it based on params
    # simply use market order since we are buying and forgetting
    """
    # create the authenticated client
    client = cbpro.AuthenticatedClient(cargs.key, cargs.secret, cargs.passwd)

    # for accounts (default) just list any holdings and amounts
    if cargs.action == "accounts":
        accounts = client.get_accounts()
        for account in accounts:
            if float(account['balance']) > 0.0:
                print(f"type: {account['currency']}\t{account['balance']}")
        status = {'message': 'accounts retrieved successfully'}
    elif cargs.action == "deposit":
        status = client.deposit(cargs.amount, cargs.currency, cargs.method_id)
    elif cargs.action == "buy":
        status = client.place_market_order(f'{cargs.crypto}-{cargs.currency}',
                'buy', None, cargs.amount)
    else:
        status = {'error': f'{cargs.action} is not defined'}

    print(json.dumps(status, indent=2))
    return



if __name__ == "__main__":

    # parse args and execute
    main(get_args())
