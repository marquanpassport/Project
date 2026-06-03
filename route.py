"class Route:
    def __init__(self):
        self.locations = []

    def add_location(self, point):
        self.locations.append(point)

    def total_distance(self):
        distance = 0

        for i in range(len(self.locations) - 1):
            distance += self.locations[i].distance_to(
                self.locations[i + 1]
            )

        return round(distance, 2)
