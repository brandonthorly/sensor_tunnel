from typing import List

from sensor_node import SensorNode
from sensor_tunnel import SensorTunnel


class TestSensorTunnel(object):

    def test_graph_build(self):
        node1 = SensorNode(0, 0, 1)
        node2 = SensorNode(1, 0, 1)
        node3 = SensorNode(2, 0, 1)
        node4 = SensorNode(0, 3, 1)

        sensor_list = [node1, node2, node3, node4]

        tunnel = SensorTunnel(3, 2, sensor_list)

        graph = tunnel.sensor_graph

        for sensor in sensor_list:
            assert sensor in graph.keys()

        self.assert_expected_edges(graph[node1], [node2, node3])
        self.assert_expected_edges(graph[node2], [node1, node3])
        self.assert_expected_edges(graph[node3], [node1, node2])
        self.assert_expected_edges(graph[node4], [])

    @staticmethod
    def assert_expected_edges(edges: List[SensorNode], expected_edges: List[SensorNode]) -> None:
        for edge in edges:
            assert edge in expected_edges

    def test_can_pass_through_undetected_true_no_top_intersect(self):
        node1 = SensorNode(0, 2, 1)
        node2 = SensorNode(0, 3, 1)
        node3 = SensorNode(0, 4, 1)
        node4 = SensorNode(1, 4, 1)

        sensor_list = [node1, node2, node3, node4]

        tunnel = SensorTunnel(4, 1, sensor_list)

        assert tunnel.can_pass_through_undetected()

    def test_can_pass_through_undetected_true_no_bottom_intersect(self):
        node1 = SensorNode(0, 0, 1)
        node2 = SensorNode(0, 1, 1)
        node3 = SensorNode(0, 2, 1)
        node4 = SensorNode(1, 3, 1)

        sensor_list = [node1, node2, node3, node4]

        tunnel = SensorTunnel(5, 1, sensor_list)

        assert tunnel.can_pass_through_undetected()

    def test_can_pass_through_undetected_true_top_and_bottom_intersect(self):
        node1 = SensorNode(0, 0, 1)
        node2 = SensorNode(0, 1, 1)
        node3 = SensorNode(2, 2, 1)
        node4 = SensorNode(2, 3, 1)

        sensor_list = [node1, node2, node3, node4]

        tunnel = SensorTunnel(4, 2, sensor_list)

        assert tunnel.can_pass_through_undetected()

    def test_can_pass_through_undetected_true_offset(self):
        node1 = SensorNode(0, 0, 1)
        node2 = SensorNode(0, 1, 1)
        node3 = SensorNode(2, 2, 1)
        node4 = SensorNode(2, 3, 1)

        sensor_list = [node1, node2, node3, node4]

        tunnel = SensorTunnel(4, 2, sensor_list)

        assert tunnel.can_pass_through_undetected()

    def test_can_pass_through_undetected_false_offset(self):
        node1 = SensorNode(0, 0, 1)
        node2 = SensorNode(0, 1, 1)
        node3 = SensorNode(1, 2, 1)
        node4 = SensorNode(1, 3, 1)

        sensor_list = [node1, node2, node3, node4]

        tunnel = SensorTunnel(4, 2, sensor_list)

        assert not tunnel.can_pass_through_undetected()
