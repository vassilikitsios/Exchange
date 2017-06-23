#====================================================================
# CODE OVERVIEW
#====================================================================

Author: Vassili Kitsios

This program matches up a series of input orders into matching trades

To run the code type the following at the command line.
    ./run_exchange

To run the unit tests type the following at the command line.
    ./run_tests

#====================================================================
# LIST OF FILES AND DIRECTORIES
#====================================================================

libExchange/	                - contains classes used in main program
libExchange/markets.py	        - class to match orders to create trades
libExchange/orders.py	        - class specifying order properties and functionality
libExchange/trades.py	        - class specifying trade properties and functionality

Exchange.py	                    - main program

orders.txt	                    - input data set
trades.txt	                    - output data set

orders-01.txt	                - test input data set 1
orders-02.txt	                - test input data set 2

orders-01.correct_output.txt	- correct output for test input data set 1
orders-02.correct_output.txt	- correct output for test input data set 2

orders-01.output_diff.txt	    - difference between output and correct output for test input data set 1
orders-02.output_diff.txt	    - difference between output and correct output for test input data set 2

README.md	                    - this readme file

#====================================================================