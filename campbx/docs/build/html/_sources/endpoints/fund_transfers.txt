==============
Fund Transfers
==============

Send Bitcoins to other CampBX users, bitcoint addresses, or get your deposit address

------------------------------
Instant, Free Bitcoin Transfer
------------------------------

If you need to send Bitcoins to other CampBX users, we recommend using this. This call provides two distinct advantages over the traditional method of sending Bitcoin to an address: 

* You can send Bitcoin instantly - there is no need to wait for confirmations from the Bitcoin network.
* You do not need to pay miner fees to transfer Bitcoins.

Parameters

* CBXCode - A valid CampBX account code
* BTCAmt - A decimal amount less than your account balance

Usage::

    c.send_instant({
      'CBXCode': 'some_code',
      'BTCAmt': '2.50',
    })

API call returns "Success" if account-to-account transfer is successful. The transaction will appear in your timeline as "CBX Instant Send/Receive".

.. note::

  The default withdrawal limit is 500 Bitcoins per 24 hours, and it can be raised by submitting a ticket to the helpdesk.

-----------------
Bitcoin desposits
-----------------

Get your Bitcoin deposit address

Usage::

    c.get_btc_address()

Output::

    {'Success': 'your_deposit_address'}

---------------
Bitcoin send-to
---------------

Send Bitcoins to any address

Parameters::

* BTCTo -  A valid Bitcoin address
* BTCAmt - A decimal amount less than your account balance

Usage::

    c.send_btc({
      'BTCTo': 'bitcoin_address',
      'BTCAmt': '100.00',
    })

Output::

    {'Success': 'transfer_id'}

.. note::

  The default withdrawal limit is 500 Bitcoins per 24 hours, and it can be raised by submitting a ticket to the helpdesk.