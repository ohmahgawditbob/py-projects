import math

vel = float(input("Velocity (m/s): "))
mass = float(input("Mass (kg): "))

energy_kinetic = 0.5*mass*(math.pow(vel, 2))

print("The Kinetic Energy is " + str(energy_kinetic) + " Joules.")
