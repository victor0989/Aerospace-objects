>>> from math import exp
>>> from rocketpy import Fluid, LiquidMotor, CylindricalTank, MassFlowRateBasedTank
>>> from rocketpy import Fluid, CylindricalTank, MassFlowRateBasedTank, HybridMotor
>>> oxider_liq = Fluid(name="N20_1", density=1220)
>>> print(oxider_liq)
Fluid: N20_1
>>> oxizer_gas = Fluid(name="N20_g", density=1.9277)
>>> tank_shape = CylindricalTank(115 / 2000, 0.705)
>>> oxider_liq = Fluid(name="N20_1", density=1220)
>>> print(oxider_liq)
Fluid: N20_1
>>> oxider_gas = Fluid(name="N20_g", density=1.9277)
>>> fuel_liq = Fluid(name="ethanol_l", density=789)
>>> fuel_gas = Fluid(name="ethanol_g", density=789)
>>> tanks_shape = CylindricalTank(radius = 0.1, height = 1, spherical_caps = True)
>>> oxizer_tank = MassFlowRateBasedTank(
...     name="oxidizer tank",
...     geometry=tanks_shape,
...     flux_time=5,
...     initial_liquid_mass=32,
...     initial_gas_mass=0.1,
...     liquid_mass_flow_rate_in=0,
...     liquid_mass_flow_rate_out=lambda t: 32 / 3 * exp(-0.25 * t),
...     gas_mass_flow_rate_in=0,
...     gas_mass_flow_rate_out=0,
...     liquid=oxidizer_liq,
...     gas=oxidizer_gas,
... )

>>> example_hybrid = HybridMotor(
...     thrust_source=lambda t: 2000 - (2000 - 1400) / 5.2 * t,
...     dry_mass=2,
...     dry_inertia=(0.125, 0.125, 0.002),
...     nozzle_radius=63.36 / 2000,
...     grain_number=4,
...     grain_separation=0,
...     grain_outer_radius=0.0575,
...     grain_inner_radius=0.025,
... )
