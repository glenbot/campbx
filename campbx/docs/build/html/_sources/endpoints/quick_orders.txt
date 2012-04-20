==============
Quick sell/buy
==============

Execute quick sell or quick buy orders. Cancel orders.

-----------------------
Canceling an open order
-----------------------

Cancel an order

Parameters

* Type -  The order type. This is either *Buy* or *Sell*
* OrderID - The ID of the order. You can get this from `c.my_orders()` in :doc:`Account Data </endpoints/account_data>`.

.. note::

    The parameters for this call are case-sensitive.

Usage::

    c.trade_cancel({
        'Type': 'Buy',
        'OrderID': 239801
    })

Output::

    {'Success': 'Order ID 239801 was deleted successfully.'}

-------------------
Placing a new order
-------------------

Place a buy or sell order

Parameters

* TradeMode -  *QuickBuy* or *QuickSell*
* Quantity - The amount of Bitcoins to buy or sell
* Price - The price at which you are willing to buy or sell the Bitcoins.

.. note::

    Orders stay open on CampBX order book for up to 31 days. Quantity and Price are decimal values that must follow all rules / limits set by CampBX. Minimum quantity to place an order is 0.1 Bitcoins.

Usage::

    c.trade_enter({
        'TradeMode': 'QuickSell',
        'Quantity': '10.0',
        'Price': '4.50'
    })

Output::

    {'Success': '0'}
