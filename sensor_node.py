from math import sqrt


class SensorNode(object):
    x: int
    y: int
    r: int

    def __init__(self, x: int, y: int, r: int):
        if x < 0 or y < 0 or r < 0:
            raise ValueError('x, y, and r for the sensor node must be greater than or equal to zero')
        self.x = x
        self.y = y
        self.r = r

    def intersects_node(self, sensor_node) -> bool:
        return sqrt((self.x - sensor_node.x) ** 2 + (self.y - sensor_node.y) ** 2) <= self.r + sensor_node.r

    def intersects_top(self) -> bool:
        return self.y - self.r <= 0

    def intersects_bottom(self, tunnel_width: int) -> bool:
        return self.y + self.r >= tunnel_width
