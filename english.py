import rice
def english() :
    print("Welcome to agri-app")
    print("What type of farmer are you")
    print("1. Large-Scale")
    print("2. Small-Scale")
    print("3. Subsistence")
    farmer = int (input("Enter a number corresponding to your type"))
    if (farmer == 1) :
        print("You selected Large Scale Farmer")
        print("Select The Type of Crop")
        print("1. Rice")
        print("2. Sugarcane")
        print("3. Tea")
        crop = int(input("Enter a number corresponding to the crop"))
        if (crop == 1) :
            rice.rice()
            
    