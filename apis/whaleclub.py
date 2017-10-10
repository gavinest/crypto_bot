import os
import requests

from utils.password_vault import passwordVault

'''
http://docs.whaleclub.co/
'''

WHALEHEAD_DEMO_API_TOKEN =  passwordVault.get('WHALECLUB_BTC_DEMO')

BASE_URL = 'https://api.whaleclub.co/v1/'

HEADERS = {
    'Authorization': 'Bearer ' + WHALEHEAD_DEMO_API_TOKEN,
    }

class MarketsEndpoint(object):
    '''
    Returns market information for one or more markets.
    '''

    ENDPOINT_URL = 'markets'

    @classmethod
    def get(cls, symbols):
        symbols = ','.join(symbols)
        r = requests.get(
                os.path.join(BASE_URL, cls.ENDPOINT_URL, symbols),
                headers=HEADERS,
                )
        return r.json()

class PriceEndpoint(object):
    '''
    Returns the current bid and ask prices for one or more markets.
    '''

    ENDPOINT_URL = 'price'

    @classmethod
    def get(cls, symbols):
        symbols = ','.join(symbols)
        r = requests.get(
                os.path.join(BASE_URL, cls.ENDPOINT_URL, symbols),
                headers=HEADERS,
                )
        return r.json()

class BalanceEndpoint(object):
    '''
    Returns information about your balance.
    '''

    ENDPOINT_URL = 'balance'

    @classmethod
    def get(cls):
        r = requests.get(
                os.path.join(BASE_URL, cls.ENDPOINT_URL),
                headers=HEADERS,
                )
        return r.json()

class TransactionsEndpoint(object):
    '''
    List transactions that have occurred on your account.

    types: deposits, withdrawals, referrals, or bonuses
    '''

    ENDPOINT_URL = 'transactions'
    PAYLOAD = {
        'limit': 50,
        }

    @classmethod
    def get(cls, transaction_type='deposits'):
        r = requests.get(
                os.path.join(BASE_URL, cls.ENDPOINT_URL, transaction_type),
                headers=HEADERS,
                params=cls.PAYLOAD,
                )
        return r.json()

class PositionsEndpoint(object):
    pass

class PositionsTurboEndpoint(object):
    pass

if __name__ == '__main__':
    # m = MarketsEndpoint.get(['XAU-USD', 'AAPL'])
    # p = PriceEndpoint.get(['XAU-USD', 'AAPL'])
    b = BalanceEndpoint.get()
