"""
pslib: Power Systems Library
Simple pandapower network builder for course project.
"""

import pandapower as pp


def create_test_network():
    """Create test power distribution network with 2 buses + transformer.

    Returns
    -------
    net : pandapower network
        Ready-to-run power flow network.
    """
    # Create empty network
    net = pp.create_empty_network()

    # Buses (simplified from your loops)
    bhv = pp.create_bus(net, vn_kv=33.0, name="Bus_HV", geodata=(-0.01, 0))
    blv = pp.create_bus(net, vn_kv=0.415, name="Bus_LV", geodata=(0, 0))

    # External grid
    pp.create_ext_grid(net, bus=bhv, vm_pu=1.02, va_degree=0, name="Grid")

    # Transformer HV→LV (FIXED with all required args)
    pp.create_transformer_from_parameters(
        net, hv_bus=bhv, lv_bus=blv,
        sn_mva=1, vn_hv_kv=33, vn_lv_kv=0.415,
        vkr_percent=0.1, vk_percent=4,
        pfe_kw=0, i0_percent=0,
        shift_degree=0, name="Main_TX"
    )

    return net


def create_loads(net, bus, p_mw, q_mvar):
    """Add residential loads to LV bus.

    Parameters
    ----------
    net : pandapower network
    bus : int, bus index
    p_mw : float, active power (negative for load)
    q_mvar : float, reactive power

    Returns
    -------
    load_idx : int
    """
    return pp.create_load(net, bus=bus, p_mw=p_mw, q_mvar=q_mvar, name="Residential")


def run_powerflow(net):
    """Run power flow calculation.

    Parameters
    ----------
    net : pandapower network

    Returns
    -------
    None on success (pandapower convention)
    """
    pp.runpp(net)


def plot_results(net):
    """Plot network with power flow results.

    Parameters
    ----------
    net : pandapower network (after run_powerflow)

    Returns
    -------
    fig : plotly figure
    """
    import pandapower.plotting as pplot
    fig = pplot.simple_plotly(net, respect_switches=False)  # FIXED: no unpack
    return fig
