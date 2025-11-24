spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix id: {spice_mix}")
spice_mix.add("Ginger")
spice_mix.add("cardamom")
spice_mix.add("lemon")
# here this set datatype is mutable, which means it can be changed first be addng Ginger,
# cardamom, lemon and the id is not changed so this datatype is mutable
print(f"Initial spice mix id: {spice_mix}")
print(f"After spice mix id: {id(spice_mix)}")
