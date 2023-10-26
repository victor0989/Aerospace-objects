#Maybe in the future we will control and manipulate rockets and satellites with our linux terminals with the right hardware and materials
#The Rocket class requires two drag curves, one for when the motor is off and one for when the motor is on.
>>> from rocketpy import Rocket
>>> calisto = Rocket(
...     radius=127 / 2000,
...     mass=14.426,
...     inertia=(6.321, 6.321, 0.034),
...     power_off_drag="../data/calisto/powerOffDragCurve.csv",
...     power_on_drag="../data/calisto/powerOnDragCurve.csv",
...     center_of_mass_without_motor=0,
...     coordinate_system_orientation="tail_to_nose",
... )

#CSV file
0.0, 0.0
0.1, 0.4018816
0.2, 0.38821269
0.3, 0.38150576
0.4, 0.37946785
0.5, 0.38118499
0.6, 0.38947261
0.7, 0.40604949
0.8, 0.40110651
0.9, 0.45696342
1.0, 0.62744566

#Pay special attention to the following:
#mass is the rocket’s mass, without the motor, in kg.
#inertia is defined as a tuple of the form (I11, I22, I33). Where I11 and I22 are the inertia of the mass around the perpendicular axes to the rocket, 
#and I33 is the inertia around the rocket center axis.
#Alternatively, inertia can be defined as a tuple of the form (I11, I22, I33, I12, I13, I23). 
#Where I12, I13 and I23 are the component of the inertia tensor in the directions 12, 13 and 23 respectively.
#center_of_mass_without_motor and coordinate_system_orientation are position parameters. They must be treated with care.
