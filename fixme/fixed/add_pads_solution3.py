"""
This is the best solution.
Be aware that sometimes you need to flip the ports for the automatic get_bundle algorithm to work well.

"""


import pp

c = pp.Component("mzi_with_pads_sample_with_corners")
mzi = pp.components.mzi2x2(with_elec_connections=True)
pads = pp.components.pad_array(n=3, port_list=["S"])
p = c << pads
mzir = c << mzi
p.move((-150, 150))

routes = pp.routing.get_bundle(
    ports2=p.ports,
    ports1=mzir.get_ports_list(port_type="dc"),
    waveguide="metal_routing",
    bend_factory=pp.components.wire_corner,
)
for route in routes:
    c.add(route.references)
c.show()