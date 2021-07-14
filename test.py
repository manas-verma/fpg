from data_cache import DataCache
from exchange_client import ExchangeClient
import src.api_handler


def test():
    START = "2021-07-06T10:34:47.123456"
    END = "2021-07-06T11:34:47.123456"
    print(src.api_handler.get_candle_data("LTC-EUR", START, END))

def test_one():
    START = 1626293010
    END = 1626294070

    print("Initializing DB")
    dc = DataCache("coinbase", "LTC-EUR")
    print("Load data")
    print(dc.load(START, END))

    print("Fetching data")
    data = ExchangeClient("coinbase").fetch("LTC-EUR", START, END)
    print(data)

    print("Saving then loading...")
    dc.save(data)
    print(dc.load(START, END))


if __name__ == '__main__':
    test()