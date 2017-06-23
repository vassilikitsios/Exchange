#!/usr/bin/env python
'''
Author: Vassili Kitsios

This program matches up a series of input orders into matching trades
'''

import sys
from libExchange.orders import Orders
from libExchange.markets import Markets

#=====================================================================
# Helper functions
#=====================================================================
def get_order_string_list():
    ''' Reads order string list from standard input '''
    order_string_list = list()
    for line in sys.stdin:
        # To ignore blank lines
        if len(line)>1:
            order_string_list.append(line)
    return order_string_list


def populate_order_list(order_string_list):
    ''' Populates a list of orders from the order input data '''
    order_list = list()
    for line in order_string_list:
        order = Orders()
        order.set_parameters(line)
        order_list.append(order)
        del order
    return order_list


#=====================================================================
# Main program
#=====================================================================
if __name__ == '__main__':
    order_string_list = get_order_string_list()

    order_list = populate_order_list(order_string_list)

    market = Markets()
    market.match_orders(order_list)
    market.print()
