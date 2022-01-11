#by Derek Neil
#Really basic blackjack ish game to understand functions
from random import randint
PlayerValue = 0
DealerValue = 0
Card1 = 0
Card2 = 0
ExtraCard1 = 0
ExtraCard2 = 0
Dealer1 = 0
Dealer2 = 0




def Playerdraw():
    global PlayerValue
    global Card1
    global Card2
    UserCard1 = randint(2, 10)
    UserCard2 = randint(2,11)
    PlayerValue = int(UserCard1)+int(UserCard2)
    Card1 = int(UserCard1)
    Card2 = int(UserCard2)

def Dealerdraw():
    global DealerValue
    global Dealer1
    global Dealer2
    DealerCard1 = randint(2, 10)
    DealerCard2 = randint(2,11)
    DealerValue = int(DealerCard1)+int(DealerCard2)
    Dealer1 = int(DealerCard1)
    Dealer2 = int(DealerCard2)


def hit1():
    global PlayerValue
    global ExtraCard1
    UserCardHit = randint(1,10)
    PlayerValue = int(UserCardHit) + PlayerValue
    ExtraCard1 = int(UserCardHit)
    print("New card: " + str(ExtraCard1) + " | Total: " + str(PlayerValue))
    CheckScore()

def hit2():
    global PlayerValue
    global ExtraCard2
    UserCardHit = randint(1,10)
    PlayerValue = int(UserCardHit) + PlayerValue
    ExtraCard2 = int(UserCardHit)
    print("New card: " + str(ExtraCard2) + " | Total: " + str(PlayerValue))
    CheckScore()

def Check4FirstHit():
    global ExtraCard1
    if(ExtraCard1 != 0):
        hit2()
    else:
        hit1()
def PlayerStay():
    global PlayerValue
    global DealerValue
    if(PlayerValue > DealerValue):
        print("You Win!  Your Score: " + str(PlayerValue) + " | Dealers Score: " + str(DealerValue))
    else:
        Print("Dealer Wins! Your Score: " + str(PlayerValue) + " | Dealers Score: " + str(DealerValue))


def Game():
    UserImput = input("Command:")
    if (UserImput == "Draw" or UserImput == "draw" or UserImput == "Deal" or UserImput == "deal"):
        Playerdraw()
        Dealerdraw()
        print("Card One: " + str(Card1) + " | Card Two: " + str(Card2) + " | Total Hand: " +str(PlayerValue) + " | Dealer Showing: " + str(Dealer1))
        CheckScore()
    elif(UserImput == "Hit"):
        Check4FirstHit()
    else:
        PlayerStay()

def CheckScore():
    global PlayerValue
    if(PlayerValue <= 20):
        Game()
    elif(PlayerValue == 21):
        print("Blackjack!!")
    else:
        print("You busted!")
#Game Start
while(PlayerValue<21):
    Game()