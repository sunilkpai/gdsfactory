import gdsfactory as gf

c = gf.components.straight(length=10.0, npoints=2, with_bbox=False)
c.plot()