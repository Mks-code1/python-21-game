import random , os, time
def clear ():
    os.system ("cls" if os.name == "nt" else "clear" )

def deal_card():
    """ترجع رقم عشوائي"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card 



def calculete_score(cards):
    """ تأخذ قائمة من الكروت وترجع لنا مجموعهم  """
    # هل يوجد بلا داك 
    if sum(cards) == 21 and len(cards) == 2:
        return 0 
    
    # هل الكروت فوق 21 وهناك كرت رقمه 11
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

 


def compare (user_score , computer_score):
    
        results = {
            "draw" :"Draw 😊 \n\n",
            "user_over" : "You went over 21, Sorry😔 \n\n",
            "computer_over" : "Computer went over 21, You win 🌟\n\n",
            "user_21" : "You won with a blackjack 🌟 \n\n",
            "computer_21" : "Sorry, computer had a blackjack 😱 \n\n",
            "user_win"  : "You win 🌟\n\n",
            "user_lose" : "You lose😢\n\n",
            
        }
        if user_score == computer_score:
             return results["draw"]
        elif user_score > 21 :
             return results["user_over"]
        elif computer_score > 21 :
             return results ["computer_over"]
        elif user_score == 21 :
              return results["user_21"]
        elif computer_score == 0 :
             return results["computer_21"]
        elif user_score == 0 :
             return results ["computer_21"]
        elif user_score > computer_score:
             return results ["user_win"]
        else:
             return results["user_lose"]
        

                  
def game ():                                              # List Comprehension ---> e.g--> numbers = [ i  for i in (range(1,11)) if i % 2 ==0  ]

    user_cards = [deal_card() for _ in range(2)]
    computer_card = [deal_card() for _ in range(2)]
    game_continue = True
    while game_continue:
          user_score = calculete_score(user_cards)
          computer_score = calculete_score(computer_card)
          print(f"\n\nYour cards are {user_score}, current score is {sum(user_cards)}")
          print(f"Compute's first card is {computer_card[0]}")
          if user_score == 0 or computer_score ==0 or user_score > 21 or computer_score >21:
               game_continue = False
          else:
               user_needs_nother_card = input ("Get another card? (Y/N): ").lower()
               if user_needs_nother_card == "y":
                    user_cards.append(deal_card())
               else:
                    game_continue= False
    while computer_score != 0 and computer_score < 17  :
         computer_card.append(deal_card())
         computer_score = calculete_score(computer_card)

    print(f"Your final hand: {user_cards} with score {user_score}") 
    print(f"Computer's final hand: {computer_card} with score {computer_score}")   
    print(compare(user_score, computer_score))
Photo= ("""
_________          _______  _       _________               _______  _        _______ 
\__   __/|\     /|(  ____ \( (    /|\__   __/|\     /|     (  ___  )( (    /|(  ____ 
   ) (   | )   ( || (    \/|  \  ( |   ) (   ( \   / )     | (   ) ||  \  ( || (    \/
   | |   | | _ | || (__    |   \ | |   | |    \ (_) /_____ | |   | ||   \ | || (__    
   | |   | |( )| ||  __)   | (\ \) |   | |     \   /(_____)| |   | || (\ \) ||  __)   
   | |   | || || || (      | | \   |   | |      ) (        | |   | || | \   || (      
   | |   | () () || (____/\| )  \  |   | |      | |        | (___) || )  \  || (____/
   )_(   (_______)(_______/|/    )_)   )_(      \_/        (_______)|/    )_)(_______/
                                                                                                                      
"""
)


clear()
while input("Choose a game to start...... \n---------\n1- Froggy\n2- Twenty one\n3- Snake\n---------\n").lower() == "twenty one":
        clear()
        print("Starting game .....")
        time.sleep(2.5)
        clear()
        # Display Logo
        print(Photo)
        game()








          # clear()
          
         



 




