import json
import datetime

def concat(exchange, pair):
    return exchange + "|" + pair

def save_db(db):
    with open("db.json", "w+") as file:
        file.write(json.dumps(db, sort_keys=True))

def load_db():
    with open("db.json", "r") as file:
        db = json.load(file)
    return db

def is_current_minute(timestamp):
    """ TODO: Implement this.
    """
    return False

def floor_timestamp(timestamp):
    tm = datetime.datetime.fromtimestamp(timestamp)
    tm -= datetime.timedelta(seconds=tm.second,
                             microseconds=tm.microsecond)
    return tm.timestamp()

def ciel_timestamp(timestamp):
    tm = datetime.datetime.fromtimestamp(timestamp)
    if tm.second == 0 and tm.microsecond == 0:
        return timestamp

    tm -= datetime.timedelta(seconds=tm.second,
                             microseconds=tm.microsecond)
    tm += datetime.timedelta(minutes=1)

    return tm.timestamp()