'''
Author: Vassili Kitsios
'''

class Trades(object):
    '''
    Class that contains trade information matched from a set of orders.
    '''

    def __init__(self, ):
        '''
        Constructor initialisation
        '''
        self.buyer_name = ''
        self.seller_name = ''
        self.market_name = ''
        self.volume = 0.0
        self.price = 0.0
        return


    def set_parameters(self, order1, order2):
        '''
        Sets trade information from matching trades, and determines
        any unfilled volume.
        '''
        if order1.volume>0:
            self.buyer_name = order1.trader_name
            self.seller_name = order2.trader_name
        else:
            self.buyer_name = order2.trader_name
            self.seller_name = order1.trader_name
        self.market_name = order1.market_name
        self.price = order1.price
        self.volume = min(abs(order1.volume), abs(order2.volume))

        remaining_order1_volume = abs(abs(self.volume) - abs(order1.volume)) \
            * order1.volume/abs(order1.volume)
        remaining_order2_volume = abs(abs(self.volume) - abs(order2.volume)) \
            * order2.volume/abs(order2.volume)

        return remaining_order1_volume, remaining_order2_volume


    def print(self, ):
        '''
        Prints matching trade to standard output
        '''
        print(self.buyer_name, self.seller_name, self.market_name, int(self.volume), self.price, sep=':')
        return
