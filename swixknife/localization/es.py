

__all__ = ('SezimalLocaleES',)


from typing import TypeVar

SezimalDate = TypeVar('SezimalDate', bound='SezimalDate')


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleES(SezimalLocale):
    LANG = 'es'
    LANGUAGE = 'español'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'lunes',
        'martes',
        'miércoles',
        'jueves',
        'viernes',
        'sábado',
        'domingo',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'lun',
        'mar',
        'mié',
        'jue',
        'vie',
        'sáb',
        'dom',
    ]

    MONTH_NAME= [
        'enero',
        'febrero',
        'marzo',
        'abril',
        'mayo',
        'junio',
        'julio',
        'agosto',
        'septiembre',
        'octubre',
        'noviembre',
        'diciembre',
    ]

    MONTH_ABBREVIATED_NAME = [
        'ene',
        'feb',
        'mar',
        'abr',
        'may',
        'jun',
        'jul',
        'ago',
        'sep',
        'oct',
        'nov',
        'dic',
    ]

    ERA_NAME = [
        #
        # Era Humana Sezimal
        #
        'EHS',
        #
        # Antes de la Era Humana Sezimal
        #
        'aEHS',
    ]

    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#-d#O de #M de #Y'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#@W, #d/#m/#Y, #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#W, #-d#O de #M de #Y, #u:#p:#a'
    DST_NAME = 'Horário de Invierno'
    DST_SHORT_NAME = 'HI'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern

    SEASON_NAME = {
        'spring_cross_quarter': 'Transición Invierno – Primavera',
        'spring_equinox': 'Primavera',
        'summer_cross_quarter': 'Transición Primavera – Verano',
        'summer_solstice': 'Verano',
        'autumn_cross_quarter': 'Transición Verano – Otoño',
        'autumn_equinox': 'Otoño',
        'winter_cross_quarter': 'Transición Otoño – Invierno',
        'winter_solstice': 'Invierno',
    }

    MOON_PHASE = {
        'new': 'Nueva',
        'waxing crescent': 'Creciente',
        'first quarter': 'Cuarto Creciente',
        'waxing gibbous': 'Cuarto Creciente para Llena',
        'full': 'Llena',
        'waning gibbous': 'Minguante',
        'third quarter': 'Cuarto Minguante',
        'waning crescent': 'Cuarto Minguante para Nueva',
    }

    def day_ordinal_suffix(self, day: SezimalInteger, case: str = None) -> str:
        day = SezimalInteger(day)

        if day == 1:
            return 'º'

        return ''
