import gdsfactory as gf

c = gf.components.grating_coupler_rectangular_arbitrary(gaps=(0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2), widths=(0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5), wg_width=0.5, width_grating=11.0, length_taper=150.0, layer=(1, 0), polarization='te', wavelength=1.55, layer_slab=(2, 0), slab_xmin=-1.0, slab_offset=1.0, fiber_marker_layer=(203, 0))
c.plot()