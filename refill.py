#Using the starting and ending values of the car's odometer and measure of fuel consumed
#calculate the no of stops one could make for refueling, whiletraveling form Banglore to GOA
#a distance of 560 km?


def mileage():
    mileage = input("what is the mileage of the car?")
    mileage = int(mileage)
    tankcapacity = input("what is the tankcapacity?")
    tankcapacity = int(tankcapacity)
    distance = 560
    distance_full = mileage*tankcapacity
    Nooftime = distance / distance_full
    value  = distance % distance_full
    actualno = (distance // distance_full) + 1
    if value == 0:
        print(Nooftime)
    else:
        print(actualno)
        
mileage()
