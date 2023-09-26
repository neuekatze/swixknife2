

from ..sezimal import Sezimal


#
# Time and Frequency
#
AGRIMA_TO_SECOND = Sezimal('1.504')
SECOND_TO_AGRIMA = Sezimal('0.3123_5012_3501_2350_1235_0123_5012_3501_2350_1235_0123_5013')

#
# Avrita = agrima⁻¹
#
AVRITA_TO_HERTZ = Sezimal('1.504')
HERTZ_TO_AVRITA = Sezimal('0.3123_5012_3501_2350_1235_0123_5012_3501_2350_1235_0123_5013')

#
# Civil time
#
UTA_TO_HOUR = Sezimal('0.4')
HOUR_TO_UTA = Sezimal('1.3')
POSHA_TO_MINUTE = Sezimal('1.04')
MINUTE_TO_POSHA = Sezimal('0.5222_2222_2222_2222_2222_2222_2222_2222_2222_2222_2222_2223')
ANUGA_TO_SECOND = Sezimal('0.0150_4')
SECOND_TO_ANUGA = Sezimal('31.2350_1235_0123_5012_3501_2350_1235_0123_5012_3501_2350_1234')
BODA_TO_SECOND = Sezimal('0.0015_04')
SECOND_TO_BODA = Sezimal('3123.5012_3501_2350_1235_0123_5012_3501_2350_1235_0123_5012_3500')


DAY_TO_AGRIMA = Sezimal('100_0000')
UTA_TO_AGRIMA = Sezimal('1_0000')
POSHA_TO_AGRIMA = Sezimal('100')
ANUGA_TO_AGRIMA = Sezimal('0.01')
BODA_TO_AGRIMA = Sezimal('0.0001')

UTA_TO_DAY = Sezimal('0.01')
POSHA_TO_DAY = Sezimal('0.0001')
AGRIMA_TO_DAY = Sezimal('0.0000_01')
ANUGA_TO_DAY = Sezimal('0.0000_0001')
BODA_TO_DAY = Sezimal('0.0000_0000_01')

#
# Length, Speed, Acceleration, Area, Volume
#
PADA_TO_METER = Sezimal('0.532')
METER_TO_PADA = Sezimal('1.0251_4025_1402_5140_2514_0251_4025_1402_5140_2514_0251_4024')

PADA_TO_KILOMETER = Sezimal('0.0001_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111')
KILOMETER_TO_PADA = Sezimal('5000')

CHAMAPADA_TO_KILOMETER = Sezimal('1.1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111')
KILOMETER_TO_CHAMAPADA = Sezimal('0.5')

PADA_TO_CENTIMETER = Sezimal('232.332')
CENTIMETER_TO_PADA = Sezimal('0.0021_5551_5041_1212_3052_0502_2505_5332_5241_4455_0042_5430')

PADA_TO_MILLIMETER = Sezimal('4141.532')
MILLIMETER_TO_PADA = Sezimal('0.0001_2221_5524_5312_0152_0030_1252_5543_1424_5514_4113_5213')

CHATIPADA_TO_MILLIMETER = Sezimal('0.4141_532')
MILLIMETER_TO_CHATIPADA = Sezimal('1.2221_5524_5312_0152_0030_1252_5543_1424_5514_4113_5212_4450')

PADA_TO_MILE = Sezimal('0.0000_4250_2045_5550_2334_1043_0203_0510_2450_4145_3202_4025')
MILE_TO_PADA = Sezimal('1_2014.0314_3354_2423_2202_2123_3214_1533_1125_5521_3344_1225_1223')

PADA_TO_YARD = Sezimal('1.0024_2003_2224_2351_2442_0250_0141_1211_5342_2101_2300_5035')
YARD_TO_PADA = Sezimal('0.5531_5112_0501_2515_5532_0240_5134_3533_1030_0523_3254_1131')

PADA_TO_FOOT = Sezimal('3.0121_0014_1121_1534_2210_1230_0503_4035_4511_0304_1302_3200')
FOOT_TO_PADA = Sezimal('0.1550_3422_4140_2543_5550_4052_1431_3151_0210_0145_1055_2230')

PADA_TO_INCH = Sezimal('100.2420_0322_2423_5124_4202_5001_4112_1153_4221_0123_0051_1030')
INCH_TO_PADA = Sezimal('0.0055_3151_1205_0125_1555_3202_4051_3435_3310_3005_2332_5411')

#
# Vega = pada × agrima⁻¹
# Vega = pada × avrita
#
# 1 km/h = 0.32 veg
# 1 veg = 1 ÷ 0.32 km/h
#
VEGA_TO_METER_PER_SECOND = Sezimal('0.3')
METER_PER_SECOND_TO_VEGA = Sezimal('2')

VEGA_TO_KILOMETER_PER_HOUR = Sezimal('1.4444_4444_4444_4444_4444_4444_4444_4444_4444_4444_4444_4445')
KILOMETER_PER_HOUR_TO_VEGA = Sezimal('0.32')

VEGA_TO_MILE_PER_HOUR = Sezimal('1.0413_3112_5543_3523_1404_3304_4143_4114_0242_2004_0041_5505')
MILE_PER_HOUR_TO_VEGA = Sezimal('0.5210_4211_0234_5454_1321_3254_2130_5142_0455_5533_0230_4535')

PADA_PER_AGRIMA_TO_METER_PER_SECOND = VEGA_TO_METER_PER_SECOND
PADA_PER_AGRIMA_TO_KILOMETER_PER_HOUR = VEGA_TO_KILOMETER_PER_HOUR
PADA_PER_AGRIMA_TO_MILE_PER_HOUR = VEGA_TO_MILE_PER_HOUR

#
# Tevara = pada × agrima⁻²
#
# 1 m/s² = 3.412 tvr = 3.412 pad/agm²
# 1 tvr = 1 ÷ 3.412 m/s²
#
TEVARA_TO_METER_PER_SQUARE_SECOND = Sezimal('0.1341_5304_1530_4153_0415_3041_5304_1530_4153_0415_3041_5305')
METER_PER_SQUARE_SECOND_TO_TEVARA = Sezimal('3.412')
PADA_PER_SQUARE_AGRIMA_TO_METER_PER_SQUARE_SECOND = TEVARA_TO_METER_PER_SQUARE_SECOND

#
# Keshe = pada²
#
KESHE_TO_SQUARE_METER = Sezimal('0.5051_04')  # 0.532²
SQUARE_METER_TO_KESHE = Sezimal('1.0555_3532_0340_4132_4023_1123_2544_4242_0522_5302_1251_2000')
SQUARE_PADA_TO_SQUARE_METER = KESHE_TO_SQUARE_METER

#
# Ekadimakeshe = EDksh = EDpd² = 1_0000_0000 pd²
#
# 1 km² = 0.41 EDksh = 0.41 Cpad²
# 1 EDksh = 1 Cpad² = 1 ÷ 0.41
#
EKADIMAKESHE_TO_SQUARE_KILOMETER = Sezimal('1.2350_1235_0123_5012_3501_2350_1235_0123_5012_3501_2350_1234')
SQUARE_KILOMETER_TO_EKADIMAKESHE = Sezimal('0.41')
SQUARE_CHAMAPADA_TO_SQUARE_KILOMETER = EKADIMAKESHE_TO_SQUARE_KILOMETER
SQUARE_KILOMETER_TO_SQUARE_CHAMAPADA = SQUARE_KILOMETER_TO_EKADIMAKESHE

#
# Aytan = pada³
# Varti = ayta ÷ 1_0000 = pada³ ÷ 1_0000
#
AYTAN_TO_CUBIC_METER = Sezimal('0.4432_4501_2')  # 0.532³
CUBIC_METER_TO_AYTAN = Sezimal('1.1320_3304_2330_0141_1135_3423_1432_5434_2521_1220_3011_5310')
CUBIC_PADA_TO_CUBIC_METER = AYTAN_TO_CUBIC_METER
CUBIC_METER_TO_CUBIC_PADA = CUBIC_METER_TO_AYTAN

AYTAN_TO_LITER = Sezimal('3401.4554_3301_2')  # 0.532³ × 4344
LITER_TO_AYTAN = Sezimal('0.0001_3443_4554_4551_4240_3400_3551_3435_0450_1422_5022_2514')
CUBIC_PADA_TO_LITER = AYTAN_TO_LITER
LITER_TO_CUBIC_PADA = LITER_TO_AYTAN

VARTI_TO_CUBIC_METER = Sezimal('0.0000_4432_4501_2')  # 0.532³ ÷ 1_0000
CUBIC_METER_TO_VARTI = Sezimal('1_1320.3304_2330_0141_1135_3423_1432_5434_2521_1220_3011_5305_4514')
VARTI_TO_LITER = Sezimal('0.3401_4554_3301_2')  # 0.532³ ÷ 1_0000 × 4344
LITER_TO_VARTI = Sezimal('1.3443_4554_4551_4240_3400_3551_3435_0450_1422_5022_2513_5510')

#
# Mass and Density
#
# 1 kg = 0.532 drv
# 1 drv = 1 ÷ 0.532 kg
#
DRAVYA_TO_KILOGRAM = Sezimal('1.0251_4025_1402_5140_2514_0251_4025_1402_5140_2514_0251_4024')
KILOGRAMA_TO_DRAVYA = Sezimal('0.532')

#
# Gana = dravya ÷ ayta = dravya ÷ pada³
#
# 1 kg/m³ = 0.4224_3331_5224 gan = 0.4224_3331_5224 drv/pad³ = 0.4224_3331_5224 drv/ayt
# 1 gan = 1 ÷ 0.4224_3331_5224 kg/m³
#
GANA_TO_KILOGRAM_PER_CUBIC_METER = Sezimal('1.2055_1055_0052_2412_3020_3152_2051_1401_1240_2120_0222_1515')
KILOGRAM_PER_CUBIC_METER_TO_GANA = Sezimal('0.4224_3331_5224')
DRAVYA_PER_AYTA_TO_KILOGRAM_PER_CUBIC_METER = GANA_TO_KILOGRAM_PER_CUBIC_METER
DRAVYA_PER_CUBIC_PADA_TO_KILOGRAM_PER_CUBIC_METER = GANA_TO_KILOGRAM_PER_CUBIC_METER

#
# Force/Weight, Pressure, Energy/Work/Heat, Power
#

#
# Force / Weight
#
# Bara = dravya × pada × agrima⁻²
# Bara = dravya × tevara
#
# 1 Newton = 3.2324_24 bar
# 1 bar = 1 ÷ 3.2324_24 N
#
BARA_TO_NEWTON = Sezimal('0.1425_5252_0053_1022_1003_4450_5124_1040_3120_4213_3212_0000')
NEWTON_TO_BARA = Sezimal('3.2324_24')

#
# Pressure
#
# Daba = dravya × pada⁻¹ × agrima⁻²
# Daba = bara × pada⁻² = bara × keshe⁻¹
# Daba = karya × pada⁻³ = karya × ayta⁻¹
#
# 1 Pascal = 2.5350_2211_3344 dab
# 1 dab = 1 ÷ 2.5350_2211_3344 Pa
#
DABA_TO_PASCAL = Sezimal('0.2012_4442_4312_0402_0433_0455_0311_4530_1510_0320_0033_3300')
PASCAL_TO_DABA = Sezimal('2.5350_2211_3344')

#
# Energy/Work/Heat
#
# Karya = dravya × pada² × agrima⁻²
# Karya = bara × pada
# Karya = daba × aytan
#
# 1 J = 3.412 karya
# 1 karya = 1 ÷ 3.412 J
#
KARYA_TO_JOULE = Sezimal('0.1341_5304_1530_4153_0415_3041_5304_1530_4153_0415_3041_5305')
JOULE_TO_KARYA = Sezimal('3.412')

#
# Power
#
# Shati = dravya × pada² × agrima⁻³ = dravya × keshe × agrima⁻³
# Shati = karya × agrima⁻¹
# Shati = bara × pada × agrima⁻¹
# Shati = daba × pada³ × agrima⁻¹ = daba × aytan × agrima⁻¹
#
# 1 W = 10.5052_52 sht
# 1 sht = 1 ÷ 10.5052_52 W
#
SHATI_TO_WATT = Sezimal('0.0512_5424_0024_3311_0301_5223_2342_0320_1340_2104_4403_5400')
WATT_TO_SHATI = Sezimal('10.5052_52')

#
# Electric Current
#
DARA_TO_AMPERE = Sezimal('0.3123_5012_3501_2350_1235_0123_5012_3501_2350_1235_0123_5013')
AMPERE_TO_DARA = Sezimal('1.504')

#
# Electric Charge
#
AVESHA_TO_COULOMB = Sezimal('1')
COULOMB_TO_AVESHA = Sezimal('1')

#
# Electric Potential Difference
#
VIBAVA_TO_VOLT = Sezimal('0.1341_5304_1530_4153_0415_3041_5304_1530_4153_0415_3041_5305')
VOLT_TO_VIBAVA = Sezimal('3.412')

#
# Electrical Resistance
#
PRATIRODA_TO_OHM = Sezimal('0.3')
OHM_TO_PRATIRODA = Sezimal('2')

#
# Electrical Conductance
#
CHALANA_TO_SIEMENS = Sezimal('2')
SIEMENS_TO_CHALANA = Sezimal('0.3')

#
# Electrical Inductance
#
PRERAKA_TO_HENRY = Sezimal('0.532')
HENRY_TO_PRERAKA = Sezimal('1.0251_4025_1402_5140_2514_0251_4025_1402_5140_2514_0251_4024')

#
# Electrical Capacitance
#
SAMAI_TO_FARAD = Sezimal('3.412')
FARAD_TO_SAMAI = Sezimal('0.1341_5304_1530_4153_0415_3041_5304_1530_4153_0415_3041_5305')

#
# Magnetic Flux
#
ABIVA_TO_WEBER = Sezimal('0.3')
WEBER_TO_ABIVA = Sezimal('2')

#
# Magnetic Flux Density
#
VISTARA_TO_TESLA = Sezimal('0.3255_4544_0150_2044_2011_3341_4252_2121_0241_2431_0423_4001')
TESLA_TO_VISTARA = Sezimal('1.4142_12')

#
# Temperature
#
# 1 K = 3.412 gtk
# 1 gtk = 1 ÷ 3.412 K
#
GATIKA_TO_KELVIN = Sezimal('0.1341_5304_1530_4153_0415_3041_5304_1530_4153_0415_3041_5305')
KELVIN_TO_GATIKA = Sezimal('3.412')


#
# Currency
#
MANI_TO_MISALI = Sezimal('0.0000_0001')
MISALI_TO_MANI = Sezimal('1_0000_0000')

MANI_TO_SATOSHI = Sezimal('1')
SATOSHI_TO_MANI = Sezimal('1')

MISALI_TO_SATOSHI = Sezimal('1_0000_0000')
SATOSHI_TO_MISALI = Sezimal('0.0000_0001')

MANI_TO_BITCOIN = Sezimal('0.0000_0000_0033_4335_0332_2223_1144_0532_5021_4152_2431_5050')
BITCOIN_TO_MANI = Sezimal('135_3120_2544')

MISALI_TO_BITCOIN = Sezimal('0.0033_4335_0332_2223_1144_0532_5021_4152_2431_5045_5321_0221')
BITCOIN_TO_MISALI = Sezimal('135.3120_2544')


#
# Proportions
#
PERNIFF_TO_PERCENTAGE = Sezimal('2.44')
PERCENTAGE_TO_PERNIFF = Sezimal('0.2054_3205_4320_5432_0543_2054_3205_4320_5432_0543_2054_3210')

PERSIXNIFF_TO_PERCENTAGE = Sezimal('0.244')
PERCENTAGE_TO_PERSIXNIFF = Sezimal('2.0543_2054_3205_4320_5432_0543_2054_3205_4320_5432_0543_2055')

PERUNEXIAN_TO_PERCENTAGE = Sezimal('0.0244')
PERCENTAGE_TO_PERUNEXIAN = Sezimal('20.5432_0543_2054_3205_4320_5432_0543_2054_3205_4320_5432_0543')

PERNIFF_TO_PERMILLE = Sezimal('43.44')
PERMILLE_TO_PERNIFF = Sezimal('0.0114_3534_1020_0324_2255_0452_1311_4353_4102_0032_4225_5045')

PERSIXNIFF_TO_PERMILLE = Sezimal('4.344')
PERMILLE_TO_PERSIXNIFF = Sezimal('0.1143_5341_0200_3242_2550_4521_3114_3534_1020_0324_2255_0452')

PERUNEXIAN_TO_PERMILLE = Sezimal('0.4344')
PERMILLE_TO_PERUNEXIAN = Sezimal('1.1435_3410_2003_2422_5504_5213_1143_5341_0200_3242_2550_4522')
