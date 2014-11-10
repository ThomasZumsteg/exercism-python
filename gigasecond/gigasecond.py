"""Adds a gigaseconds to a give date"""

from datetime import timedelta

def add_gigasecond(now):
    """Adds a gigaseconds to a given date"""
    return now + timedelta(seconds=10**9)
