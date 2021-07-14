import util

class DataCache:

    def __init__(self, exchange, pair):
        self.table = util.concat(exchange, pair)
        self.db = util.load_db()

    def load(self, start, end):
        """ Loads data from database.
        """
        results = []
        for values in self.db.get(self.table, []):
            if start > values[0]:
                continue
            if end < values[0]:
                break
            results.append(values)
        return results

    def save(self, data):
        """ TODO: Check if saved values includes current minute.
        """
        self.db[self.table] = self.db.get(self.table, [])

        # Can be optimized by merging in pre-sorted lists.
        self.db[self.table].extend(data)
        data = self.db[self.table]
        data = [tuple(values) for values in data]
        self.db[self.table] = list(sorted(set(data)))

        # Remove the last minute if it is the current minute,
        # since current minute data is incomplete.
        if util.is_current_minute(self.db[self.table][-1][0]):
            self.db[self.table].pop(-1)

        util.save_db(self.db)