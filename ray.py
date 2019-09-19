import vec3

class ray:
    def __init__(self, origin, direction):
        self.start = origin
        self.dir = direction

    def origin(self):
        return self.start

    def direction(self):
        return self.dir

#    def point_at_parameter(self, dist):
#        return self.start + vec3.mul_float(self.direction, dist)