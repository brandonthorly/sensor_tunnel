from typing import List, Dict, Set

from sensor_node import SensorNode


class SensorTunnel(object):
    width: int
    length: int
    sensors: List[SensorNode]
    sensor_graph: Dict
    intersect_top_sensors: Set

    def __init__(self, width: int, length: int, sensors: List[SensorNode]):
        self.width = width
        self.length = length
        self.sensors = sensors
        self.build_graph()

    def build_graph(self) -> None:
        self.sensor_graph = {}
        self.intersect_top_sensors = set()

        for sensor in self.sensors:
            if sensor.y > self.width and sensor.x > self.length:
                raise ValueError('Attempting to place sensors in tunnel with coordinates outside tunnel bounds')

            self.sensor_graph[sensor] = []

            if sensor.intersects_top():
                self.intersect_top_sensors.add(sensor)

            for other_sensor in self.sensors:
                if sensor == other_sensor:
                    continue

                if sensor.intersects_node(other_sensor):
                    self.sensor_graph[sensor].append(other_sensor)

    def can_pass_through_undetected(self) -> bool:
        for intersect_top_sensor in self.intersect_top_sensors:
            intersects_bottom = self.search_for_intersects_bottom(intersect_top_sensor)

            if intersects_bottom:
                return False

        return True

    def search_for_intersects_bottom(self, node: SensorNode, visited: Set = None) -> bool:
        if not visited:
            visited = set()

        edges = [s for s in self.sensor_graph[node] if s not in visited]

        if len(edges) == 0:
            return False

        for edge in edges:
            if edge.intersects_bottom(self.width):
                return True

            else:
                visited.add(edge)
                return self.search_for_intersects_bottom(edge, visited)




