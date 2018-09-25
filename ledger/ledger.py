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


def us_date(day, month, year):
    return '{:02d}/{:02d}/{:04d}'.format(month, day, year)

def nl_date(day, month, year):
    return '{:02d}-{:02d}-{:04d}'.format(day, month, year)

def us_number(amount, currency):
    fmt_str = '{}{:s}.{:02d} '
    if amount < 0:
        fmt_str = '({}{:s}.{:02d})'
    units, change = abs(amount) // 100, abs(amount) % 100
    digits = str(units)[::-1]
    return fmt_str.format(
        currency,
        ','.join(reversed(list(''.join(
            reversed(digits[l:l+3])) for l in range(0, len(digits), 3)))),
        change)

def nl_number(amount, currency):
    fmt_str = '{} {:s},{:02d} '
    if amount < 0:
        fmt_str = '{} -{:s},{:02d} '
    units, change = abs(amount) // 100, abs(amount) % 100
    digits = str(units)[::-1]
    return fmt_str.format(
        currency,
        '.'.join(reversed(list(''.join(
            reversed(digits[l:l+3])) for l in range(0, len(digits), 3)))),
        change)

def format_entries(currency, locale, entries):
    localization = {
        'en_US':  Local(
             {"Date": "Date", "Description": "Description", "Change": "Change"},
            us_date,
            us_number),
        'nl_NL': Local(
            {"Date": "Datum", "Description": "Omschrijving", "Change": "Verandering"},
            nl_date,
            nl_number)
    }
    # Generate Header Row
    config = localization[locale]
    table = ["{Date:10s} | {Description:25s} | {Change:13s}".format(**config.dict)]
    while len(entries) > 0:
        table.append('')

        # Find next entry in order
        min_entry_index = -1
        for i, entry in enumerate(entries):
            if min_entry_index < 0:
                min_entry_index = i
                continue
            min_entry = entries[min_entry_index]
            if entry.date < min_entry.date:
                min_entry_index = i
                continue
            if (
                entry.date == min_entry.date and
                entry.change < min_entry.change
            ):
                min_entry_index = i
                continue
            if (
                entry.date == min_entry.date and
                entry.change == min_entry.change and
                entry.description < min_entry.description
            ):
                min_entry_index = i
                continue
        entry = entries[min_entry_index]
        entries.pop(min_entry_index)

        desc = entry.description
        table[-1] += '{:s} | {:<25s} | {:>13s}'.format(
                config.date(entry.date.day, entry.date.month, entry.date.year),
                desc if len(desc) <= 25 else desc[:22] + '...',
                config.number(entry.change, '$' if currency == "USD" else u'€'))
    return '\n'.join(table)
