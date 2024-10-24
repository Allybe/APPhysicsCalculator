print("Momentum Calculator by Allison")

user_input = int(input("Number of objects in system: "))

if user_input == 0:
    print("Momentum: 0")

totalInitialMomentum = 0

for x in range(user_input):
    mass = int(input("Enter Mass (Kg): "))
    velocity = int(input("Enter Velocity (m/s): "))

    totalMomentum = mass * velocity
    # clear screen

print("Momentum: " + str(totalMomentum))



