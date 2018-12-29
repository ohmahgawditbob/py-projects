import math

energy_kinetic = float(input("Kinetic Energy (J): "))
mass = float(input("Mass (kg): "))

vel = math.sqrt((2*energy_kinetic)/mass)

print("The Velocity is " + str(vel) + " m/s.")
