from sensor_node import SensorNode


class TestSensorNode(object):

    def test_intersecting_sensor_true(self):
        node = SensorNode(0, 1, 1)
        node2 = SensorNode(0, 2, 1)

        assert node.intersects_node(node2), 'Overlapping sensors not intersecting'

    def test_intersecting_sensor_true_offset(self):
        node = SensorNode(0, 1, 1)
        node2 = SensorNode(1, 1, 1)

        assert node.intersects_node(node2), 'Overlapping sensors offset x,y not intersecting'

    def test_intersecting_sensor_exactly(self):
        node = SensorNode(0, 1, 1)
        node2 = SensorNode(0, 3, 1)

        assert node.intersects_node(node2), 'sensor radius meeting not intersecting'

    def test_intersecting_sensor_false(self):
        node = SensorNode(0, 1, 1)
        node2 = SensorNode(2, 2, 1)

        assert not node.intersects_node(node2), 'non overlapping sensors'

    def test_intersects_top_true(self):
        node = SensorNode(0, 1, 2)

        assert node.intersects_top(), 'Larger radius than y coordinate not intersecting top bound'

    def test_intersects_top_exactly_true(self):
        node = SensorNode(0, 1, 1)

        assert node.intersects_top(), 'Matching y coordinate and radius not intersecting top bound'

    def test_intersects_top_false(self):
        node = SensorNode(0, 2, 1)

        assert not node.intersects_top(), 'Greater y coordinate than radius intersecting top bound'

    def test_intersects_bottom_true(self):
        node = SensorNode(0, 1, 1)

        assert node.intersects_bottom(1), 'y + r > tunnel width not intersecting bottom bound'

    def test_intersects_bottom_exactly_true(self):
        node = SensorNode(0, 1, 1)

        assert node.intersects_bottom(2), 'y + r == tunnel width not intersecting bottom bound'

    def test_intersects_bottom_false(self):
        node = SensorNode(0, 1, 1)

        assert not node.intersects_bottom(3), 'y + r < tunnel width intersecting bottom bound'
