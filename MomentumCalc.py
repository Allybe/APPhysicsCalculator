print("Momentum Calculator by Allison")

def safeGetIndex(list, index, default):
    if len(list) - 1 < index or len(list) == 0:
        return default
    return list[index]

def giveEquationSide(size, masses, velocities, isRightSide):
    equationStr =  ""

    if isRightSide:
        for x in range(size, size * 2):
            equationStr += str("(" + str(safeGetIndex(masses, x, "m")) + " • " + str(safeGetIndex(velocities, x, "v")) + ")")
            if x != ((size * 2) - 1):
                equationStr += " + "
    else:
        # left side
        for x in range(size):
            equationStr += str("(" + str(safeGetIndex(masses, x, "m")) + " • " + str(safeGetIndex(velocities, x, "v")) + ")")
            if x != (size - 1):
                equationStr += " + "

    return equationStr
    

def printEquation(size, masses, velocities):
    # (mv) = (mv)
    equationStr =  ""
    if size == 1: 
        joe = 0

    equationStr += giveEquationSide(size, masses, velocities, False)
    equationStr += " = "
    equationStr += giveEquationSide(size, masses, velocities, True)

    print(equationStr)

numOfObjects = int(input("Number of objects in system: "))

if numOfObjects < 0:
    print("Momentum: 0")

massKg = []
velocityMS = []
totalInitialMomentum = 0

printEquation(numOfObjects, massKg, velocityMS)

for x in range(numOfObjects):
    mass = int(input("Enter Mass (Kg): "))
    massKg.append(mass)
    printEquation(numOfObjects, massKg, velocityMS)

    velocity = int(input("Enter Velocity (m/s): "))
    velocityMS.append(velocity)
    printEquation(numOfObjects, massKg, velocityMS)

    totalInitialMomentum += mass * velocity
    # clear screen

print("Momentum: " + str(totalInitialMomentum))
