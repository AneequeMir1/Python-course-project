import pytest
from pslib.network import create_test_network
import pandapower as pp


def test_network_creation():
    net = create_test_network()
    assert hasattr(net, 'bus') and len(net.bus) > 0
