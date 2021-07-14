from lib.candle_data import get_one_minute_candles_from_coinbase

import datetime

class ExchangeClient:
    """ Wrapper around different exchange clients to fetch candles.
    """

    def __init__(self, exchange):
        self.exchange = exchange

    def fetch(self, pair, start, end):
        fetch_func = {
            "coinbase": self.fetch_coinbase,
            "binance": self.fetch_binance
        }

        return fetch_func[self.exchange](pair, start, end)

    def fetch_coinbase(self, pair, start, end):
        """ time, low, high, open, close, volume
        """
        start_iso = datetime.datetime.fromtimestamp(start).isoformat()
        end_iso = datetime.datetime.fromtimestamp(end).isoformat()
        result = get_one_minute_candles_from_coinbase(pair, start_iso, end_iso)
        if "message" in result:
            raise ValueError(result)
        return result

    def fetch_binance(self, pair, start, end):
        pass