============
Account Data
============

Access balances, orders, and margin position. All account data enpoints **require username and password**.

----------------
Account Balances
----------------

Latest account balances

Usage::

    c.my_funds()

Output::

      {'Liquid BTC': '0.00000000',
       'Liquid USD': '2.19',
       'Margin Account BTC': '0.00000000',
       'Margin Account USD': '0.00',
       'Total BTC': '15.00000000',
       'Total USD': '74.58'}

-----------
Orders List
-----------

Latest orders buy or sell.

Usage::

    c.my_orders()

Output::

      {'Buy': [{'Dark Pool': 'No',
         'Fill Type': 'Incremental',
         'Margin Percent': 'None',
         'Order Entered': '2012-04-10 08:59:51',
         'Order Expiry': '2012-05-11 00:00:00',
         'Order ID': '239801',
         'Order Type': 'Quick Buy',
         'Price': '4.50',
         'Quantity': '16.00000000',
         'Stop-loss': 'No'}],
       'Sell': [{'Dark Pool': 'No',
         'Fill Type': 'Incr',
         'Margin Percent': 'None',
         'Order Entered': '2012-04-05 22:07:05',
         'Order Expiry': '2012-05-06 00:00:00',
         'Order ID': '215603',
         'Order Type': 'Quick Sell',
         'Price': '5.20',
         'Quantity': '15.00000000',
         'Stop-loss': 'No'}]}

----------------
Margin positions
----------------

Open margin positions

Usage::

    c.my_margins()

Output::

      {'Margins': [{'Info': 'No open Margin positions.'}]}
