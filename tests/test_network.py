import pytest
from pslib.network import create_test_network, create_loads, run_powerflow
import pandapower as pp


def test_network_creation():
    net = create_test_network()
    assert hasattr(net, 'bus') and len(net.bus) > 0


def test_create_loads():
    net = create_test_network()
    load_idx = create_loads(net, 1, -0.006, -0.0029)
    assert load_idx == 0
    assert net.load.p_mw.iloc[0] == -0.006


def test_run_powerflow():
    net = create_test_network()
    create_loads(net, 1, -0.006, -0.0029)
    run_powerflow(net)  # No return value expected
    assert hasattr(net, 'res_bus') and len(net.res_bus) > 0
