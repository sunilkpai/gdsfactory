import pp

if __name__ == "__main__":
    c = pp.components.straight(cross_section_settings=pp.TECH.waveguide.strip)
    c.show()