import pytest
import time
import pandas as pd
import numpy as np
import pandapower as pp
from pslib.network import (
    create_test_network, create_loads, run_powerflow,
    plot_results, create_loads_vectorized
)


def test_network_creation():
    net = create_test_network()
    assert hasattr(net, 'bus') and len(net.bus) > 0


def test_create_loads():
    net = create_test_network()
    load_idx = create_loads(net, 1, -0.006, -0.0029)
    assert load_idx == 1
    assert len(net.load) == 2


def test_run_powerflow():
    net = create_test_network()
    create_loads(net, 1, -0.006, -0.0029)
    run_powerflow(net)  # No return value expected
    assert hasattr(net, 'res_bus') and len(net.res_bus) > 0


def test_plot_results():
    net = create_test_network()
    create_loads(net, 1, -0.006, -0.0029)
    run_powerflow(net)
    fig = plot_results(net)
    assert fig is not None


# testing vectorized function


def test_vectorization_speed():
    """Benchmark scalar vs vectorized (1000 loads on bus 1 only)."""
    buses = np.array([1] * 1000)  # FIX: Only use bus 1
    p_mw = np.random.uniform(-0.01, -0.001, 1000)
    q_mvar = p_mw * 0.5

    # Scalar baseline (SLOW)
    net_scalar = create_test_network()
    start = time.time()
    for b, p, q in zip(buses, p_mw, q_mvar):
        pp.create_load(net_scalar, bus=b, p_mw=p, q_mvar=q)
    scalar_time = time.time() - start

    # Vectorized (FAST)
    net_vec = create_test_network()
    start = time.time()
    create_loads_vectorized(net_vec, buses, p_mw, q_mvar)
    vectorized_time = time.time() - start

    speedup = scalar_time / vectorized_time
    print(f"🔥 1000 LOADS BENCHMARK (Bus 1):")
    print(f"Scalar loop:    {scalar_time:.3f}s")
    print(f"Vectorized:     {vectorized_time:.3f}s")
    print(f"Speedup:      {speedup:.0f}x FASTER! 🚀")

    assert vectorized_time < scalar_time * 0.8  # At least 25% faster
