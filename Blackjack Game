import random
import art
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and len(cards) == 2:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(u_score, c_score):
    if u_score==c_score:
        return "Draw"
    elif c_score==0:
        return "Lose. Opponent has Blackjack"
    elif u_score==0:
        return "Win with a Blackjack"
    elif u_score>21:
        return "You went over. You Lose"
    elif c_score>21:
        return "Opponent went over. You Win"
    elif u_score>c_score:
        return "You Win"
    else:
        return "You Lose"
def play_game():
    print(art.logo)
    user_cards=[]
    computer_cards=[]
    computer_score=-1
    user_score=-1
    a=False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not a:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your Cards:{user_cards},current score:{user_cards}, current score:{user_score}")
        print(f"Computer's First card :{computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            a=True
        else:
            b=input("Type 'y' to get another card, type 'n' to pass")
            if b=="y":
                user_cards.append(deal_card())
            else:
                a=True
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    print(f"Your Final hand:{user_cards},current score:{user_cards}, final score:{user_score}")
    print(f"Computer's Final hand:{computer_cards},final score:{computer_score}")
    print(compare(user_score,computer_score))
while input("Do you want to play blackjack?(y/n)")=="y":
    print("\n"*20)
    play_game()
