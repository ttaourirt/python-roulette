import random
import math

class Player:

    def __init__(self, number, bid):

        self.number = number
        self.bid = bid

    def checkNumber(self, number):
        
        numero = False
        while numero == False :
            self.number = input("\nSur quel numéro souhaitez vous miser (entre 0 et 49) ? : ")
            try:
                int(self.number) != False
            except ValueError:
                print("Vous etes sur ?")
            else :
                self.number = int(self.number)
                if self.number < 0 or self.number > 49:
                    print(
                        "Ce numero n'est pas possible, veuillez en choisir un autre !")
                else:
                    numero = True

    def checkBid (self, bid):

        Mise = False
        while Mise == False:
            self.bid = input("\nQuelle sera votre mise avec ce numéro ? : ")
            try:
                int(self.bid) != False
            except ValueError:
                print("Vous etes sur ?")
            else:
                self.bid = int(self.bid)
                if self.bid < 0:
                    print("Ceci est un nombre négatif !")
                else:
                    Mise = True


class Casino:

    def __init__(self, win, gain):
        self.win = win
        self.gain = gain


    def winnerNum(self, win):
        self.win = random.randrange(50)
        print("Le", self.win, " est le numero gagnant ")


    def checkGain(self, win, gain, number, bid):

        if win != number :
            if (self.win %2 == 0 and number %2 == 0) or (self.win %2 != 0 and number %2 != 0):
                self.gain = math.ceil(bid * 0.5)
                print("\n Vous avez misé sur la bonne couleur, vous gagnez {} $".format(self.gain))
            else:
                print("\n C'est perdu !")
        else:
            self.gain = bid * 3
            print("\n Bravo !!! Vous gagnez 3 fois votre mise, soit {} $".format(self.gain))

# """Nombre donne pour la roulette (a ne pas toucher)"""
number = 0

# """"somme mise (a ne pas toucher)"""
bid = 0

# """"Gain (a ne pas toucher)"""
gain = 0

# """"numero gagnant (a ne pas toucher)"""
win = 0

p = Player(number, bid)
c = Casino(gain, bid)

number = p.checkNumber(number)
bid = p.checkBid(bid)
c.winnerNum(win)
c.checkGain(win, gain, p.number, p.bid)
