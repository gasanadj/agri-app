import mpunga
import miwa
import majanichai
import viazi
import maharage
import mahindi
import ndizi
import aina_mkulima
def Kiswahili() :
    while True: 
        print("Karibu sana agri-app")
        print("Je, wewe ni mkulima wa aina gani?")
        aina_mkulima.mkulimaaina()
        aina_mkulima.kutoka()
        mkulima = int(input("Chagua nambari kulingana na kilimo unachofanya: "))
        if (mkulima == 0):
            break
        elif (mkulima == 1) :
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
        elif (mkulima == 2):
            print("Umechagua mkulima wa kiwango cha chini")
            print("Chagua mmea utakao")
            print("1. Viazi")
            print("2.Maharage")
            print("3.Mahindi")
            print("4.Ndizi")
            mmea = int(input("Chagua nambari kulingana na mmea utakao: "))
            if (mmea == 1):
                viazi.viazi()
            elif (mmea == 2):
                maharage.maharage()
            elif (mmea == 3):
                mahindi.mahindi()
            elif (mmea == 4):
                ndizi.ndizi() 
        