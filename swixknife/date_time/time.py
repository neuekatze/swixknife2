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

import time as _time
import datetime as _datetime
from pytz import timezone, UTC

from decimal import Decimal

from ..sezimal import Sezimal, SezimalInteger
from ..units.conversions import AGRIMA_TO_SECOND, SECOND_TO_AGRIMA
from ..base import sezimal_format

TIME_SEPARATOR = "'"


def _system_time_zone():
    diff = int(_time.strftime('%z')) // 100

    if diff == 0:
        return 'UTC'

    if diff > 0:
        return 'Etc/GMT-' + str(diff)

    return 'Etc/GMT+' + str(diff * -1)


def _date_time_to_agrima(date_time: _datetime.datetime):
    total_seconds = Decimal(str(date_time.hour * 60 * 60))
    total_seconds += Decimal(str(date_time.minute * 60))
    total_seconds += Decimal(str(date_time.second))
    total_seconds += Decimal(str(date_time.microsecond / 1_000_000))
    total_agrimas = total_seconds * SECOND_TO_AGRIMA
    return total_agrimas


def _tz_agrimas_offset(time_zone: str = 'UTC', base_date: str = None):
    if not time_zone:
        time_zone = _system_time_zone()

    elif time_zone == 'UTC':
        return Sezimal('0'), Sezimal('0')

    time_zone = timezone(time_zone)

    if base_date:
        dt_tz = _datetime.datetime.fromisoformat(f'{base_date}T12:00:00')
        dt_tz = time_zone.localize(dt_tz)
    else:
        dt_tz = _datetime.datetime.now(time_zone)

    td = dt_tz.utcoffset()
    total_seconds = Decimal(str(td.days * 86_400))
    total_seconds += Decimal(str(td.seconds))

    total_agrimas = total_seconds * SECOND_TO_AGRIMA

    td_dst = dt_tz.dst()
    total_seconds_dst = Decimal(str(td_dst.days * 86_400))
    total_seconds_dst += Decimal(str(td_dst.seconds))

    total_agrimas_dst = total_seconds_dst * SECOND_TO_AGRIMA

    return total_agrimas, total_agrimas_dst


class SezimalTime():
    __slots__ = '_uta', '_posha', '_agrima', '_anuga', '_boda', '_ekaditiboda', '_day', '_time_zone', '_total_agrimas', '_iso_time', '_time_zone_offset', '_dst_offset'

    def __new__(cls,
                uta: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
                posha: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
                agrima: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
                anuga: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
                boda: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
                ekaditiboda: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
                day: str | int | float | Decimal | Sezimal | SezimalInteger = 0,
                time_zone: str = None,
                ):
        day = Sezimal(day)
        uta = Sezimal(uta)
        posha = Sezimal(posha)
        agrima = Sezimal(agrima)
        anuga = Sezimal(anuga)
        boda = Sezimal(boda)
        ekaditiboda = Sezimal(ekaditiboda)

        total_agrimas = day * 100_0000
        total_agrimas += uta * 1_0000
        total_agrimas += posha * 100
        total_agrimas += agrima
        total_agrimas += anuga / 100
        total_agrimas += boda / 1_0000
        total_agrimas += (ekaditiboda / 1_0000_0000) / 1_0000

        self = object.__new__(cls)

        self._total_agrimas = total_agrimas

        self._day = SezimalInteger(total_agrimas // 100_0000)
        total_agrimas -= self._day * 100_0000

        self._uta = SezimalInteger(total_agrimas // 1_0000)
        total_agrimas -= self._uta * 1_0000

        self._posha = SezimalInteger(total_agrimas // 100)
        total_agrimas -= self._posha * 100

        self._agrima = SezimalInteger(total_agrimas)
        total_agrimas -= SezimalInteger(total_agrimas)

        total_agrimas *= 100
        self._anuga = SezimalInteger(total_agrimas)
        total_agrimas -= self._anuga

        total_agrimas *= 100
        self._boda = SezimalInteger(total_agrimas)
        total_agrimas -= self._boda

        total_agrimas *= 1_0000_0000
        self._ekaditiboda = SezimalInteger(total_agrimas)

        if not time_zone:
            time_zone = _system_time_zone()

        self._time_zone = time_zone
        self._time_zone_offset, self._dst_offset = _tz_agrimas_offset(time_zone)

        total_seconds = self._total_agrimas
        total_seconds = total_seconds.decimal * AGRIMA_TO_SECOND.decimal

        hour = int(total_seconds // 60 // 60)
        total_seconds -= hour * 60 * 60

        minute = int(total_seconds // 60)
        total_seconds -= minute * 60

        second = int(total_seconds)
        total_seconds -= second

        microssecond = int(total_seconds * 1_000_000)

        iso_time = _datetime.time(hour, minute, second, microssecond, tzinfo=timezone(time_zone))

        self._iso_time = iso_time

        return self

    @property
    def day(self):
        return self._day

    @property
    def uta(self):
        return self._uta

    @property
    def posha(self):
        return self._posha

    @property
    def agrima(self):
        return self._agrima

    @property
    def anuga(self):
        return self._anuga

    @property
    def boda(self):
        return self._boda

    @property
    def ekaditiboda(self):
        return self._ekaditiboda

    @property
    def time_zone(self):
        return self._time_zone

    @property
    def is_dst(self):
        return self._dst_offset != 0

    @property
    def iso_time(self):
        return self._iso_time

    @property
    def as_agrimas(self):
        return self._total_agrimas

    @property
    def as_seconds(self):
        return self.as_agrimas * AGRIMA_TO_SECOND

    def __repr__(self):
        return f"SezimalTime(uta={self.uta}, posha={self.posha}, agrima={self.agrima}, anuga={self.anuga}, boda={self.boda}, ekaditiboda={self.ekaditiboda}, day={self.day}, time_zone={self.time_zone}) - {self.iso_time.__repr__()}"

    def __str__(self):
        res = self.format(f'#*d #u{TIME_SEPARATOR}#p{TIME_SEPARATOR}#a.#n#b#e #t #V')
        return res.strip()

    @classmethod
    def now(cls, time_zone: str = None):
        if not time_zone:
            time_zone = _system_time_zone()

        traditional_utc_now = _datetime.datetime.now(UTC)
        total_agrimas = _date_time_to_agrima(traditional_utc_now)
        tz_offset, dst_offset = _tz_agrimas_offset(time_zone)
        total_agrimas += tz_offset # + dst_offset
        return cls(agrima=total_agrimas, time_zone=time_zone)

    def to_time_zone(self, time_zone: str = 'UTC'):
        if not time_zone:
            time_zone = 'UTC'

        utc_agrimas = self.as_agrimas - self._time_zone_offset # - self._dst_offset
        tz_offset, dst_offset = _tz_agrimas_offset(time_zone)
        tz_agrimas = utc_agrimas + tz_offset # + dst_offset

        return SezimalTime(agrima=tz_agrimas, time_zone=time_zone)

    def _apply_format(self, fmt, token, value, size=None):
        if token in fmt:
            if '*' in token and (not value):
                fmt = fmt.replace(token, '')
            else:
                if size:
                    fmt = fmt.replace(token, str(value).zfill(size))
                else:
                    fmt = fmt.replace(token, str(value))

        return fmt

    def format(self, fmt: str = f'#u{TIME_SEPARATOR}#p{TIME_SEPARATOR}#a'):
        fmt = fmt.replace('##', '__HASHTAG__')

        fmt = self._apply_format(fmt, '#*d', self.day)
        fmt = self._apply_format(fmt, '#d', self.day)

        fmt = self._apply_format(fmt, '#*-u', self.uta)
        fmt = self._apply_format(fmt, '#*u', self.uta, 2)
        fmt = self._apply_format(fmt, '#-u', self.uta)
        fmt = self._apply_format(fmt, '#u', self.uta, 2)

        fmt = self._apply_format(fmt, '#*-p', self.posha)
        fmt = self._apply_format(fmt, '#*p', self.posha, 2)
        fmt = self._apply_format(fmt, '#-p', self.posha)
        fmt = self._apply_format(fmt, '#p', self.posha, 2)

        fmt = self._apply_format(fmt, '#*-a', self.agrima)
        fmt = self._apply_format(fmt, '#*a', self.agrima, 2)
        fmt = self._apply_format(fmt, '#-a', self.agrima)
        fmt = self._apply_format(fmt, '#a', self.agrima, 2)

        fmt = self._apply_format(fmt, '#*-n', self.anuga)
        fmt = self._apply_format(fmt, '#*n', self.anuga, 2)
        fmt = self._apply_format(fmt, '#-n', self.anuga)
        fmt = self._apply_format(fmt, '#n', self.anuga, 2)

        fmt = self._apply_format(fmt, '#*-b', self.boda)
        fmt = self._apply_format(fmt, '#*b', self.boda, 2)
        fmt = self._apply_format(fmt, '#-b', self.boda)
        fmt = self._apply_format(fmt, '#b', self.boda, 2)

        fmt = self._apply_format(fmt, '#*-e', self.ekaditiboda)
        fmt = self._apply_format(fmt, '#*e', self.ekaditiboda, 8)
        fmt = self._apply_format(fmt, '#-e', self.ekaditiboda)
        fmt = self._apply_format(fmt, '#e', self.ekaditiboda, 8)

        if '#t' in fmt:
            if self._time_zone_offset == 0:
                fmt = fmt.replace('#t', f'+00{TIME_SEPARATOR}00')
            else:
                if self._time_zone_offset > 0:
                    text = '+'
                else:
                    text = '−'

                text += sezimal_format(
                    abs(self._time_zone_offset / 100),
                    sezimal_places=0,
                    minimum_size=4,
                    group_separator=TIME_SEPARATOR,
                    subgroup_separator=TIME_SEPARATOR,
                )

                fmt = fmt.replace('#t', text)

        if '#T' in fmt:
            fmt = fmt.replace('#T', self.time_zone)

        if '#z' in fmt:
            if self._time_zone_offset == 0:
                fmt = fmt.replace('#z', '+0000')
            else:
                if self._time_zone_offset > 0:
                    text = '+'
                else:
                    text = '−'

                text += str(SezimalInteger(abs(self._time_zone_offset / 100))).zfill(4)

                fmt = fmt.replace('#z', text)

        if '#v' in fmt:
            fmt = fmt.replace('#v', str(self.is_dst))

        if '#V' in fmt:
            fmt = fmt.replace('#V', 'DST' if self.is_dst else '')

        fmt = fmt.replace('__HASHTAG__', '#')

        return self.iso_time.strftime(fmt)

    def strftime(self, fmt):
        return self.format(fmt)
