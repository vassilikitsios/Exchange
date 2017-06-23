'''
Author: Vassili Kitsios
'''

class Orders(object):
    '''
    Class that contains order information extracted from a standardised input order string.
    '''

    def __init__(self, ):
        '''
        Constructor initialisation
        '''
        self.trader_name = ''
        self.market_name = ''
        self.volume = 0.0
        self.is_long = False
        self.price = 0.0
        return


    def set_parameters(self, order_string):
        '''
        Extracts order information from standard order string input
        '''
        order_string_elements = order_string.split(":")
        if len(order_string_elements) == 4:
            self.trader_name = order_string_elements[0]
            self.market_name = order_string_elements[1]
            self.volume = int(order_string_elements[2])
            if self.volume>0.0:
                self.is_long = True
            price_string = order_string_elements[3].split("\n")[0]
            self.price = float(price_string)
        else:
            print('Invalid order entry')
        return


    def print(self, ):
        '''
        Prints order information to standard output
        '''
        print(self.trader_name, self.market_name, self.volume, self.is_long, self.price, sep=':')
        return
