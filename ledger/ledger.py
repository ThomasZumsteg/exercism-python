# -*- coding: utf-8 -*-
from datetime import datetime
from collections import namedtuple


Local = namedtuple('Local', ('date', 'words', 'number'))


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
    return '{month:02d}/{day:02d}/{year:04d}'.format(month=month, day=day, year=year)

def nl_date(day, month, year):
    return '{day:02d}-{month:02d}-{year:04d}'.format(month=month, day=day, year=year)

def us_number(amount):

    pass

def nl_number(amount):
    pass

def format_entries(currency, locale, entries):
    localization = {
        'en_US':  (
            '{month:02d}/{day:02d}/{year:04d} | {desc:<25s} | ',
             {"Date": "Date", "Description": "Description", "Change": "Change"}),
        'nl_NL': (
            '{day:02d}-{month:02d}-{year:04d} | {desc:<25s} | ',
            {"Date": "Datum", "Description": "Omschrijving", "Change": "Verandering"})
    }
    # Generate Header Row
    table = ["{Date:10s} | {Description:25s} | {Change:13s}".format(**localization[locale][1])]
    if locale == 'en_US':
        while len(entries) > 0:
            table.append('')

            # Find next entry in order
            min_entry_index = -1
            for i, entry in enumerate(entries):
                min_entry = entries[min_entry_index]
                if entry.date < min_entry.date:
                    min_entry_index = i
                elif (
                    entry.date == min_entry.date and
                    entry.change < min_entry.change
                ):
                    min_entry_index = i
                elif (
                    entry.date == min_entry.date and
                    entry.change == min_entry.change and
                    entry.description < min_entry.description
                ):
                    min_entry_index = i
            entry = entries[min_entry_index]
            entries.pop(min_entry_index)

            desc = entry.description
            table[-1] += localization['en_US'][0].format(
                    day=entry.date.day,
                    month=entry.date.month,
                    year=entry.date.year,
                    desc=(desc if len(desc) <= 25 else desc[:22] + '...'))

            # Write entry change to table
            if currency == 'USD':
                change_str = ''
                if entry.change < 0:
                    change_str = '('
                change_str += '$'
                change_dollar = abs(int(entry.change / 100.0))
                dollar_parts = []
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                if len(dollar_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += dollar_parts[0]
                        dollar_parts.pop(0)
                        if len(dollar_parts) == 0:
                            break
                        change_str += ','
                change_str += '.'
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                if entry.change < 0:
                    change_str += ')'
                else:
                    change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table[-1] += change_str
            elif currency == 'EUR':
                change_str = ''
                if entry.change < 0:
                    change_str = '('
                change_str += u'€'
                change_euro = abs(int(entry.change / 100.0))
                euro_parts = []
                while change_euro > 0:
                    euro_parts.insert(0, str(change_euro % 1000))
                    change_euro = change_euro // 1000
                if len(euro_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += euro_parts[0]
                        euro_parts.pop(0)
                        if len(euro_parts) == 0:
                            break
                        change_str += ','
                change_str += '.'
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                if entry.change < 0:
                    change_str += ')'
                else:
                    change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table[-1] += change_str
        return '\n'.join(table)
    elif locale == 'nl_NL':
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
            table[-1] += localization['nl_NL'][0].format(
                day=entry.date.day,
                month=entry.date.month,
                year=entry.date.year,
                desc=(desc if len(desc) <= 25 else desc[:22] + '...'))

            # Write entry change to table
            if currency == 'USD':
                change_str = '$ '
                if entry.change < 0:
                    change_str += '-'
                change_dollar = abs(int(entry.change / 100.0))
                dollar_parts = []
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                if len(dollar_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += dollar_parts[0]
                        dollar_parts.pop(0)
                        if len(dollar_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table[-1] += change_str
            elif currency == 'EUR':
                change_str = u'€ '
                if entry.change < 0:
                    change_str += '-'
                change_euro = abs(int(entry.change / 100.0))
                euro_parts = []
                while change_euro > 0:
                    euro_parts.insert(0, str(change_euro % 1000))
                    change_euro = change_euro // 1000
                if len(euro_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += euro_parts[0]
                        euro_parts.pop(0)
                        if len(euro_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table[-1] += change_str
        return '\n'.join(table)
