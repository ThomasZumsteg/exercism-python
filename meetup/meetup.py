"""Returns a datetime date object for a given year, month, and weekday that meet
a predefined natrual language description. e.g. 1st, 2nd, last, teenth
"""

import datetime

def meetup_day(year, month, weekday, condition):
    """Returns date object for a given year, month, weekday and given condition
    Current conditions [1-4]th occurence, last, teenth
    """

    # Conversion of string weekday to number
    weekday_to_num = {'Monday'   : 0,
                      'Tuesday'  : 1,
                      'Wednesday': 2,
                      'Thursday' : 3,
                      'Friday'   : 4,
                      'Saturday' : 5,
                      'Sunday'   : 6,
                     }

    def last(day):
        """True on the last week of the month"""
        return day.month != (day + datetime.timedelta(days=7)).month

    def nth(n):
        """Returns a function that is true on the nth week of a month"""
        def nth_worker(day):
            """True on the nth week of the month"""
            return (day.day - 1) // 7 == n-1
        return nth_worker

    def teenth(day):
        """True on a days ending in -teenth, ie seventeenth"""
        return 13 <= day.day and day.day <= 19

    # Maps condition to function test
    conditions = {'teenth': teenth,
                  'last': last,
                  '1st': nth(1),
                  '2nd': nth(2),
                  '3rd': nth(3),
                  '4th': nth(4),
                 }

    day = datetime.date(year, month, 1)
    # Tests everyday in the month until the weekday and condition are met
    while day.month == month:
        if day.weekday() == weekday_to_num[weekday] and \
            conditions[condition](day):
            return day
        day += datetime.timedelta(days=1)
