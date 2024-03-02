#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# SezimalCalendar - The Symmetry454 Calendar, with Holocene Epoch and Sezimal in Python
#
# Copyright (C) 2023–
# Copyright (C) Ari Caldeira <aricaldeira at gmail.com>
#
# Original calendar documentation is Public Domain by it’s author:
# http://individual.utoronto.ca/kalendis/symmetry.htm
#

__all__ = ('SezimalDate')

from typing import TypeVar

Self = TypeVar('Self', bound='SezimalDate')
SezimalTime = TypeVar('SezimalTime', bound='SezimalTime')
SezimalDateTime = TypeVar('SezimalDateTime', bound='SezimalDateTime')

import time as _time
import datetime as _datetime

from decimal import Decimal
from zoneinfo import ZoneInfo

from ..sezimal import Sezimal, SezimalInteger
from ..dozenal import Dozenal, DozenalInteger
from ..base import decimal_format, sezimal_format, \
    sezimal_to_niftimal, default_to_dedicated_digits, \
    default_niftimal_to_dedicated_digits, default_niftimal_to_regularized_digits, \
    default_niftimal_to_regularized_dedicated_digits
from .gregorian_functions import ordinal_date_to_gregorian_year_month_day
from ..units import AGRIMA_TO_SECOND, SECOND_TO_AGRIMA
from .date_time_delta import SezimalDateTimeDelta
from ..text import sezimal_spellout
from ..localization import sezimal_locale, DEFAULT_LOCALE, SezimalLocale
from .sezimal_functions import *
from .format_tokens import DATE_NUMBER_FORMAT_TOKENS, \
    YEAR_NUMBER_FORMAT_TOKENS, DATE_TEXT_FORMAT_TOKENS, \
    ISO_DATE_NUMBER_FORMAT_TOKENS


class SezimalDate:
    __slots__ = '_year', '_month', '_day', '_hashcode', '_gregorian_date', '_is_leap', '_ordinal_date', '_weekday', \
        '_day_in_year', '_day_in_week', '_week_in_year', \
        '_quarter', '_day_in_quarter', '_week_in_quarter', '_month_in_quarter'

    def __new__(
        cls,
        year: str | int | float | Decimal | Sezimal | SezimalInteger | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self,
        month: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        day: str | int | float | Decimal | Sezimal | SezimalInteger = None
        ) -> Self:
        if month is None:
            if type(year) in (_datetime.date, _datetime.datetime):
                return cls.from_ordinal_date(Decimal(year.toordinal()))

            elif type(year).__name__ in ('SezimalDate', 'SezimalDateTime', 'SezimalTime'):
                return cls.from_ordinal_date(year.ordinal_date)

            elif type(year) == str:
                if VALID_DATE_STRING.match(year):
                    year, month, day = year.split('-')

        year = SezimalInteger(year)
        month = SezimalInteger(month)
        day = SezimalInteger(day)

        check_date_fields(year, month, day)

        self = object.__new__(cls)
        self._year = year
        self._month = month
        self._day = day
        self._ordinal_date = year_month_day_to_ordinal(year, month, day)

        y, m, d, diy, wiy, q, diq, wiq, miq = ordinal_to_year_month_day(self._ordinal_date)

        self._day_in_year = diy
        self._week_in_year = wiy
        self._quarter = q
        self._day_in_quarter = diq
        self._week_in_quarter = wiq
        self._month_in_quarter = miq

        self._weekday = day % SezimalInteger(11)

        if self._weekday == 0:
            self._weekday = SezimalInteger(11)

        self._hashcode = -1
        self._is_leap = is_leap(year - ISO_YEAR_DIFF)

        gregorian_date = ordinal_date_to_gregorian_year_month_day(int(self._ordinal_date.decimal))

        if gregorian_date[0] >= 1 and gregorian_date[0] <= 9_999:
            self._gregorian_date = _datetime.date(*gregorian_date)
        else:
            self._gregorian_date = gregorian_date

        return self

    # Additional constructors

    @classmethod
    def from_timestamp(cls, timestamp) -> Self:
        "Construct a date from a POSIX timestamp (like time.time())."
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(timestamp)
        x = _datetime.date(y, m, d)
        return cls.from_ordinal_date(Decimal(x.toordinal()))

    @property
    def timestamp(self) -> float:
        timestamp = self.ordinal_date.decimal - POSIX_EPOCH.decimal
        timestamp *= 24 * 60 * 60
        return float(timestamp)

    @classmethod
    def today(cls) -> Self:
        "Construct a date from time.time()."
        t = _time.time()
        return cls.from_timestamp(t)

    @classmethod
    def from_ordinal_date(cls, ordinal_date) -> Self:
        ordinal_date = SezimalInteger(ordinal_date)
        y, m, d, *x = ordinal_to_year_month_day(ordinal_date)
        return cls(y, m, d)

    @classmethod
    def from_iso_format(cls, date_string) -> Self:
        return cls.from_ordinal_date(_datetime.date.fromisoformat(date_string).toordinal())

    @classmethod
    def from_iso_calendar(cls, year, week, day) -> Self:
        return cls.from_ordinal_date(_datetime.date.fromisocalendar(year, week, day).toordinal())

    def __repr__(self) -> str:
        return f'{self.__class__.__qualname__}({self.year.formatted_number}, {self.month}, {self.day})'

    @property
    def gregorian_date(self):
        return self._gregorian_date

    def ctime(self):
        return self.gregorian_date.ctime()

    def __format__(self, fmt):
        if not isinstance(fmt, str):
            raise TypeError("must be str, not %s" % type(fmt).__name__)
        if len(fmt) != 0:
            return self.format(fmt)
        return str(self)

    def isoformat(self) -> str:
        return f'{str(self.year).zfill(6)}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}'

    def isoformat_decimal(self) -> str:
        return f'{str(self.year.decimal).zfill(5)}-{str(self.month.decimal).zfill(2)}-{str(self.day.decimal).zfill(2)}'

    __str__ = isoformat

    @property
    def year(self) -> SezimalInteger:
        return self._year

    @property
    def month(self) -> SezimalInteger:
        return self._month

    @property
    def day(self) -> SezimalInteger:
        return self._day

    @property
    def is_leap(self) -> bool:
        return bool(self._is_leap)

    @property
    def is_long_month(self) -> bool:
        return self.month in (2, 5, 12, 15) or (self.is_leap and self.month == 20)

    @property
    def weekday(self) -> SezimalInteger:
        return self._weekday

    @property
    def week_in_month(self) -> SezimalInteger:
        if self.day <= 11:
            return SezimalInteger(1)
        elif self.day <= 22:
            return SezimalInteger(2)
        elif self.day <= 33:
            return SezimalInteger(3)
        elif self.day <= 44:
            return SezimalInteger(4)

        return SezimalInteger(5)

    @property
    def day_in_year(self) -> SezimalInteger:
        return self._day_in_year

    @property
    def week_in_year(self) -> SezimalInteger:
        return self._week_in_year

    @property
    def quarter(self) -> SezimalInteger:
        return self._quarter

    @property
    def day_in_quarter(self) -> SezimalInteger:
        return self._day_in_quarter

    @property
    def week_in_quarter(self) -> SezimalInteger:
        return self._week_in_quarter

    @property
    def month_in_quarter(self) -> SezimalInteger:
        return self._month_in_quarter

    @property
    def weekday_name(self) -> str:
        return DEFAULT_LOCALE.weekday_name(self.weekday)

    @property
    def weekday_abbreviated_name(self) -> str:
        return DEFAULT_LOCALE.weekday_abbreviated_name(self.weekday)

    @property
    def month_name(self) -> str:
        return DEFAULT_LOCALE.month_name(self.month)

    @property
    def month_abbreviated_name(self) -> str:
        return DEFAULT_LOCALE.month_abbreviated_name(self.month)

    @property
    def era_name(self) -> str:
        return DEFAULT_LOCALE.era_name(self.year)

    @property
    def day_ordinal_suffix(self) -> str:
        return DEFAULT_LOCALE.day_ordinal_suffix(self.day)

    def _apply_number_format(self, token: str, value_name: str, size: int | SezimalInteger = None, locale: SezimalLocale = None, from_decimal: bool = False) -> str:
        value = getattr(self, value_name, 0)

        if value_name.startswith('gregorian_') or value_name.startswith('symmetric_'):
            if type(value) == Decimal:
                value = SezimalInteger(value)
            else:
                value = SezimalInteger(Decimal(value))

        if from_decimal:
            value = Decimal(str(value))

        if '*' in token and (not value):
            return ''

        if '@' in token or 'Z' in token:
            if from_decimal:
                value = SezimalInteger(value)

            value = str(value)

            value = sezimal_to_niftimal(value)

            #
            # For the year, using “>”
            # yields only the last 2 digits
            #
            if token.endswith('>y'):
                value = value[::-1][0:2][::-1]

            if size and '-' not in token:
                value = value.zfill(int(SezimalInteger(size)))

            if '!' in token:
                value = default_niftimal_to_regularized_dedicated_digits(value)
            elif '@' in token:
                value = default_niftimal_to_regularized_digits(value)

        else:
            if '5' in token:
                value = str(SezimalInteger(value))

                #
                # For the year, using “>”
                # yields only the last 3 digits
                #
                if token.endswith('>y'):
                    value = value[::-1][0:3][::-1]

            elif '↋' in token:
                value = str(DozenalInteger(value))

                #
                # For the year, using “>”
                # yields only the last 2 digits
                #
                if token.endswith('>y'):
                    value = value[::-1][0:2][::-1]

            elif '9' in token or from_decimal:
                if from_decimal:
                    value = str(int(value))
                else:
                    value = str(int(value.decimal))

                #
                # For the year, using “>”
                # yields only the last 2 digits
                #
                if token.endswith('>y'):
                    value = value[::-1][0:2][::-1]

            else:
                value = str(value)

                #
                # For the year, using “>”
                # yields only the last 3 digits
                #
                if token.endswith('>y'):
                    value = value[::-1][0:3][::-1]

            if size and '-' not in token and '>' not in token:
                value = value.zfill(int(SezimalInteger(size)))

            if '!' in token:
                value = default_to_dedicated_digits(value)

            elif '?' in token:
                value = locale.digit_replace(value)

        return value

    def format(self, fmt: str = None, locale: str | SezimalLocale = None, skip_strftime: bool = False, time_zone: str | ZoneInfo = None) -> str:
        if locale:
            if isinstance(locale, SezimalLocale):
                lang = locale.LANG
            else:
                lang = locale
                locale = sezimal_locale(lang)

        else:
            locale = DEFAULT_LOCALE
            lang = locale.LANG

        if not fmt:
            fmt = locale.DATE_FORMAT

        fmt = fmt.replace('##', '__HASHTAG__')

        #
        # Astronomical formats: seasons and moon phases
        #
        fmt = self._apply_season_format(fmt, locale=locale, time_zone=time_zone)

        #
        # Let’s deal first with the numeric formats
        #
        for regex, token, base, zero, character, value_name, \
            size, size_niftimal, size_decimal in DATE_NUMBER_FORMAT_TOKENS:
            if not regex.findall(fmt):
                continue

            if base in ['@', '@!', 'Z']:
                value = self._apply_number_format(token, value_name, size_niftimal, locale)
            elif base in ['9', '9?', '↋', '↋?']:
                value = self._apply_number_format(token, value_name, size_decimal, locale)
            else:
                value = self._apply_number_format(token, value_name, size, locale)

            fmt = regex.sub(value, fmt)

        #
        # Formatted year number
        #
        for regex, token, base, separator, character, value_name in YEAR_NUMBER_FORMAT_TOKENS:
            if not regex.findall(fmt):
                continue

            year = getattr(self, value_name, 0)

            if value_name.startswith('gregorian_') or value_name.startswith('symmetric_'):
                if type(year) == Decimal:
                    year = SezimalInteger(year)
                else:
                    year = SezimalInteger(Decimal(year))

            if base in ['', '!', '?']:
                year = locale.format_number(
                    year,
                    dedicated_digits='!' in base,
                    use_group_separator=True,
                    sezimal_places=0,
                )

            elif base in ['@', '@!', 'Z', 'Z?']:
                year = locale.format_niftimal_number(
                    year,
                    dedicated_digits='!' in base,
                    regularized_digits='@' in base,
                    use_group_separator=True,
                    niftimal_places=0,
                )

            elif base in ['9', '9?']:
                year = locale.format_decimal_number(
                    year,
                    use_group_separator=True,
                    decimal_places=0,
                )

            elif base in ['↋', '↋?']:
                year = locale.format_dozenal_number(
                    year,
                    use_group_separator=True,
                    dozenal_places=0,
                )

            if '?' in base:
                year = locale.digit_replace(year)

            if separator:
                if separator[0] == '\\' and len(separator) >= 2:
                    separator = separator[1:]

                if separator != locale.GROUP_SEPARATOR:
                    year = year.replace(locale.GROUP_SEPARATOR, separator)

            fmt = regex.sub(year, fmt)

        #
        # And now, the text formats
        #
        for regex, token, base, case, month_week in DATE_TEXT_FORMAT_TOKENS:
            if not regex.findall(fmt):
                continue

            if month_week == 'M':
                if base == '@':
                    text = locale.month_abbreviated_name(self.month)
                else:
                    text = locale.month_name(self.month)

            else:
                if base == '@':
                    text = locale.weekday_abbreviated_name(self.weekday)
                else:
                    text = locale.weekday_name(self.weekday)

            if base == '1':
                text = text[0]
            elif base == '2':
                if len(text) > 2:
                    text = text[0:2]
            elif base == '3':
                if len(text) > 3:
                    text = text[0:3]

            if case == '!':
                text = text.upper()
            elif case == '?':
                text = text.lower()
            elif case == '>':
                text = text[0].upper() + text[1:].lower()

            fmt = regex.sub(text, fmt)

        if '#O' in fmt:
            fmt = fmt.replace('#O', locale.day_ordinal_suffix(self.day))

        if '#E' in fmt:
            fmt = fmt.replace('#E', locale.era_name(self.year))

        fmt = locale.apply_date_format(self, fmt)

        fmt = fmt.replace('__HASHTAG__', '#')

        #
        # Some very basic formatting for Gregorian years below
        # Python’s minimum year number
        #
        if '%' in fmt:
            fmt = fmt.replace('%%', '__PERCENT__')

            for regex, token, base, zero, character, value_name, \
                size_decimal, size_niftimal, size_sezimal in ISO_DATE_NUMBER_FORMAT_TOKENS:
                if not regex.findall(fmt):
                    continue

                if token.endswith('y'):
                    token = token[0:-1] + '>y'
                    size_sezimal -= 2
                    size_niftimal -= 1
                    size_decimal -= 2

                if base in ['@', '@!', 'Z']:
                    value = self._apply_number_format(token, value_name, size_niftimal, locale, from_decimal=True)
                elif base in ['5', '5!', '5?']:
                    value = self._apply_number_format(token, value_name, size_sezimal, locale, from_decimal=True)
                elif base in ['↋', '↋?']:
                    value = self._apply_number_format(token, value_name, size_decimal, locale, from_decimal=True)
                else:
                    value = self._apply_number_format(token, value_name, size_decimal, locale, from_decimal=True)

                fmt = regex.sub(value, fmt)

            if '%A' in fmt:
                fmt = fmt.replace('%A', locale.weekday_name(self.weekday))

            if '%a' in fmt:
                fmt = fmt.replace('%a', locale.weekday_abbreviated_name(self.weekday))

            if '%o' in fmt:
                fmt = fmt.replace('%o', locale.day_ordinal_suffix(Decimal(self.gregorian_day)))

            if '%B' in fmt:
                fmt = fmt.replace('%B', locale.month_name(Decimal(self.gregorian_month)))

            if '%b' in fmt:
                fmt = fmt.replace('%b', locale.month_abbreviated_name(Decimal(self.gregorian_month)))

            if not skip_strftime:
                if type(self.gregorian_date) == _datetime.date:
                    fmt = fmt.replace('__PERCENT__', '%%')
                    fmt = self.gregorian_date.strftime(fmt)

            fmt = fmt.replace('__PERCENT__', '%')

        return fmt

    @property
    def gregorian_year(self) -> int:
        if type(self._gregorian_date) in (list, tuple):
            return self._gregorian_date[0]

        return self.gregorian_date.year

    @property
    def gregorian_month(self) -> int:
        if type(self._gregorian_date) in (list, tuple):
            return self._gregorian_date[1]

        return self.gregorian_date.month

    @property
    def gregorian_day(self) -> int:
        if type(self._gregorian_date) in (list, tuple):
            return self._gregorian_date[2]

        return self.gregorian_date.day

    @property
    def gregorian_isoformat(self) -> str:
        if self.gregorian_year > 9_999:
            return f'+{str(self.gregorian_year).zfill(4)}-{str(self.gregorian_month).zfill(2)}-{str(self.gregorian_day).zfill(2)}'
        else:
            return f'{str(self.gregorian_year).zfill(4)}-{str(self.gregorian_month).zfill(2)}-{str(self.gregorian_day).zfill(2)}'

    @property
    def gregorian_holocene_date(self):
        return (self.gregorian_holocene_year, self.gregorian_holocene_month, self.gregorian_holocene_day)

    @property
    def gregorian_holocene_year(self) -> int:
        return self.gregorian_year + int(ISO_HOLOCENE_YEAR_DIFF)

    @property
    def gregorian_holocene_month(self) -> int:
        return self.gregorian_month

    @property
    def gregorian_holocene_day(self) -> int:
        return self.gregorian_day

    @property
    def gregorian_holocene_isoformat(self) -> str:
        return f'{str(self.gregorian_holocene_year).zfill(5)}-{str(self.gregorian_holocene_month).zfill(2)}-{str(self.gregorian_holocene_day).zfill(2)}'

    @property
    def gregorian_is_leap(self):
        year = self.gregorian_year
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @property
    def symmetric_date(self):
        return (self.symmetric_year, self.symmetric_month, self.symmetric_day)

    @property
    def symmetric_year(self) -> int:
        return int(self.year) - int(ISO_YEAR_DIFF)

    @property
    def symmetric_month(self) -> int:
        return int(self.month)

    @property
    def symmetric_day(self) -> int:
        return int(self.day)

    @property
    def symmetric_isoformat(self) -> str:
        return f'{str(self.symmetric_year).zfill(4)}-{str(self.symmetric_month).zfill(2)}-{str(self.symmetric_day).zfill(2)}'

    @property
    def symmetric_holocene_date(self):
        return (self.symmetric_holocene_year, self.symmetric_holocene_month, self.symmetric_holocene_day)

    @property
    def symmetric_holocene_year(self) -> int:
        return self.symmetric_year + int(ISO_HOLOCENE_YEAR_DIFF)

    @property
    def symmetric_holocene_month(self) -> int:
        return int(self.month)

    @property
    def symmetric_holocene_day(self) -> int:
        return int(self.day)

    @property
    def symmetric_holocene_isoformat(self) -> str:
        return f'{str(self.symmetric_holocene_year).zfill(5)}-{str(self.symmetric_holocene_month).zfill(2)}-{str(self.symmetric_holocene_day).zfill(2)}'

    def timetuple(self):
        return self.gregorian_date.timetuple()

    def toordinal(self) -> SezimalInteger:
        return self._ordinal_date

    @property
    def ordinal_date(self) -> SezimalInteger:
        return self._ordinal_date

    @property
    def isocalendar(self):
        return self.gregorian_date.isocalendar()

    @property
    def julian_date(self) -> Sezimal:
        return self.ordinal_date + ISO_EPOCH_JULIAN_DATE

    @property
    def mars_sol_date(self) -> Sezimal:
        return mars_sol_date(self.julian_date)

    def replace(self,
        year: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        month: str | int | float | Decimal | Sezimal | SezimalInteger = None,
        day: str | int | float | Decimal | Sezimal | SezimalInteger = None,
    ) -> Self:
        if year is None:
            year = self._year

        if month is None:
            month = self._month

        if day is None:
            day = self._day
        else:
            day = SezimalInteger(day)

        if day > 44:
            if (month not in (2, 5, 12, 15)) \
                or (month == 20 and not _is_leap(year)):
                day -= 11

        return type(self)(year, month, day)

    # Comparisons of date objects with other.

    def __eq__(self, other: str | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self) -> bool:
        return self._cmp(other) == 0

    def __le__(self, other: str | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self) -> bool:
        return self._cmp(other) <= 0

    def __lt__(self, other: str | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self) -> bool:
        return self._cmp(other) < 0

    def __ge__(self, other: str | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self) -> bool:
        return self._cmp(other) >= 0

    def __gt__(self, other: str | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self) -> bool:
        return self._cmp(other) > 0

    def _cmp(self, other: str | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self) -> bool:
        if type(other) != SezimalDate:
            other = SezimalDate(other)

        this_ordinal = self.toordinal()
        other_ordinal = other.toordinal()

        if this_ordinal == other_ordinal:
            return 0
        elif this_ordinal > other_ordinal:
            return 1
        else:
            return -1

    def __hash__(self):
        if self._hashcode == -1:
            self._hashcode = hash(self._getstate())

        return self._hashcode

    def __add__(self, other: SezimalDateTimeDelta):
        if type(other) != SezimalDateTimeDelta:
            raise ValueError('You can only add a SezimalDate to a SezimalDateTimeDelta')

        return SezimalDate.from_ordinal_date(other._total_days + self.ordinal_date)

    __radd__ = __add__

    def __sub__(self, other: str | _datetime.date | _datetime.datetime | SezimalDateTime | SezimalTime | Self | SezimalDateTimeDelta):
        """Subtract two dates, or a date and a timedelta."""
        if isinstance(other, timedelta):
            return self + timedelta(-other.days)
        if isinstance(other, _datetime.date) or isinstance(other, SezimalDate):
            days1 = self.toordinal()
            days2 = other.toordinal()
            return timedelta(days1 - days2)
        return NotImplemented


    # Pickle support.

    def _getstate(self):
        return self.gregorian_date._getstate()

    def __setstate(self, string):
        yhi, ylo, self._month, self._day = string
        self._year = yhi * SezimalInteger('1_104') + ylo

    def __reduce__(self):
        return (self.__class__, self._getstate())

    @property
    def as_agrimas(self) -> SezimalInteger:
        return self.ordinal_date * 1_000_000

    @property
    def as_seconds(self) -> Decimal:
        seconds = self.as_agrimas * AGRIMA_TO_SECOND
        return seconds.decimal

    @property
    def as_days(self) -> SezimalInteger:
        return self.ordinal_date

    @classmethod
    def from_days(cls, days: SezimalInteger) -> Self:
        return cls.from_ordinal_date(SezimalInteger(days))

    def _moon_phase_name_simplified(self) -> str:
        #
        # Mean moon month = days ÷ years
        # According to Wikipedia, this gives a mean lunar month
        # 1 day behind the actual moon phase
        #
        MOON_MONTH = Sezimal('312_113') / Sezimal('3_534')

        #
        # Date and time at the end of the day
        # minus 1 day, compensating the moon cycle
        #
        moon_phase = self.ordinal_date - 1
        moon_phase += Sezimal('0.555_555')

        #
        # Specific point in time where the moon was knowingly
        # on the new phase:
        #
        # Ordinal date 23_014_020.04
        # Sezimal date 131_111-01-25 04:00
        # Gregorian date 1923-01-17 02:40
        #
        # It was first new moon of the first lunation (lunar month),
        # according to this site: https://www.timeanddate.com/moon/phases/?year=1923
        #
        moon_phase -= Sezimal('23_014_020.04')

        day_in_cycle = moon_phase.decimal % MOON_MONTH.decimal

        if day_in_cycle < 0:
            day_in_cycle = MOON_MONTH.decimal + day_in_cycle

        persixniff = Sezimal(day_in_cycle / MOON_MONTH.decimal * 216)

        if persixniff > 1_000:
            persixniff -= 1_000

        if persixniff < 20:
            phase = 'new'

        elif persixniff < 130:
            phase = 'waxing_crescent'

        elif persixniff < 140:
            phase = 'first_quarter'

        elif persixniff < 300:
            phase = 'waxing_gibbous'

        elif persixniff < 320:
            phase = 'full'

        elif persixniff < 430:
            phase = 'waning_gibbous'

        elif persixniff < 440:
            phase = 'third_quarter'

        else:
            phase = 'waning_crescent'

        return phase


SezimalDate.min = SezimalDate(1, 1, 1)
SezimalDate.max = SezimalDate(MAXYEAR, 20, 44)
SezimalDate.resolution = _datetime.timedelta(days=1)


if __name__ == '__main__':
    try:
        1/0
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
        documentation_title = '     Datas da Documentação do Calendário'
        holidays_title = '   Feriados e Eventos Históricos do Brasil'
        size = 16
        date_format = '%a. %d-%b-%_Y'

    except:
        documentation_title = '  Dates from the Symmetry454 Documentation'
        holidays_title = '   Brazilian Holidays and Historical Events'
        size = 16
        date_format = '%_Y-%m-%d %a.'

    print(documentation_title)
    print(holidays_title)
    print(' ===========================================')

    dates = [
        # (( -753,  1,  1), 'Kalendae Ianuarius I AUC => -0753-12-23 CE, -0753-12-24 Gregorian/ISO (no year zero)'),
        # (( -121,  4, 27), '=> -0121-04-27 CE, -0121-04-26 Gregorian/ISO (no year zero)'),
        # ((  -91,  9, 22), '=> -0091-09-22 CE, -0091-09-27 Gregorian/ISO (no year zero)'),
        ((    1,  1,  1), 'First date possible, Python’s date doesn’t deal with years before 1'),
        ((  122,  9,  7), 'Building of Hadrian’s Wall (circa)'),
        ((1_776,  7,  4), 'Independence Day - USA'),
        ((1_867,  7,  1), 'Canadian Confederence - Canada'),
        ((1_947, 10, 24), ''),
        ((1_970,  1,  1), 'POSIX epoch'),
        ((1_995,  8, 10), ''),
        ((2_000,  2, 29), ''),
        ((2_004,  5,  2), ''),
        ((2_004, 12, 31), 'Dr. Irv Bromberg proposed switching calendars on 2005-01-01'),
        ((2_020,  2, 20), ''),
        ((2_023,  1, 16), 'Day I commited this code to GitHub'),
        ((2_222,  2,  6), ''),
        ((3_333,  3,  1), ''),
        ((9_998, 12, 27), 'Last date compatible with Python’s date, see code'),

        ((1500,  5,  2), 'Descobrimento do Brasil (22-abr-1500 cal. juliano)'),
        ((1532,  2,  1), 'Fundação de São Vicente (22-jan-1532 cal. juliano)'),
        ((1554,  2,  4), 'Fundação de São Paulo (25-jan-1554 cal. juliano)'),
        ((1792,  4, 21), 'Tiradentes'),
        ((1822,  9,  7), 'Independência'),
        ((1857,  5,  8), 'Dia da Mulher'),
        ((1886,  5,  1), 'Dia do Trabalhador'),
        ((1888,  5, 13), 'Libertação da Escravatura'),
        ((1889, 11, 15), 'Proclamação da República'),
        ((1932,  7,  9), 'Revolução Constitucionalista'),
        ((1968,  1,  1), 'Fraternidade Universal'),
        ((1980, 10, 12), 'Nossa Senhora Aparecida'),
    ]

    for ymd, name in dates:
        dt = _datetime.date(*ymd)
        sd = SezimalDate(dt)
        # print(dt, dt.toordinal(), sd, sd.isoformat_decimal(), sd.toordinal().decimal, Decimal(dt.toordinal()) == sd.toordinal().decimal)
        print(sd.isoformat_decimal(), decimal_format(sd.toordinal().decimal, decimal_places=0), decimal_format(sd.to_julian_date().decimal))
        # print(' ', sd.gregorian_date.strftime(date_format).rjust(size), f'Greg. =', sd.strftime(date_format + ' %E').rjust(size), f'({sd.isoformat_decimal()})', name)

    # sd = SezimalDate.today()
    # dt = sd.gregorian_date
    # print()
    # print(' ', sd.gregorian_date.strftime(date_format).rjust(size), f'Greg. =', sd.strftime(date_format + ' %E').rjust(size), f'({sd.isoformat_decimal()})', 'Today')
