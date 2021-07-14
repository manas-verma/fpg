import json
from typing import List, Union

import requests


def get_one_minute_candles_from_coinbase(
    currency_pair: str,
    start_utc_datetime: str,
    end_utc_datetime: str
) -> List[List[Union[str, float]]]:
    """Return one minute candles for the currency pair from Coinbase.

    start/end_utc_datetime should be ISO 8601 formatted datetime strings, for example
    2014-11-06T10:34:47.123456Z.

    This endpoint is document at https://docs.pro.coinbase.com/#get-historic-rates.

    Notes
        - start timestamps are rounded up to the next minute. 12:00:50 will
          have the candle from 12:01 to 12:02 as the first candle
        - end timestamps are inclusive. If the end is 12:00:00, the candle for
          12:00 to 12:01 will be included. To avoid this, use 11:59:59
          as the end timestamp.
    """

    candles_resp = requests.get(
        f'https://api.exchange.coinbase.com/products/{currency_pair}/candles',
        params={
            'start': start_utc_datetime,
            'end': end_utc_datetime
        }
    )
    return json.loads(candles_resp.content)
