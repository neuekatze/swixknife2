
__all__ = (
    'Sezimal',
    'SezimalInteger',
    'SezimalFraction',
)


from decimal import Decimal, localcontext, getcontext

from typing import TypeVar
import numbers as _numbers

Self = TypeVar('Self', bound='Sezimal')
IntegerSelf = TypeVar('IntegerSelf', bound='SezimalInteger')
FractionSelf = TypeVar('FractionSelf', bound='SezimalFraction')

Dozenal = TypeVar('Dozenal', bound='Dozenal')
DozenalInteger = TypeVar('DozenalInteger', bound='DozenalInteger')
DozenalFraction = TypeVar('DozenalFraction', bound='DozenalFraction')

from .base import validate_clean_sezimal, \
    decimal_to_sezimal, sezimal_to_decimal, \
    sezimal_format, decimal_format, \
    sezimal_to_dozenal, dozenal_format, \
    sezimal_to_niftimal, niftimal_format, \
    dozenal_to_sezimal, \
    MAX_DECIMAL_PRECISION, MAX_SEZIMAL_PRECISION


getcontext().prec = MAX_DECIMAL_PRECISION
MAX_PRECISION = MAX_SEZIMAL_PRECISION

#
# Operations maps/tables
#
_ADDITION_MAP = {
    '0': {'0': '0', '1':  '1', '2':  '2', '3':  '3', '4':  '4', '5':  '5', '10': '10', '11': '11', '12': '12', '13': '13', '14': '14'},
    '1': {'0': '1', '1':  '2', '2':  '3', '3':  '4', '4':  '5', '5': '10', '10': '11', '11': '12', '12': '13', '13': '14', '14': '15'},
    '2': {'0': '2', '1':  '3', '2':  '4', '3':  '5', '4': '10', '5': '11', '10': '12', '11': '13', '12': '14', '13': '15', '14': '20'},
    '3': {'0': '3', '1':  '4', '2':  '5', '3': '10', '4': '11', '5': '12', '10': '13', '11': '14', '12': '15', '13': '20', '14': '21'},
    '4': {'0': '4', '1':  '5', '2': '10', '3': '11', '4': '12', '5': '13', '10': '14', '11': '15', '12': '20', '13': '21', '14': '22'},
    '5': {'0': '5', '1': '10', '2': '11', '3': '12', '4': '13', '5': '14', '10': '15', '11': '20', '12': '21', '13': '22', '14': '23'},
}

_SUBTRACTION_MAP = {
    '0': {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5'},
    '1': {'0': '1', '1': '0', '2': '1', '3': '2', '4': '3', '5': '4'},
    '2': {'0': '2', '1': '1', '2': '0', '3': '1', '4': '2', '5': '3'},
    '3': {'0': '3', '1': '2', '2': '1', '3': '0', '4': '1', '5': '2'},
    '4': {'0': '4', '1': '3', '2': '2', '3': '1', '4': '0', '5': '1'},
    '5': {'0': '5', '1': '4', '2': '3', '3': '2', '4': '1', '5': '0'},
    '10': {'0': '10', '1':  '5', '2':  '4', '3':  '3', '4':  '2', '5':  '1'},
    '11': {'0': '11', '1': '10', '2':  '5', '3':  '4', '4':  '3', '5':  '2'},
    '12': {'0': '12', '1': '11', '2': '10', '3':  '5', '4':  '4', '5':  '3'},
    '13': {'0': '13', '1': '12', '2': '11', '3': '10', '4':  '5', '5':  '4'},
    '14': {'0': '14', '1': '13', '2': '12', '3': '11', '4': '10', '5':  '5'},
    '15': {'0': '15', '1': '14', '2': '13', '3': '12', '4': '11', '5': '10'},
}

_SUBTRACTION_BORROWED = {
    '0': '5',
    '1': '0',
    '2': '1',
    '3': '2',
    '4': '3',
    '5': '4',
}

_MULTIPLICATION_MAP = {
    '0': {'0': '0', '1': '0', '2':  '0', '3':  '0', '4':  '0', '5':  '0'},
    '1': {'0': '0', '1': '1', '2':  '2', '3':  '3', '4':  '4', '5':  '5'},
    '2': {'0': '0', '1': '2', '2':  '4', '3': '10', '4': '12', '5': '14'},
    '3': {'0': '0', '1': '3', '2': '10', '3': '13', '4': '20', '5': '23'},
    '4': {'0': '0', '1': '4', '2': '12', '3': '20', '4': '24', '5': '32'},
    '5': {'0': '0', '1': '5', '2': '14', '3': '23', '4': '32', '5': '41'},
}

_RECIPROCAL_MAP = {
    '2': '0.3', '3': '0.2', '4': '0.13', '5': '0.1p',
    '10': '0.1', '11': '0.05_p', '12': '0.043', '13': '0.04', '14': '0.03p', '15': '0.0313_4524_21__p',
    '20': '0.03', '21': '0.0243_4053_1215__p', '22': '0.0_23_p', '23': '0.02p', '24': '0.0213', '25': '0.0204_1224_5351_4331__p',
    '30': '0.02', '31': '0.0152_1132_5__p', '32': '0.014p', '33': '0.0_14_p', '34': '0.0__1345_2421_03__p', '35': '0.0132_2030_441__p',
    '40': '0.013', '41': '0.0123_5__p', '42': '0.0__1215_0243_4053__p', '43': '0.012', '44': '0.01_14_p', '45': '0.0112_4045_4431_51__p',
    '50': '0.01p', '51': '0.0105_45__p', '52': '0.0104_3', '53': '0.0__1031_3452_42__p', '54': '0.0__1020_4122_4535_1433__p', '55': '0.01_p',
    '100': '0.01', '101': '0.0055_p', '102': '0.0__0540_3442_3__p', '103': '0.0__0531_2150_2434__p', '104': '0.0052p', '105': '0.0051_3354_1244_0330_2344_5504_2201_4311_5225_3211_0051_3p',
    '110': '0.0_05_p', '111': '0.005_p', '112': '0.00__4524_2103_13__p', '113': '0.004p', '114': '0.0__0441_0132_203__p', '115': '0.0043_3240_3021_4420_1310_521__p',
    '120': '0.0043', '121': '0.0042_2405_5133_15__p', '122': '0.0__0415_3__p', '123': '0.0__0412_2453_5143_3102__p', '124': '0.00__4053_1215_0243__p', '125': '0.0040_2414_5112_4551_5314_1044_3100_4024_1451_1245_5153__14_p',
    '130': '0.004', '131': '0.0035_3214_25__p', '132': '0.003_50_p', '133': '0.0__0344_2305_4__p', '134': '0.0__0342_0225_2135_33__p', '135': '0.0033_5444_0223_5104_1343_2425_0301_4552_2011_1533_20_451_p',
    '140': '0.003p', '141': '0.0033_1250_4044_1544_5301_4342_3202_2055_2243_0515__1140_p', '142': '0.0__0325_23__p', '143': '0.00_32_p', '144': '0.0032_13', '145': '0.0031_5344_1251__p',
    '150': '0.0__0313_4524_21__p', '151': '0.0031_2020_5212_3325_4215_4531_5141_1304_5003_1202_0521__23_p', '152': '0.00__3102_0412_2453_5143__p', '153': '0.0__0304_4101_322__p', '154': '0.0_03_p', '155': '0.0030_1304_3214_0502_3113_3445_2241_2040_2010_0301_3043__21_p',
    '200': '0.003', '201': '0.0025_4304_2344_0354_0055_3012_5132_1152_0155_0025_4304__23_p', '202': '0.0_0253_p', '203': '0.0__0251_4__p', '204': '0.00__2501_5211_3__p', '205': '0.0024_4553_11__p',
    '210': '0.0__0243_4053_1215__p', '211': '0.0024_2232_5434_4413_0403_3512_3541_0214_0052_4505_5313__32_p', '212': '0.0024_1p', '213': '0.0024', '214': '0.0023_4455_0422_0143_1152_2532_1100_5133_5412_4403_3023_4p', '215': '0.0023_3404_2005_1121_2401_4224_2520_3245_2544_1053_4553_2p',
    '220': '0.00_23_p', '221': '0.0023_1252_1043_5415__p', '222': '0.0_023_p', '223': '0.0__0225_2135_3303_42__p', '224': '0.002__2421_0313_45__p', '225': '0.0022_3212_0312_2544_4151_5421_4303_3502_0045_0424_1024_5p',
    '230': '0.002p', '231': '0.0022_1241_1525__p', '232': '0.00__2203_0441_013__p', '233': '0.0__0215_34__p', '234': '0.0__0214_4201_3105_2100_4332_403__p', '235': '0.0021_3504_1__p',
    '240': '0.0021_3', '241': '0.0021_2055_3435__p', '242': '0.0__0211_2025_3443_53__p', '243': '0.00__2103_1345_24__p', '244': '0.00__2054_3__p',
}


class Sezimal:
    __slots__ = ['_value', '_sign', '_integer', '_fraction', '_precision', '_digits', 'reciprocal']

    def __init__(self, number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        original_decimal = None

        if type(number) == Decimal:
            original_decimal = number
            number = decimal_to_sezimal(str(number))

        elif type(number).__name__ in ('Dozenal', 'DozenalInteger'):
            number = dozenal_to_sezimal(str(number))

        elif type(number).__name__ == 'DozenalFraction':
            number = dozenal_to_sezimal(str(number.dozenal))

        elif type(number) == SezimalFraction:
            number = number.sezimal

        elif type(number) == str and ('/' in number or '⁄' in number or '÷' in number):
            number = SezimalFraction(number).sezimal

        cleaned_number = validate_clean_sezimal(number)

        if cleaned_number[0] == '-':
            cleaned_number = cleaned_number[1:]
            self._sign = -1
        else:
            self._sign = 1

        if '.' in cleaned_number:
            self._integer = str(int(cleaned_number.split('.')[0]))
            self._fraction = cleaned_number.split('.')[1]
        else:
            self._integer = str(int(cleaned_number))
            self._fraction = ''

        self._precision = len(self._fraction)
        self._digits = list(self._integer + self._fraction)

        #
        # Converts and stores as decimal
        #
        if original_decimal is None:
            with localcontext() as context:
                context.prec = MAX_DECIMAL_PRECISION
                self._value = Decimal(sezimal_to_decimal(cleaned_number)) ## .quantize(Decimal(f'1E-{_DECIMAL_PRECISION}'))
                self._value *= self._sign

        else:
            self._value = original_decimal

    def __str__(self) -> str:
        if self._sign == -1:
            res = '-' + self._integer
        else:
            res = self._integer

        if self._precision:
            res += '.'
            res += self._fraction

        return res

    def __repr__(self) -> str:
        if not self._fraction:
            return f"Sezimal('{self.formatted_number}') == Decimal('{decimal_format(self.decimal, decimal_places=0)}')"
        else:
            return f"Sezimal('{self.formatted_number}') == Decimal('{decimal_format(self.decimal, decimal_places=MAX_DECIMAL_PRECISION)}')"

    @property
    def formatted_number(self) -> str:
        return sezimal_format(str(self), sezimal_places=Decimal(self._precision))

    @property
    def decimal(self) -> Decimal:
        return self._value

    @property
    def decimal_formatted_number(self) -> str:
        if not self._fraction:
            return decimal_format(str(self._value), decimal_places=0)
        else:
            return decimal_format(str(self._value), decimal_places=MAX_DECIMAL_PRECISION)

    @property
    def dozenal(self) -> str:
        if not self._fraction:
            return dozenal_format(self, dozenal_places=0, group_separator='')
        else:
            return dozenal_format(self, group_separator='')

    @property
    def dozenal_formatted_number(self) -> str:
        if not self._fraction:
            return dozenal_format(self, dozenal_places=0)
        else:
            return dozenal_format(self)

    @property
    def niftimal(self) -> str:
        if not self._fraction:
            return niftimal_format(self, niftimal_places=0, group_separator='')
        else:
            return niftimal_format(self, group_separator='')

    @property
    def niftimal_formatted_number(self) -> str:
        if not self._fraction:
            return niftimal_format(self, niftimal_places=0)
        else:
            return niftimal_format(self)

    def __int__(self) -> int:
        return int(sezimal_to_decimal(self._integer)) * self._sign

    def __trunc__(self) -> IntegerSelf:
        return SezimalInteger(self._integer) * self._sign

    def __float__(self) -> float:
        return float(sezimal_to_decimal(str(self)))

    def __decimal__(self) -> Decimal:
        return self._value

    def __compare__(self, other_number: Self) -> IntegerSelf:
        #
        # If the sign of both numbers are not equal,
        # they can be compared only by their sign
        #
        if self._sign != other_number._sign:
            return self._sign

        #
        # The signs are the same, let’s check the numbers
        #
        precision = max(self._precision, other_number._precision)

        this = str(self._integer) + str(self._fraction).ljust(precision, '0')
        other = str(other_number._integer) + str(other_number._fraction).ljust(precision, '0')

        length = max(len(this), len(other))

        this = this.rjust(length, '0')
        other = other.rjust(length, '0')

        if this == other:
            return 0

        if self._sign == 1:
            return 1 if this > other else -1
        else:
            return -1 if this > other else 1

    def __eq__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> bool:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return self.__compare__(other_number) == 0

    def __ne__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> bool:
        return not self.__eq__(other_number)

    def __lt__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> bool:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return self.__compare__(other_number) < 0

    def __ge__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> bool:
        return not self.__lt__(other_number)

    def __gt__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> bool:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return self.__compare__(other_number) > 0

    def __le__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> bool:
        return not self.__gt__(other_number)

    def __hash__(self):
        return self.decimal.__hash__()

    def __bool__(self) -> bool:
        return not self == 0

    def __pos__(self) -> Self:
        return Sezimal(self)

    def __neg__(self) -> Self:
        return Sezimal(self * -1)

    def __abs__(self) -> Self:
        if self._sign == 1:
            return Sezimal(self)

        return Sezimal(self * -1)

    def __addition(self, other_number: Self) -> str:
        if other_number == 0:
            return str(self)

        #
        # Adds two values;
        # the final sign of the operation is dealt with by the calling method: __add__ or __sub__
        #
        digits_a = list(self._digits)
        digits_b = list(other_number._digits)

        #
        # Normalizes the fractional part between the two values,
        #
        if self._precision > other_number._precision:
            digits_b += list('0' * (self._precision - other_number._precision))
            final_precision = self._precision

        elif other_number._precision > self._precision:
            digits_a += list('0' * (other_number._precision - self._precision))
            final_precision = other_number._precision

        else:
            final_precision = self._precision

        digits_a = digits_a[::-1]
        digits_b = digits_b[::-1]

        adition = ''
        carries = '0'

        for i in range(max(len(digits_a), len(digits_b))):
            if i + 1 <= len(digits_a):
                d1 = digits_a[i]
            else:
                d1 = '0'

            if i + 1 <= len(digits_b):
                d2 = digits_b[i]
            else:
                d2 = '0'

            sd = _ADDITION_MAP[d1][d2]
            sd = _ADDITION_MAP[carries][sd]

            adition += sd[-1]

            if len(sd) > 1:
                carries = sd[0]
            else:
                carries = '0'

        if carries != '0':
            adition += carries

        if final_precision:
            adition = adition[0:final_precision] + '.' + adition[final_precision:]

        adition = adition[::-1]

        return adition

    def __subtraction(self, other_number: Self) -> str:
        if other_number == 0:
            return str(self)

        #
        # Subtracts the lesser value from the greater one;
        # the final sign of the operation is dealt with by the calling method: __add__ or __sub__
        #
        digits_a = list(self._digits)
        digits_b = list(other_number._digits)

        #
        # Normalizes the fractional part between the two values,
        #
        if self._precision > other_number._precision:
            digits_b += list('0' * (self._precision - other_number._precision))
            final_precision = self._precision

        elif other_number._precision > self._precision:
            digits_a += list('0' * (other_number._precision - self._precision))
            final_precision = other_number._precision

        else:
            final_precision = self._precision

        digits_a = digits_a[::-1]
        digits_b = digits_b[::-1]

        if abs(self) < abs(other_number):
            d = digits_a
            digits_a = digits_b
            digits_b = d

        subtraction = ''

        i = 0
        while i < len(digits_a):
            d1 = digits_a[i]

            if i + 1 <= len(digits_b):
                d2 = digits_b[i]
            else:
                d2 = '0'

            if d1 >= d2:
                sd = _SUBTRACTION_MAP[d1][d2]

            #
            # Vay presizar enprestar 1?
            #
            else:
                d1 = '1' + d1
                sd = _SUBTRACTION_MAP[d1][d2]

                #
                # Trata u enpréstimu nus prósimus díjitus,
                # kuydandu ki u 0 propaga u enpréstimu uma kaza
                # pra frenti
                #
                if len(digits_a) >= i + 1:
                    j = i + 1

                    while j < len(digits_a):
                        if digits_a[j] != '0':
                            digits_a[j] = _SUBTRACTION_BORROWED[digits_a[j]]
                            break

                        else:
                            digits_a[j] = _SUBTRACTION_BORROWED[digits_a[j]]
                            j += 1

                else:
                    i = len(digits_a)

            i += 1

            subtraction += sd

        if final_precision:
            subtraction = subtraction[0:final_precision] + '.' + subtraction[final_precision:]

        subtraction = subtraction[::-1]

        return subtraction

    def __add__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        #
        # Deals with the signs, and does the adition or subtraction accordingly
        #
        if self._sign == 1 and other_number._sign == 1:
            res = self.__addition(other_number)

        elif self._sign == 1 and other_number._sign == -1:
            res = self.__subtraction(other_number)

            if abs(other_number) > abs(self) and res[0] != '-':
                res = '-' + res

        elif self._sign == -1 and other_number._sign == -1:
            res = self.__addition(other_number)
            res = '-' + res

        elif self._sign == -1 and other_number._sign == 1:
            res = other_number.__subtraction(self)

            if abs(self) > abs(other_number) and res[0] != '-':
               res = '-' + res

        return Sezimal(res)

    def __radd__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__add__(self)

    def __sub__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        #
        # Deals with the signs, and does the adition or subtraction accordingly
        #
        if self._sign == 1 and other_number._sign == 1:
            res = self.__subtraction(other_number)

            if abs(other_number) > abs(self) and res[0] != '-':
                res = '-' + res

        elif self._sign == 1 and other_number._sign == -1:
            res = self.__addition(other_number)

        elif self._sign == -1 and other_number._sign == -1:
            res = self.__subtraction(other_number)

            if abs(self) > abs(other_number) and res[0] != '-':
                res = '-' + res

        elif self._sign == -1 and other_number._sign == 1:
            res = self.__addition(other_number)

            if res[0] != '-':
                res = '-' + res

        return Sezimal(res)

    def __rsub__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__sub__(self)

    def __round_half_up__(self, precision: IntegerSelf, last_digit: str, next_digit: str, to_discard: str) -> Self:
        adjust = Sezimal(0)

        if next_digit == '3':
            if to_discard.replace('0', '') != '':
                adjust = Sezimal(f'1e-{precision}') * self._sign
            elif last_digit in '135':
                adjust = Sezimal(f'1e-{precision}') * self._sign

        elif next_digit in '45':
            adjust = Sezimal(f'1e-{precision}') * self._sign

        return adjust

    def __round_half_down__(self, precision: IntegerSelf, last_digit: str, next_digit: str, to_discard: str) -> Self:
        adjust = Sezimal(0)

        if next_digit == '3':
            if to_discard.replace('0', '') != '':
                adjust = Sezimal(f'1e-{precision}') * self._sign

        elif next_digit in '45':
            adjust = Sezimal(f'1e-{precision}') * self._sign

        return adjust

    def __round__(self, precision: IntegerSelf = MAX_PRECISION) -> Self:
        precision = SezimalInteger(precision)

        if self._precision <= int(precision):
            return self

        to_round = self._integer + '.' + self._fraction[:int(precision)]

        if self._sign == -1:
            to_round = '-' + to_round

        if precision == 0:
            last_digit = self._integer[-1]
            next_digit = self._fraction[0]
            to_discard = self._fraction[1:]

        else:
            last_digit = self._fraction[int(precision) - 1]
            next_digit = self._fraction[int(precision)]
            to_discard = self._fraction[int(precision) + 1:]

        adjust = self.__round_half_up__(precision, last_digit, next_digit, to_discard)

        rounded = Sezimal(to_round) + adjust

        if rounded._sign != self._sign:
            rounded = Sezimal(0)

        return rounded

    def trunc(self, precision: IntegerSelf = MAX_PRECISION) -> Self:
        if precision is None:
            precision = 0

        precision = SezimalInteger(precision)

        if self._precision <= int(precision):
            return self

        to_round = self._integer + '.' + self._fraction[:int(precision)]

        if self._sign == -1:
            to_round = '-' + to_round

        return Sezimal(to_round)

    def is_integer(self) -> bool:
        return self == self.trunc(0)

    def _mult_div_finalizing(self):
        res = round(self, MAX_PRECISION)

        if str(res).endswith('5555'):
            res += Sezimal(f'1E-{decimal_to_sezimal(res._precision)}')

        return res

    def __multiplication(self, other_number: Self) -> str:
        if self == 0 or other_number == 0:
            return '0'

        if other_number == 1 or other_number == -1:
            if self._sign == -1:
                return str(self)[1:]
            else:
                return str(self)

        #
        # Multiplies two values;
        # the final sign of the operation is dealt with by the calling method: __mul__
        #
        digits_a = list(self._digits)[::-1]
        digits_b = list(other_number._digits)[::-1]
        final_precision = self._precision + other_number._precision
        sums = []

        i = 0
        for d1 in digits_a:
            carries = '0'
            sums.append('0' * i)
            i += 1

            for d2 in digits_b:
                md = _MULTIPLICATION_MAP[d1][d2]

                if carries != '0':
                    md = str(Sezimal(md) + carries)

                sums[-1] += md[-1]

                if len(md) != 1:
                    carries = md[0]
                else:
                    carries = '0'

            if carries != '0':
                sums[-1] += carries

        multiplication = Sezimal('0')

        for s in sums:
            if s:
                multiplication += Sezimal(s[::-1])

        multiplication = str(multiplication)

        if final_precision:
            multiplication = multiplication[::-1]

            if len(multiplication) < final_precision + 1:
                multiplication += '0' * (final_precision - len(multiplication) + 1)

            multiplication = multiplication[0:final_precision] + '.' + multiplication[final_precision:]
            multiplication = multiplication[::-1]

        return multiplication

    def __mul__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        #
        # Deals with the signs
        #
        if self._sign == 1 and other_number._sign == 1:
            res = self.__multiplication(other_number)

        elif self._sign == 1 and other_number._sign == -1:
            res = self.__multiplication(other_number)
            res = '-' + res

        elif self._sign == -1 and other_number._sign == -1:
            res = self.__multiplication(other_number)

        elif self._sign == -1 and other_number._sign == 1:
            res = self.__multiplication(other_number)
            res = '-' + res

        return Sezimal(res)._mult_div_finalizing()

    def __rmul__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__mul__(self)

    def __basic_division(self, dividend: Self, divisor: Self) -> tuple[Self]:
        remainder = dividend
        quotient = Sezimal('0')

        while remainder >= divisor:
            remainder -= divisor
            quotient += 1

        return quotient, remainder

    def new_division(self, dividend: Self, divisor: Self) -> tuple[Self]:
        if dividend < divisor:
            return Sezimal(0), dividend

        quotient = Sezimal('0')
        remainder = Sezimal(dividend._digits[0])

        for i in range(1, len(dividend._digits)):
            remainder *= 10
            remainder += Sezimal(dividend._digits[i])

            factor = Sezimal(0)

            while (divisor * (factor + 1)) < remainder:
                factor += 1

            quotient *= 10
            quotient += factor
            remainder -= divisor * factor

        return quotient, remainder

        # # Convert quotient and remainder to strings
        # remainder_str = ''
        # while remainder:
        #     remainder_str += str(remainder % base)
        #     remainder //= base
        #
        # # Return quotient and remainder as strings
        # return quotient_str, int(remainder_str[::-1])

    def __division(self, other_number: Self, max_precision: IntegerSelf = MAX_PRECISION) -> str:
        #
        # Divides two values;
        # the final sign of the operation is dealt with by the calling method: __div__
        #
        if other_number == 0:
            raise ZeroDivisionError('Division by zero')

        if self == 0:
            return '0'

        if other_number == 1:
            return str(self)

        if self == 1 and str(other_number) in _RECIPROCAL_MAP:
            return _RECIPROCAL_MAP[str(other_number)]

        max_precision = int(SezimalInteger(max_precision))

        digits_a = list(self._digits)
        digits_b = list(other_number._digits)

        #
        # Normalizes the fractional part between the two values,
        #
        if self._precision > other_number._precision:
            digits_b += list('0' * (self._precision - other_number._precision))
            final_precision = self._precision

        elif other_number._precision > self._precision:
            digits_a += list('0' * (other_number._precision - self._precision))
            final_precision = other_number._precision

        else:
            final_precision = self._precision

        initial_precision = final_precision

        dividend = Sezimal(''.join(digits_a))
        divisor = Sezimal(''.join(digits_b))
        quotient, remainder = self.__basic_division(dividend, divisor)
        max_precision = max(final_precision, max_precision) * 2

        while remainder > 0 and final_precision < max_precision:
            dividend = remainder * 10
            final_precision += 1
            q, remainder = self.__basic_division(dividend, divisor)
            quotient = Sezimal(str(quotient) + str(q))

        division = str(quotient)

        final_precision -= initial_precision

        if final_precision:
            division = division[::-1]

            if len(division) < final_precision + 1:
                division += '0' * (final_precision - len(division) + 1)

            division = division[0:final_precision] + '.' + division[final_precision:]
            division = division[::-1]

        return division

    def __truediv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        #
        # Calculate the reciprocal first
        #
        if hasattr(other_number, 'reciprocal'):
            reciprocal = other_number.reciprocal
        else:
            if type(other_number) != Sezimal:
                other_number = Sezimal(other_number)

            if other_number == 1 or other_number == -1:
                reciprocal = other_number
            else:
                reciprocal = Sezimal('1').__division(other_number) * other_number._sign

        return self * reciprocal

        # #
        # # Deals with the signs
        # #
        # if self._sign == 1 and other_number._sign == 1:
        #     res = self.__division(other_number)
        #
        # elif self._sign == 1 and other_number._sign == -1:
        #     res = self.__division(other_number)
        #     res = '-' + res
        #
        # elif self._sign == -1 and other_number._sign == -1:
        #     res = self.__division(other_number)
        #
        # elif self._sign == -1 and other_number._sign == 1:
        #     res = self.__division(other_number)
        #     res = '-' + res
        #
        # return Sezimal(res)._mult_div_finalizing()

    def __rtruediv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__truediv__(self)

    def __divmod__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> tuple[Self]:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        dividend = Sezimal(self._integer)
        divisor = Sezimal(other_number._integer)

        if divisor == 0:
            raise ZeroDivisionError('Division by zero')

        if divisor == 1:
            return dividend, Sezimal(0)

        quotient, remainder = self.__basic_division(dividend, divisor)

        if self._sign == 1 and other_number._sign == 1:
            pass

        elif self._sign == 1 and other_number._sign == -1:
            quotient *= -1
            remainder *= -1

            if remainder != 0:
                quotient -= 1
                remainder = dividend + (quotient * divisor)

        elif self._sign == -1 and other_number._sign == -1:
            remainder *= -1

        elif self._sign == -1 and other_number._sign == 1:
            quotient *= -1

            if remainder != 0:
                quotient -= 1
                remainder = (dividend + (quotient * divisor)) * -1

        return quotient, remainder

    def __floordiv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        quotient, remainder = self.__divmod__(other_number)
        return quotient

    def __rfloordiv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__floordiv__(self)

    def __mod__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        quotient, remainder = self.__divmod__(other_number)
        return remainder

    def __rmod__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__mod__(self)

    def factorial(self) -> Self:
        if self == 0 or self == 1:
            return Sezimal(1)

        if self == 2:
            return Sezimal(2)

        integer = Sezimal(self._integer)
        next_integer = integer - 1

        return integer * next_integer.factorial()

    def calculus_exp(self) -> Self:
        result = Sezimal(1)
        term = Sezimal(1)
        i = Sezimal(1)

        while term > 0:
            term *= self * (Sezimal(1) / i)
            result += term
            i += 1

        return result

    def exp(self) -> Self:
        result = self.decimal.exp()
        result = Sezimal(result)
        return result._mult_div_finalizing()

    # def calculus_ln(self) -> Self:
    #     result = Sezimal(0)
    #
    #     if str(self) in LOGARITHM_TABLE:
    #         return Sezimal(LOGARITHM_TABLE[str(self)])._mult_div_finalizing()
    #
    #     term = (self - 1) * (Sezimal(1) / self)
    #
    #     i = Sezimal(1)
    #
    #     while i <= 200:
    #         result += (term ** i) * (Sezimal(1) / i)
    #         i += 1
    #
    #     return result

    def ln(self) -> Self:
        result = self.decimal.ln()
        result = Sezimal(result)
        return result._mult_div_finalizing()

    def __calculus_power(self, other_number: Self) -> Self:
        if other_number == 0:
            return Sezimal(1)

        if self == 0:
            return Sezimal(0)

        if other_number < 0:
            return Sezimal(1) / self.__power(other_number * -1)

        if other_number.is_integer():
            result = self

            while other_number > 1:
                result *= self
                other_number -= 1

        else:
            result = self.ln() * other_number
            result = result.exp()

        return result

    def __power(self, other_number: Self) -> Self:
        #
        # When the exponent is an integer,
        # avoid loosing precision in the decimal conversion,
        #
        if other_number.is_integer():
            result = self

            negative = other_number < 0

            if negative:
                other_number *= -1

            while other_number > 1:
                result *= self
                other_number -= 1

            if negative:
                return 1 / result

            return result

        result = self.decimal ** other_number.decimal
        result = Sezimal(result)
        return result._mult_div_finalizing()

    def __pow__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return self.__power(other_number)

    def __rpow__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        return other_number.__pow__(self)

    def log(self) -> Self:
        with localcontext() as context:
            context.prec = int(MAX_PRECISION / 2)
            result = self.decimal.ln() / Decimal(6).ln()
            result = Sezimal(result)

        return result._mult_div_finalizing()

    def log2(self) -> Self:
        with localcontext() as context:
            context.prec = int(MAX_PRECISION / 2)
            result = self.decimal.ln() / Decimal(2).ln()
            result = Sezimal(result)

        return result._mult_div_finalizing()

    def log14(self) -> Self:
        with localcontext() as context:
            context.prec = int(MAX_PRECISION / 2)
            result = self.decimal.ln() / Decimal(10).ln()
            result = Sezimal(result)

        return result._mult_div_finalizing()

    def sqrt(self) -> Self:
        return self ** Sezimal('0.3')

    def _find_gcd(self, numerator: Self, denominator: Self) -> Self:
        if denominator == 0:
            return numerator

        return self._find_gcd(denominator, numerator % denominator)

    def as_integer_ratio(self) -> tuple[IntegerSelf, IntegerSelf]:
        if self.is_integer():
            return SezimalInteger(self), SezimalInteger(1)

        numerator = Sezimal(self._integer + self._fraction)
        denominator = Sezimal(f'1e+{SezimalInteger(Decimal(self._precision))}')

        gcd = self._find_gcd(numerator, denominator)
        numerator //= gcd
        denominator //= gcd

        return SezimalInteger(numerator), SezimalInteger(denominator)


class SezimalInteger(Sezimal):
    __slots__ = ['_value', '_sign', '_integer', '_fraction', '_precision', '_digits']

    def __init__(self, number: str | int | float | Decimal | Self | IntegerSelf | Dozenal | DozenalInteger) -> Self:
        original_decimal = None

        if type(number) == Decimal:
            original_decimal = number
            number = decimal_to_sezimal(str(number))

        cleaned_number = validate_clean_sezimal(number)

        if cleaned_number[0] == '-':
            cleaned_number = cleaned_number[1:]
            self._sign = -1
        else:
            self._sign = 1

        if '.' in cleaned_number:
            self._integer = str(int(cleaned_number.split('.')[0]))
            # self._fraction = cleaned_number.split('.')[1].replace('0', '')
            self._fraction = ''
        else:
            self._integer = str(int(cleaned_number))
            self._fraction = ''

        self._precision = len(self._fraction)
        self._digits = list(self._integer + self._fraction)

        if self._precision:
            raise ValueError(f'The number {number} has an invalid format for a sezimal integer number')

        #
        # Converts and stores as decimal
        #
        if original_decimal is None:
            self._value = Decimal(sezimal_to_decimal(cleaned_number))
            self._value *= self._sign
        else:
            self._value = original_decimal

    def __repr__(self) -> str:
        return super().__repr__().replace('Sezimal', 'SezimalInteger')

    def __index__(self):
        return int(self._integer, 6)


class SezimalFraction(Sezimal):
    __slots__ = ['_value', '_sign', '_integer', '_fraction', '_precision', '_digits', '_numerator', '_denominator', '_sezimal']

    def __init__(self, numerator: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction, denominator: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction = None) -> Self:
        if type(numerator) == str:
            if '/' in numerator:
                numerator, denominator = numerator.split('/')
            elif '⁄' in numerator:
                numerator, denominator = numerator.split('⁄')
            elif '÷' in numerator:
                numerator, denominator = numerator.split('÷')

        elif type(numerator) == Decimal:
            numerator = decimal_to_sezimal(str(numerator))

        cleaned_numerator = validate_clean_sezimal(numerator)

        if denominator is None:
            numerator = Sezimal(cleaned_numerator)
            numerator, denominator = numerator.as_integer_ratio()
            cleaned_numerator = str(numerator)
            cleaned_denominator = str(denominator)

        elif type(denominator) == Decimal:
            denominator = decimal_to_sezimal(str(denominator))
            cleaned_denominator = validate_clean_sezimal(denominator)

        else:
            cleaned_denominator = validate_clean_sezimal(denominator)

        self._numerator = Sezimal(cleaned_numerator)
        self._denominator = Sezimal(cleaned_denominator)
        # self._sezimal = self._numerator / self._denominator
        self._sezimal = Sezimal(self._numerator.decimal / self._denominator.decimal)

        super().__init__(self._sezimal)

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @property
    def sezimal(self):
        return self._sezimal

    @property
    def reciprocal(self) -> FractionSelf:
        return SezimalFraction(self._denominator, self._numerator)

    @reciprocal.setter
    def reciprocal(self, value):
        pass

    def __str__(self) -> str:
        if self._sign == -1:
            res = '-'
        else:
            res = ''

        res += str(self._numerator)
        res += ' / '
        res += str(self._denominator)

        return res

    def __repr__(self) -> str:
        return f"SezimalFraction('{self._numerator.formatted_number}/{self._denominator.formatted_number}') == {self._sezimal.__repr__()}"

    def as_integer_ratio(self) -> tuple[IntegerSelf, IntegerSelf]:
        return self._numerator, self._denominator

    def as_decimal_integer_ratio(self) -> tuple[Decimal, Decimal]:
        return int(self._numerator.decimal), int(self._denominator.decimal)

    def __mul__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) == SezimalFraction:
            numerator = self.numerator * other_number.numerator
            denominator = self.denominator * other_number.denominator
            return SezimalFraction(numerator, denominator)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if other_number._fraction == '':
            numerator = self.numerator * other_number
            denominator = self.denominator
            return SezimalFraction(numerator, denominator)

        return super().__mul__(other_number)

    def __rmul__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) == SezimalFraction:
            numerator = self.numerator * other_number.numerator
            denominator = self.denominator * other_number.denominator
            return SezimalFraction(numerator, denominator)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if other_number._fraction == '':
            numerator = self.numerator * other_number
            denominator = self.denominator
            return SezimalFraction(numerator, denominator)

        return super().__rmul__(other_number)

    # def __div__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
    #     if type(other_number) == SezimalFraction:
    #         numerator = self.numerator * other_number.denominator
    #         denominator = self.denominator * other_number.numerator
    #         return SezimalFraction(numerator, denominator)
    #
    #     if type(other_number) != Sezimal:
    #         other_number = Sezimal(other_number)
    #
    #     if other_number._fraction == '':
    #         numerator = self.numerator
    #         denominator = self.denominator * other_number
    #         return SezimalFraction(numerator, denominator)
    #
    #     return super().__div__(other_number)
    #
    # def __rdiv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
    #     if type(other_number) == SezimalFraction:
    #         numerator = self.numerator * other_number.denominator
    #         denominator = self.denominator * other_number.numerator
    #         return SezimalFraction(numerator, denominator)
    #
    #     if type(other_number) != Sezimal:
    #         other_number = Sezimal(other_number)
    #
    #     if other_number._fraction == '':
    #         numerator = self.numerator
    #         denominator = self.denominator * other_number
    #         return SezimalFraction(numerator, denominator)
    #
    #     return super().__rdiv__(other_number)

    def __truediv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) == SezimalFraction:
            numerator = self.numerator * other_number.denominator
            denominator = self.denominator * other_number.numerator
            return SezimalFraction(numerator, denominator)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if other_number._fraction == '':
            numerator = self.numerator
            denominator = self.denominator * other_number
            return SezimalFraction(numerator, denominator)

        return super().__truediv__(other_number)

    def __rtruediv__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) == SezimalFraction:
            numerator = self.numerator * other_number.denominator
            denominator = self.denominator * other_number.numerator
            return SezimalFraction(numerator, denominator)

        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if other_number._fraction == '':
            numerator = self.numerator
            denominator = self.denominator * other_number
            return SezimalFraction(denominator, numerator)

        return super().__rtruediv__(other_number)

    def __pow__(self, other_number: str | int | float | Decimal | Self | IntegerSelf | FractionSelf | Dozenal | DozenalInteger | DozenalFraction) -> FractionSelf | Self:
        if type(other_number) != Sezimal:
            other_number = Sezimal(other_number)

        if other_number._fraction == '':
            numerator = self.numerator ** other_number
            denominator = self.denominator ** other_number
            return SezimalFraction(numerator, denominator)

        return super().__pow__(other_number)


_numbers.Number.register(Sezimal)
_numbers.Integral.register(Sezimal)
_numbers.Rational.register(Sezimal)

_numbers.Number.register(SezimalInteger)
_numbers.Integral.register(SezimalInteger)

_numbers.Number.register(SezimalFraction)
_numbers.Integral.register(SezimalFraction)
