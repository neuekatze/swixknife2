

from ..sezimal import Sezimal, SezimalInteger, SezimalFraction
from decimal import Decimal


#
# Proportions
#
PERNIF_TO_PERCENTAGE = SezimalFraction('244 / 100')
PERCENTAGE_TO_PERNIF = SezimalFraction('100 / 244')
PERNIF_TO_PERCENTAGE.reciprocal = PERCENTAGE_TO_PERNIF
PERCENTAGE_TO_PERNIF.reciprocal = PERNIF_TO_PERCENTAGE

PERARDA_TO_PERCENTAGE = SezimalFraction('244 / 1_000')
PERCENTAGE_TO_PERARDA = SezimalFraction('1_000 / 244')
PERARDA_TO_PERCENTAGE.reciprocal = PERCENTAGE_TO_PERARDA
PERCENTAGE_TO_PERARDA.reciprocal = PERARDA_TO_PERCENTAGE

PERSIXARDA_TO_PERCENTAGE = SezimalFraction('244 / 10_000')
PERCENTAGE_TO_PERSIXARDA = SezimalFraction('10_000 / 244')
PERSIXARDA_TO_PERCENTAGE.reciprocal = PERCENTAGE_TO_PERSIXARDA
PERCENTAGE_TO_PERSIXARDA.reciprocal = PERSIXARDA_TO_PERCENTAGE

PERSIXNIF_TO_PERCENTAGE = SezimalFraction('244 / 1_000')
PERCENTAGE_TO_PERSIXNIF = SezimalFraction('1_000 / 244')
PERSIXNIF_TO_PERCENTAGE.reciprocal = PERCENTAGE_TO_PERSIXNIF
PERCENTAGE_TO_PERSIXNIF.reciprocal = PERSIXNIF_TO_PERCENTAGE

PERUNEXIAN_TO_PERCENTAGE = SezimalFraction('244 / 10_000')
PERCENTAGE_TO_PERUNEXIAN = SezimalFraction('10_000 / 244')
PERUNEXIAN_TO_PERCENTAGE.reciprocal = PERCENTAGE_TO_PERUNEXIAN
PERCENTAGE_TO_PERUNEXIAN.reciprocal = PERUNEXIAN_TO_PERCENTAGE

PERARDA_TO_PERMILLE = SezimalFraction('4_344 / 1_000')
PERMILLE_TO_PERARDA = SezimalFraction('1_000 / 4_344')
PERARDA_TO_PERMILLE.reciprocal = PERMILLE_TO_PERARDA
PERMILLE_TO_PERARDA.reciprocal = PERARDA_TO_PERMILLE

PERSIXARDA_TO_PERMILLE = SezimalFraction('4_344 / 10_000')
PERMILLE_TO_PERSIXARDA = SezimalFraction('10_000 / 4_344')
PERSIXARDA_TO_PERMILLE.reciprocal = PERMILLE_TO_PERSIXARDA
PERMILLE_TO_PERSIXARDA.reciprocal = PERSIXARDA_TO_PERMILLE

PERNIF_TO_PERMILLE = SezimalFraction('4_344 / 100')
PERMILLE_TO_PERNIF = SezimalFraction('100 / 4_344')
PERNIF_TO_PERMILLE.reciprocal = PERMILLE_TO_PERNIF
PERMILLE_TO_PERNIF.reciprocal = PERNIF_TO_PERMILLE

PERSIXNIF_TO_PERMILLE = SezimalFraction('4_344 / 1_000')
PERMILLE_TO_PERSIXNIF = SezimalFraction('1_000 / 4_344')
PERSIXNIF_TO_PERMILLE.reciprocal = PERMILLE_TO_PERSIXNIF
PERMILLE_TO_PERSIXNIF.reciprocal = PERSIXNIF_TO_PERMILLE

PERUNEXIAN_TO_PERMILLE = SezimalFraction('4_344 / 10_000')
PERMILLE_TO_PERUNEXIAN = SezimalFraction('10_000 / 4_344')
PERUNEXIAN_TO_PERMILLE.reciprocal = PERMILLE_TO_PERUNEXIAN
PERMILLE_TO_PERUNEXIAN.reciprocal = PERUNEXIAN_TO_PERMILLE
