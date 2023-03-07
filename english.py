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


        import potatoes    
    elif (farmer == 2) :
        print("You selected Small Scale Farmer")
        print("GENERAL TIPS FOR SMALL SCALE FARMING")
        print("TIPS ")
        print("Select The Type of Crop")
        print("1. Potatoes")
        print("2. Beans")
        print("3. Maize")
        print("4. Banana")
        crop = int(input("Enter a number corresponding to the crop"))
        if (crop == 1):
            potatoes.potatoes()

        import 
    elif (farmer == 3):
        print("You selected Subsitence farming")
        print("GENERAL TIPS FOR SMALL SCALE FARMING")
        print("TIPS ")
        print("Select The Type of Crop")
        print("1. Greens")
        print("2. Cabbage")
        print("3. Cassava")
        crop = int(input("Enter a number corresponding to the crop"))
        if (crop == 1):
            greens.green()