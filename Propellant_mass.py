#1/Propellant mass

#2/Mass flow rate

#3/Motor center of mass

#4/Inertial moment

#5/Exhaust velocity
#example_liquid.propellant_mass.plot(0, 5)

>>> fuel_tank = MassFlowRateBasedTank(name="fuel tank",geometry=tanks_shape,
...     flux_time=5,
...     initial_liquid_mass=21,
...     initial_gas_mass=0.01,
...     liquid_mass_flow_rate_in=0,
...     liquid_mass_flow_rate_out=lambda t: 21 / 3 * exp(-0.25 * t),
...     gas_mass_flow_rate_in=0,
...     gas_mass_flow_rate_out=lambda t: 0.01 / 3 * exp(-0.25 * t),
...     liquid=fuel_liq,
...     gas=fuel_gas,
... )
>>> print(fuel_tank)
<rocketpy.motors.tank.MassFlowRateBasedTank object at 0x799b495dcfd0>
>>> #dry_inertia
>>> liquid = LiquidMotor(
...     thrust_source=lambda t: 4000 - 100 * t**2,
...     dry_mass=2,
...     dry_inertia=(0.125, 0.125, 0.002),
...     nozzle_radius=0.15,
...     burn_time=5,
...     coordinate_system_orientation="nozzle_to_rombustion_chamber",
... )
missing 1 required positional argument: 'center_of_dry_mass_position'
