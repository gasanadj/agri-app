import mpunga
import miwa
import majanichai
def Kiswahili() :
    print("Karibu sana agri-app")
    print("Je, wewe ni mkulima wa aina gani?")
    print("1. Mkulima wa kiwango cha juu")
    print("2. Mkulima wa kiwango cha chini")
    print("3. Mkulima wa kawaida/kujikimu")
    mkulima = int(input("Chagua nambari kulingana na kilimo unachofanya: "))
    if (mkulima == 1) :
        print("Umechagua mkulima wa kiwango cha juu")
        print("Chagua mmea utakao")
        print("1. Mpunga")
        print("2. Miwa")
        print("3. Majani chai")
        mmea = int(input("Chagua nambari kulingana na mmea utakao: "))
        if (mmea == 1) :
            mpunga.mpunga()
        elif (mmea == 2) :
            miwa.miwa()
        elif (mmea == 3) :
            majanichai.majanichai()

