print("Hello, I am a huge Soccer/Football Fan, based in the US.")
print("Pick a team and type its acronym in")
print("Algeria ALG")
print("Argentina ARG")
print("Australia AUS")
print("Austria AUT")
print("Belguim BEL")
print("Bosnia and Heregovina BIH")
print("Brazil BRA")
print("Canada CAN")
print("Cape Verde CPV")

nation = input("Give me an acronym: ")

if nation == "ALG":
    # Removed the print() from inside input() and fixed the indentation
    playerType = input("Pick a Player position: Goal Keeper? - Type G, Forward? - Type F, Midfielders?-Type M, Defenders? - Type D: ")
    
    if playerType == "G":
        print("This is a W")
    elif playerType == "F":
        print("This is a F")
    elif playerType == "M":
        print("This is a M")
    elif playerType == "D":
        print("This is a D")