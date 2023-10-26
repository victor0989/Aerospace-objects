>>> example_liquid = LiquidMotor(
...     thrust_source=lambda t: 4000 - 100 * t**2,
...     dry_mass=2,
...     dry_inertia=(0.125, 0.125, 0.002),
...     nozzle_radius=0.15,
...     center_of_dry_mass_position=0.584,
...     nozzle_position=0,
...     burn_time=5,
...     coordinate_system_orientation="nozzle_to_combustion_chamber",
... )
>>> example_liquid.add_tank(tank=oxidizer_tank, position=0.6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'oxidizer_tank' is not defined
>>> example_liquid.add_tank(tank=fuel_tank, position=1.8)
