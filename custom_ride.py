ride = input("What type of transportation do you want to ride (bike/car): ")
if ride == "bike":
    type = input("What type of bike do you want to ride?(electric/motorbike): ")
    if type == "electric":
        print("you ride is a electric bike")
    if type == "motorbike":
        print("Your ride is a motorbike")
if ride == "car":
    type = input("What type of car do you want to ride?(electric/non electric): ")
    if type == "electric":
        print("you ride is a electric car")
    if type == "non electric":
        print("Your ride is a non electric car")
        
