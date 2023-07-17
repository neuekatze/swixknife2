

__all__ = ('SezimalLocaleVI',)


from .lokale import SezimalLocale
from ..sezimal import SezimalInteger
from ..base import SEPARATOR_COMMA, SEPARATOR_DOT, SEPARATOR_NARROW_NOBREAK_SPACE


class SezimalLocaleVI(SezimalLocale):
    LANG = 'vi'
    LANGUAGE = 'Tiếng Việt'

    SEZIMAL_SEPARATOR = SEPARATOR_COMMA

    GROUP_SEPARATOR = SEPARATOR_DOT
    SUBGROUP_SEPARATOR = ''

    FRACTION_GROUP_SEPARATOR = SEPARATOR_NARROW_NOBREAK_SPACE
    FRACTION_SUBGROUP_SEPARATOR = ''

    WEEKDAY_NAME = [
        'thứ hai',
        'thứ ba',
        'thứ tư',
        'thứ năm',
        'thứ sáu',
        'thứ bảy',
        'chủ nhật',
    ]

    WEEKDAY_ABBREVIATED_NAME = [
        'Th2',
        'Th3',
        'Th4',
        'Th5',
        'Th6',
        'Th7',
        'CN',
    ]

    MONTH_NAME= [
        'tháng giêng',
        'tháng hai',
        'tháng ba',
        'tháng tư',
        'tháng năm',
        'tháng sáu',
        'tháng bảy',
        'tháng tám',
        'tháng chín',
        'tháng mười',
        'tháng mười một',
        'tháng chạp',
    ]

    MONTH_ABBREVIATED_NAME = [
        'thg 1',
        'thg 2',
        'thg 3',
        'thg 4',
        'thg 5',
        # 'thg 6',
        # 'thg 7',
        # 'thg 8',
        # 'thg 9',
        # 'thg 10',
        # 'thg 11',
        # 'thg 12',
        'thg 10',
        'thg 11',
        'thg 12',
        'thg 13',
        'thg 14',
        'thg 15',
        'thg 20',
    ]

    DATE_FORMAT = '#d/#m/#Y'
    DATE_LONG_FORMAT = '#d/#m/#Y #@W'
    TIME_FORMAT = '#u:#p:#a'
    DATE_TIME_FORMAT = '#d/#m/#Y #u:#p:#a'
    DATE_TIME_LONG_FORMAT = '#d/#m/#Y #@W #u:#p:#a'
    DST_NAME = 'Daylight Saving Time'
    DST_SHORT_NAME = 'DST'

    DEFAULT_HEMISPHERE = 'N'  # Use 'S' for Southern or 'N' for Northern
    DEFAULT_TIME_ZONE = 'Asia/Ho_Chi_Minh'

    SEASON_NAME = {
        'spring_cross_quarter': 'Spring Cross-Quarter',
        'spring_equinox': 'Spring',
        'summer_cross_quarter': 'Summer Cross-Quarter',
        'summer_solstice': 'Summer',
        'autumn_cross_quarter': 'Autumn Cross-Quarter',
        'autumn_equinox': 'Autumn',
        'winter_cross_quarter': 'Winter Cross-Quarter',
        'winter_solstice': 'Winter',
    }

    MOON_PHASE = {
        'new': 'New',
        'waxing_crescent': 'Waxing Crescent',
        'first_quarter': 'First Quarter',
        'waxing_gibbous': 'Waxing Gibbous',
        'full': 'Full',
        'waning_gibbous': 'Waning Gibbous',
        'third_quarter': 'Third Quarter',
        'waning_crescent': 'Waning Crescent',
    }

    HOLIDAYS = []
    HOLIDAYS_OTHER_CALENDAR = []

    WEEKDAY_ERROR = 'Invalid weekday {weekday}'
    MONTH_ERROR = 'Invalid month {month}'

