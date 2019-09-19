import vec3

class ray:
    def __init__(self, origin, dir):
        self.origin = origin
        self.dir = dir

    @property
    def origin(self):
        return self.origin

    @property
    def direction(self):
        return self.dir

    def point_at_parameter(self, dist):
        return self.origin + vec3.mul_float(self.dir, dist)