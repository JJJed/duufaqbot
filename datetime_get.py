import datetime
import pytz

current_date = datetime.datetime.now(pytz.timezone('Africa/Abidjan'))


def get_timestamp():
    current_date = datetime.datetime.now(pytz.timezone('Africa/Abidjan'))
    return current_date
