import gdsfactory as gf

c = gf.components.version_stamp(labels=('demo_label',), with_qr_code=False, layer=(1, 0), pixel_size=1, version='5.1.2', text_size=10)
c.plot()