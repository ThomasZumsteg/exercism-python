"""Calculates age on various planets"""

class SpaceAge(object):
    """Calculates age on various planets"""
    _earth_year = 31557600 # seconds

    def __init__(self, seconds):
        """Stores age builds functions"""
        self.seconds = seconds
        # Function                           Ratio to earth year
        self.on_earth = self.on_planet_gen(1.0)
        self.on_mercury = self.on_planet_gen(0.2408467)
        self.on_venus = self.on_planet_gen(0.61519726)
        self.on_mars = self.on_planet_gen(1.8808158)
        self.on_jupiter = self.on_planet_gen(11.862615)
        self.on_saturn = self.on_planet_gen(29.447498)
        self.on_uranus = self.on_planet_gen(84.016846)
        self.on_neptune = self.on_planet_gen(164.79132)

    def on_planet_gen(self, ratio_to_earth):
        """Returns a function that converts seconds into planet years"""
        def on_planet():
            """Converts seconds to planet years"""
            return round(self.seconds / (self._earth_year * ratio_to_earth), 2)
        return on_planet
