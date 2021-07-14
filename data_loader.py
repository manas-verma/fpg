from data_cache import DataCache
from exchange_client import ExchangeClient
import util

class DataLoader:

    def load(self, exchange, pair, start, end):
        start = util.floor_timestamp(start)
        end = util.ciel_timestamp(end)
        data_cache = DataCache(exchange, pair)
        self.exchange_client = ExchangeClient(exchange)

        data = data_cache.load(start, end)
        start_end_times = self.get_start_end_times(data, start, end)

        for start, end in start_end_times:
            new_data = self.exchange_client.fetch(pair, start, end)
            data.extend(new_data)
        data_cache.save(data)

        return data_cache.load(start, end)

    def get_start_end_times(self, data, start, end):
        # Consider using the window for fewer requests.
        # window = self.exchange_client.window()

        expected_num = 1 + (end - start) // 60
        if len(data) == expected_num:
            return []
        return [(start, end)]



