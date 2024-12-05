import random
Roulette = ["Red","Black"]
Alive = True
Prince = ()
bet = ()
Loss = 0
Money = 50
Kidneys = 2
House = 1
Kids = 3
IPA = 100000
Soul = 1
Bet = ()
TaxRate = 0.05
HasWife = True
card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] 
deck = [(card, category) for category in card_categories for card in cards_list]
while Alive == True:
    if Money > 1000000:
        print("You have ascended")
        Alive = False
        Deity = True
    Chosen = input("Red or Black: ")
    Round = random.choice(Roulette)
    if Chosen == Round:
        Money = Money * 2
        print(f"YOU WON ${Money}!!")
    else:
        Money = 0
        print("LOSE!!!!")
        print(f"You have {Money}")
    if Money <= 0:
        if House > 0 and HasWife == True:
            print("You can sell your house")
        else:
            Loss == Loss + 1
        if Kidneys > 1:
            print("You can sell a Kidney")
        else:
            Loss == Loss + 1
        if Kids > 0 and HasWife == True:
            print("You can sell a Kid")
        else:
            Loss == Loss + 1
        if Soul > 0:
            print("You can sell your soul")
        else:
            Loss == Loss + 1
        if IPA > 0:
            print("You can cash in your IPA")
        else:
            Loss == Loss + 1
        if Money == 0 and Alive == True:
            print("Which to sell??? (if you cant type 'Nothing')")
            Selling = input()
            if Selling == "House" and HasWife == True:
                Money = Money + 200000
                print("Your wife left you")
                HasWife = False
                Money = Money/2
            elif Selling == "Kidney":
                Money = Money + 70000
                Prince == random.randint(1,2)
                Kidneys = Kidneys - 1
                if Prince == 1:
                    Money = Money + 100000
            elif Selling == "Kid" and HasWife == True:
                Money = Money + 25000
                print("Your wife left you")
                HasWife = False
                Money = Money/2
                Kids = Kids - 1
            elif Selling == "Soul" and Soul > 0:
                Money = Money + 500000
                Soul = Soul - 1
            elif Selling == "IPA" and IPA > 0:
                MoneyIN = input(f"You have {IPA} how much would you like to take?")
                if int(MoneyIN) > int(IPA):
                    print("You dont have that much bozo")
                else:
                    Money = int(MoneyIN) + int(Money)
                IPA = int(IPA) - int(MoneyIN)
            elif Selling == "Nothing":
                Alive = False
                print("You died")
                break
