import datetime
import pytz

current_date = datetime.datetime.now(pytz.timezone('Africa/Abidjan'))


def get_timestamp():
    currentdate = datetime.datetime.now(pytz.timezone('Africa/Abidjan'))
    return currentdate
