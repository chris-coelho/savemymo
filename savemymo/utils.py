
def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a pretty string like
    'an hour ago', 'Yesterday', '3 months ago', 'just now', etc
    EXTRACTED FROM STACKOVERFLOW - TODO: Improvements if necessary
    https://stackoverflow.com/questions/1551382/user-friendly-time-format-in-python
    """
    from datetime import datetime
    full_now = datetime.now()
    now = datetime(
        full_now.year,
        full_now.month,
        full_now.day,
        full_now.hour,
        full_now.minute,
        full_now.second
    )
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        time = datetime(
            time.year,
            time.month,
            time.day,
            time.hour,
            time.minute,
            time.second
        )
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff / 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff / 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"