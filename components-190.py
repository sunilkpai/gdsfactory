import gdsfactory as gf

c = gf.components.via_stack_with_offset(layers=((25, 0), (41, 0)), sizes=((10, 10), (10, 10)), port_orientation=180)
c.plot()