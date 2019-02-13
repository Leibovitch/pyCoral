from pyCoral.geographic import Algorithms
from pyCoral.geographic import Point
from pyCoral import Units 

p1 = Point()
p2 = Point(1, 0)
# print(Algorithms.azimuth(p1, p2))

# p2 = Point(1,1)
# print(Algorithms.azimuth(p1, p2))

# p2 = Point(0,1)
# print(Algorithms.azimuth(p1, p2))

# p2 = Point(-1, 1)
# print(Algorithms.azimuth(p1, p2))

# p2 = Point(-1, 0)
# print(Algorithms.azimuth(p1, p2))

# p2 = Point(-1, -1)
# print(Algorithms.azimuth(p1, p2))

# p2 = Point(0, -1)
# print(Algorithms.azimuth(p1, p2))

# p2 = Point(1, -1)
# print(Algorithms.azimuth(p1, p2))

print(Algorithms.translate(p1, Algorithms.azimuth(p1, p2), 100 * Units.kilometer))
p2 = Point(1,1)

print(Algorithms.translate (p1, Algorithms.azimuth(p1, p2), 100 * Units.kilometer))
p2 = Point(0,1)

print(Algorithms.translate (p1, Algorithms.azimuth(p1, p2), 100 * Units.kilometer))
p2 = Point(-1, 1)

print(Algorithms.translate (p1, Algorithms.azimuth(p1, p2), 100 * Units.kilometer))
p2 = Point(-1, 0)

print(Algorithms.translate (p1, Algorithms.azimuth(p1, p2), 100 * Units.kilometer))
p2 = Point(-1, -1)

print(Algorithms.translate (p1, Algorithms.azimuth(p1, p2), 100 * Units.kilometer))
p2 = Point(0, -1)

print(Algorithms.translate (p1, Algorithms.azimuth(p1, p2), 100 * Units.kilometer))
p2 = Point(1, -1)