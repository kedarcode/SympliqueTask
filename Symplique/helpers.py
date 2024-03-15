import pytz
def get_all_timezones():
    return list(pytz.all_timezones)

def validate_timezone(timezone_str):
    return timezone_str in pytz.all_timezones
