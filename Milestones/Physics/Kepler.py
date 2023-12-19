########### KEPLER EQUATION ###############

from numpy import array


# A function is created to define Kepler force in orbits
def F_Kepler(U, t):
    x, y, vx, vy = U[0], U[1], U[2], U[3]
    mr = (x**2 + y**2)**(3/2)

    if mr == 0:
        # To handle the case where mr is zero to avoid division by zero
        return array([vx, vy, 0.0, 0.0])
    else:
        return array([vx, vy, -x / mr, -y / mr])