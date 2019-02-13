from types import SimpleNamespace
from pint import UnitRegistry

ureg = UnitRegistry()

meter                  = 1       * ureg.meter
kilometer              = 1000    * meter
degree                 = 1       * ureg.deg
radian                 = 1       * ureg.rad
sec                    = 1       * ureg.sec
minute                 = 60      * sec
hour                   = 60      * minute
day                    = 24      * hour
squared_meter          = 1       * meter ** 2 
squared_kilometer      = 10 ** 6 * meter ** 2
# meters_per_sec         = 1       * meter / sec
# meters_per_sec_squared = 1       * meter / (sec ** 2)

# TODO: Add Time, Speed, (Accel?) Units

Units = SimpleNamespace(
    m = meter,
    meter = meter,
    meters = meter,
    km = kilometer,
    kilometer = kilometer,
    kilometers = kilometer,
    deg = degree,
    degree = degree,
    degrees = degree,
    rad = radian,
    radian = radian,
    radians = radian,
    s = sec,
    sec = sec,
    second = sec,
    seconds = sec,
    min = minute,
    minute = minute,
    h = hour,
    hour = hour,
    sqm = squared_meter,
    squared_meter = squared_meter,
    meter_squared = squared_meter,
    squared_kilometer = squared_kilometer,
    kilometer_squared = squared_kilometer,
    sqkm = squared_kilometer,
}

def fromTimedelta(timedelta):
    seconds = timedelta.total_seconds()
    return seconds * Units.s