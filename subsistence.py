print("you selected subsistence farming")
print("general tips")
        #select crop
print("select your crop of choice")
print("1.GREENS")
print("2.CABBAGE")
print("3.CASSAVA")
choice=int(input("Enter crop of choice: "))
#GREENS
if choice==1:
            print("You selected Greens")
            print("1.Best farming practices")
            print("2.Best fertilizers and insecticides")
            print("3.best harvesting and storage practices")
            info=int(input("Select choice of info: "))
            if info==1:
                print("best farming practices")
                print("*info*")
            elif info==2:
                print("best ferstilizers and insecticides")
                print("*info*")
            elif info==3:
                print("best harvesting and storage practices")
                print("*info*")
            else:
                print("invalid input")

#CABBAGE   
elif choice==2:
            print("You selected Cabbage ")
            print("1.Best farming practices")
            print("2.Best fertilizers and insecticides")
            print("3.best harvesting and storage practices")
            info=int(input("Select choice of info: "))
            if info==1:
                print("best farming practices")
                print("*info*")
            elif info==2:
                print("best fers\tilizers and insecticides")
                print("*info*")
            elif info==3:
                print("best harvesting and storage practices")
                print("*info*")
            else:
                print("invalid input")

#CASSAVA    
elif choice==3:
            print("You selected Cassava")
            print("1.Best farming practices")
            print("2.Best fertilizers and insecticides")
            print("3.best harvesting and storage practices")
            info=int(input("Select choice of info: "))
            if info==1:
                print("best farming practices")
                print("*info*")
            elif info==2:
                print("best fertilizers and insecticides")
                print("*info*")
            elif info==3:
                print("best harvesting and storage practices")
                print("*info*")
            else:
                print("invalid input")
else:
      print("INVALID INPUT")                
