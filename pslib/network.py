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
        pfe_kw=0, i0_percent=0,  # ← These were missing!
        shift_degree=0, name="Main_TX"
    )

    return net
