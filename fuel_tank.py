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
