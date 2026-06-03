from point import Point
from route import Route

route = Route()

route.add_location(Point(0, 0))
route.add_location(Point(3, 4))
route.add_location(Point(6, 8))

print("Total Distance:", route.total_distance())
