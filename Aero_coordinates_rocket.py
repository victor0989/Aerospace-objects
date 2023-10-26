#The airfoil parameter can be None, in which case fins will be treated as flat plates. Otherwise, it can be a tuple of the form (path, units).
#The path is the path to the airfoil CSV file in which the first column is the angle of attack and the second column is the lift coefficient.
#The units is the unit of the first column of the CSV file. It can be either "radians" or "degrees".
nose_cone = calisto.add_nose(
    length=0.55829, kind="von karman", position=1.278
)

fin_set = calisto.add_trapezoidal_fins(
    n=4,
    root_chord=0.120,
    tip_chord=0.060,
    span=0.110,
    position=-1.04956,
    cant_angle=0.5,
    airfoil=("../data/calisto/NACA0012-radians.csv","radians"),
)

tail = calisto.add_tail(
    top_radius=0.0635, bottom_radius=0.0435, length=0.060, position=-1.194656
)

#AIR-FOIL CSV
0.0,          0.0
0.017453293,  0.11
0.034906585,  0.22
0.052359878,  0.33
0.06981317,   0.44
0.087266463,  0.55
0.104719755,  0.66
0.122173048,  0.746
0.13962634,   0.8274
0.157079633,  0.8527

#PARACHUTES-For more information on adding parachutes, see rocketpy.Rocket.add_parachute
main = calisto.add_parachute(
    name="Main",
    cd_s=10.0,
    trigger=800,
    sampling_rate=105,
    lag=1.5,
    noise=(0, 8.3, 0.5),
)

drogue = calisto.add_parachute(
    name="Drogue",
    cd_s=1.0,
    trigger="apogee",
    sampling_rate=105,
    lag=1.5,
    noise=(0, 8.3, 0.5),
)
0.174532925,  0.1325
0.191986218,  0.1095
0.20943951,   0.1533

#p: pressure considering parachute noise signal.
#h: height above ground level considering parachute noise signal.
#y: state vector in the from [x, y, z, vx, vy, vz, e0, e1, e2, e3, w1, w2, w3].
def drogue_trigger(p, h, y):

    # activate drogue when vz < 0 m/s.
    return True if y[5] < 0 else False


def main_trigger(p, h, y):

    # activate main when vz < 0 m/s and z < 800 m
    return True if y[5] < 0 and h < 800 else False
