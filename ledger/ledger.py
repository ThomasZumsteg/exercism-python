# -*- coding: utf-8 -*-
from datetime import datetime
from collections import namedtuple


Local = namedtuple('Local', ('dict', 'date', 'number'))


class LedgerEntry(object):
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    return entry

def number(pos, neg, sep):
    def wrapped(amount, currency):
        fmt_str = pos if amount >= 0 else neg 
        units, change = abs(amount) // 100, abs(amount) % 100
        digits = str(units)[::-1]
        return fmt_str.format(
            currency,
            sep.join(reversed(list(''.join(
                reversed(digits[l:l+3])) for l in range(0, len(digits), 3)))),
            change)
    return wrapped

def format_entries(currency, locale, entries):
    localization = {
        'en_US':  Local(
             {"Date": "Date", "Description": "Description", "Change": "Change"},
            lambda day, month, year: '{:02d}/{:02d}/{:04d}'.format(month, day, year),
            number('{}{:s}.{:02d} ', '({}{:s}.{:02d})', ',')),
        'nl_NL': Local(
            {"Date": "Datum", "Description": "Omschrijving", "Change": "Verandering"},
            lambda day, month, year: '{:02d}-{:02d}-{:04d}'.format(day, month, year),
            number('{} {:s},{:02d} ', '{} -{:s},{:02d} ', '.'))
    }
    symbols = {"USD": "$", "EUR": "€"}
    # Generate Header Row
    config = localization[locale]
    table = ["{Date:10s} | {Description:25s} | {Change:13s}".format(**config.dict)]
    for entry in sorted(entries, key=lambda e: (e.date, e.change, e.description)):

        desc = entry.description
        table.append('{:s} | {:<25s} | {:>13s}'.format(
                config.date(entry.date.day, entry.date.month, entry.date.year),
                desc if len(desc) <= 25 else desc[:22] + '...',
                config.number(entry.change, symbols[currency])))
    return '\n'.join(table)
