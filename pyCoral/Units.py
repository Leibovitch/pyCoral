from types import SimpleNamespace
from pint import UnitRegistry

ureg = UnitRegistry()

meter     = 1    * ureg.meter
kilometer = 1000 * meter
degree    = 1    * ureg.deg
radian    = 1    * ureg.rad

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
)