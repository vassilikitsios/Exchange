'''
Author: Vassili Kitsios
'''
import operator
from libExchange.trades import Trades

class Markets(object):
    '''
    Class that matches a list of orders to create a list of trades.
    '''

    def __init__(self, ):
        '''
        Constructor initialisation
        '''
        self.trade_list = list()
        return


    def match_orders(self, order_list):
        '''  Creates a list of trades by matching a list of orders'''

        while len(order_list)>0:

            found_matching_order, initial_order, matching_order, assessed_orders = \
                self.find_next_matching_orders(order_list)

            if found_matching_order:
                trade = Trades()
                remaining_initial_order_volume, remaining_matching_order_volume = \
                    trade.set_parameters(initial_order, matching_order)
                self.trade_list.append(trade)
                del trade
                order_list = self.update_order_list(order_list, initial_order, matching_order, \
                    remaining_initial_order_volume, remaining_matching_order_volume)
            else:
                for order in assessed_orders:
                    order_list.remove(order)
        return


    def find_next_matching_orders(self, order_list):
        '''
        Find matching orders. A match occurs between two limit orders when:
            * Both orders are for the same instrument
            * One order is a buy (+ve signed quantity) and the other is a sell (-ve signed quantity)
            * The “buy” limit price is equal to or higher than the “sell” limit price
        Note:
            * Orders should be processed and matched in order of receipt.
            * When multiple orders are candidates for matching against a new order,
            matching should be against the most aggressively priced candidate
            (lowest price for sells, highest price for buys).
            * If multiple candidates have the most aggressive price, matching should
            occur against the candidate first received.
            * A buyer is allowed to trade with itself (ie. Orders do not need different
            buyer/seller ids to match)
        '''
        found_matching_order = False
        initial_order = []
        matching_order = []

        assessed_orders = [i for i in order_list \
            if i.market_name == order_list[0].market_name]
        long_orders = [i for i in order_list \
            if i.market_name == order_list[0].market_name and i.is_long]
        short_orders = [i for i in order_list \
            if i.market_name == order_list[0].market_name and not i.is_long]

        if len(short_orders)>0 and len(long_orders)>0:
            short_orders.sort(key=operator.attrgetter('price'))
            long_orders.sort(key=operator.attrgetter('price'))
            short_order_with_best_price = short_orders[0]
            long_order_with_best_price = long_orders[-1]

            if long_order_with_best_price.price>=short_order_with_best_price.price:
                found_matching_order = True
                if order_list.index(short_order_with_best_price) \
                        < order_list.index(long_order_with_best_price):
                    initial_order = short_order_with_best_price
                    matching_order = long_order_with_best_price
                else:
                    initial_order = long_order_with_best_price
                    matching_order = short_order_with_best_price

        return found_matching_order, initial_order, matching_order, assessed_orders


    def update_order_list(self, order_list, initial_order, matching_order, \
        remaining_initial_order_volume, remaining_matching_order_volume):
        '''
        Remove filled orders, and update volume on order with remaining volume.
        '''
        if abs(remaining_initial_order_volume)>0:
            index = order_list.index(initial_order)
            order_list[index].volume = remaining_initial_order_volume
            order_list.remove(matching_order)
        elif abs(remaining_matching_order_volume)>0:
            index = order_list.index(matching_order)
            order_list[index].volume = remaining_matching_order_volume
            order_list.remove(initial_order)
        else:
            order_list.remove(matching_order)
            order_list.remove(initial_order)
        return order_list


    def print(self, ):
        '''
        Prints list of matching trade to standard output
        '''
        for trade in self.trade_list:
            trade.print()
        return
