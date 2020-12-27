class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5
    def mass_calculation(self):
        mass = self._width * self._length * self.height * self.weight
        print(mass)
        return mass

road = Road(5000, 300)
road.mass_calculation()