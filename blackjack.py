import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    card = random.choice (cards)
    return card     #return random values from cards

def calculate_score(cards):   #function to calculate score , gvs sum , removal of 11 add 1
    if sum(cards) ==21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,comp_score):  
    if user_score > 21 and comp_score > 21:
        return "You went over. You lose." #function to compare user n computer scores
    if user_score == comp_score:
        return "Its a draw."
    elif comp_score == 0 :
        return "you loss. Computer has blackjack."
    elif user_score == 0:
        return "you win with a blackjack."
    elif user_score>21:
        return "You went over, you lose."
    elif comp_score>21:
        return "Computer went over 21. You win."
    elif user_score> comp_score:
        return "You win."
    else:
        return "Computer Wins."


    

user_cards = []
computer_cards = []   
game_over = False

for _ in range(2):     #wd this getting 2 cards for user n comp
    user_cards.append (deal_card())
    computer_cards.append(deal_card())

#let user play
while game_over == False:

    user_score = calculate_score(user_cards)
    comp_score = calculate_score(computer_cards)

    print (f"Your cards{user_cards} and your score {user_score}")
    print (f"Computer's cards {computer_cards} and computer's score {comp_score}")

    if user_score ==0 or user_score>21 or comp_score==0: #checking if game ends in1st phase
        game_over = True
    else:
        asking_user= (input("Do you want to get another card? type 'y' for yes or 'n' for no.\n"))
        if asking_user == "y":
            user_cards.append(deal_card())
            print (user_cards)
        else:
            game_over = True

#let computer play
while comp_score< 17 and comp_score!=0:
    computer_cards.append(deal_card())
    comp_score = calculate_score(computer_cards)
    print (f"computer cards {computer_cards} and computer score {comp_score}")

print (compare(user_score,comp_score))