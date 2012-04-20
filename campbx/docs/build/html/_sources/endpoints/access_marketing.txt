==============
Marketing Data
==============

These endpoints are **public**. Username and password are not required. You can use them to retrieve current market data such as price, last trade, etc.

-----------
Depth Table
-----------

Full market depth

Usage::

    c.xdepth()

Output::

    {'Asks': [[6.5, 9.0],
      [6, 19.5],
      [5.5, 5.0],
      [5.4, 17.95838012],
      [5.3, 2.0],
      [5.25, 2.0],
      [5.24, 2.0],
      [5.23, 2.0],
      [5.22, 2.0],
      [5.2, 16.33884797],
      [5.17, 128.98382722],
      [5.16, 8.71]],
     'Bids': [[5.13, 51.96],
      [5.12, 54.33980295],
      [5.11, 205.0],
      [5.1, 6.57211378],
      [5.07, 1.5],
      [5.06, 2.0],
      [5.03, 2.0],
      [5, 2.3],
      [4.91, 3.0],
      [4.9, 24.7],
      [4.81, 22.63227921],
      [4.77, 14.5947811],
      [4.76, 10.0],
      [4.75, 10.41848778],
      [4.74, 1.0],
      [4.5, 30.0],
      [3, 83.0]]}

-------------
Market Ticker
-------------

Get the best ask, best bid, and last trade

Usage::

    c.xticker()

Output::

    {'Best Ask': '5.17', 'Best Bid': '5.13', 'Last Trade': '5.13'}
