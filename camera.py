
import ray
import vec3

class camera:
    
    def __init__(self):
        self.lower_left_corner = vec3.vec3([-2.0, -1.0, -1.0])
        self.horizontal = vec3.vec3([4.0, 0.0, 0.0])
        self.vertical = vec3.vec3([0.0, 2.0, 0.0])
        self.origin = vec3.vec3([0.0, 0.0, 0.0])

    def get_ray(self, x_percent, y_percent):
        ray_dir = self.lower_left_corner
        ray_dir += vec3.mul_float(self.horizontal, x_percent)
        ray_dir += vec3.mul_float(self.vertical, y_percent)
        return ray.ray(origin=self.origin, direction=ray_dir)