import urllib2
import base64
import simplejson as json
import logging
from urllib import urlencode
from functools import partial

log = logging.getLogger(__name__)
log_formatter = logging.Formatter('%(name)s - %(message)s')
log_handler = logging.StreamHandler()

log_handler.setFormatter(log_formatter)
log.addHandler(log_handler)
log.setLevel(logging.ERROR)


class EndPointPartial(partial):
    def __new__(cls, func, conf, _repr):
        cls._repr = _repr
        return super(EndPointPartial, cls).__new__(cls, func, conf)

    def __repr__(self):
        return unicode('<API endpoint %s>' % self._repr)


class CampBX(object):
    """Camp BX API Class"""
    username = None
    password = None
    api_url = 'https://campbx.com/api/'
    log = None

    # API endpoints
    # { python_call : (url_php_call, requires_auth) }
    endpoints = {
        'xdepth': ('xdepth', False),
        'xticker': ('xticker', False),
        'my_funds': ('myfunds', True),
        'my_orders': ('myorders', True),
        'my_margins': ('mymargins', True),
        'get_btc_address': ('getbtcaddr', True),
        'send_instant': ('sendinstant', True),
        'send_btc': ('sendbtc', True),
        'trade_cancel': ('tradecancel', True),
        'trade_enter': ('tradeenter', True),
        'trade_advanced': ('tradeadv', True),
    }

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

        # setup logging
        self.log = log

        # append all the enpoints to the class dictionary
        self._create_endpoints()

    def debug_mode(self, toggle):
        """
        Toddle debug mode for more detailed output
          obj.debug_mode(True) - Turn debug mode on
          obj.debug_mode(False) - Turn debug mode off
        """
        if toggle:
            self.log.setLevel(logging.DEBUG)
        else:
            self.log.setLevel(logging.ERROR)

    def _make_request(self, conf, post_params={}):
        """Make a request to the API and return data in a pythonic object"""
        endpoint, requires_auth = conf

        # setup the url and the request objects
        url = '%s%s.php' % (self.api_url, endpoint)
        log.debug('Setting url to %s' % url)
        request = urllib2.Request(url)

        # tack on authentication if needed
        log.debug('Post params: %s' % post_params)
        if requires_auth:
            post_params.update({
                'user': self.username,
                'pass': self.password
            })

        # url encode all parameters
        data = urlencode(post_params)

        # gimme some bitcoins!
        try:
            log.debug('Requesting data from %s' % url)
            response = urllib2.urlopen(request, data)
            return json.loads(response.read())
        except urllib2.URLError, e:
            log.debug('Full error: %s' % e)
            if hasattr(e, 'reason'):
                self.log.error('Could not reach host. Reason: %s' % e.reason)
            elif hasattr(e, 'code'):
                self.log.error('Could not fulfill request. Error Code: %s' % e.code)
            return None

    def _create_endpoints(self):
        """Create all api endpoints using self.endpoint and partial from functools"""
        for k, v in self.endpoints.items():
            _repr = '%s.%s' % (self.__class__.__name__, k)
            self.__dict__[k] = EndPointPartial(self._make_request, v, _repr)
