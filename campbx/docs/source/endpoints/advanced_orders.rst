===============
Advanced Orders
===============

Execute advanced orders with more options

**Required Parameters**

* TradeMode -  *AdvancedBuy* or *AdvancedSell*.
* Price - Decimal or *Market*. The price at which you are willing to buy or sell the Bitcoins.
* Quantity - The amount of Bitcoins to buy or sell.

*Optional Parameters*

* FillType - *Incremental*, *AON*, or *FOK*. Default is *Incremental*.
* DarkPool - Use darkpools. *Yes* or *No*. Default is *No*.
* Expiry - The expiraton on the order in the *YYYY/MM/DD* format.

.. note::

    Allowed Expiry range is 1 Hour through 31 Days.

.. note::

    Please note that all parameters are case-sensitive. CampBX highly recommends executing small trades and experimenting with all of the possible parameter values before implementing them in your strategy.
    Expiry date field allows using many relative and absolute values and offers a lot of flexibility. If this is something that you rely on heavily in your strategy, please contact CampBX for details about additional formats.

Usage::

    c.trade_advanced({
        'TradeMode': 'AdvancedBuy',
        'Price': 'Market',
        'Quantity': '16.00'
    })

Output::

    {'Success': '0'}
