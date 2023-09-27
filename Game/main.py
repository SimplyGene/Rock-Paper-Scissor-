import random
def play_game():
    my_choice = input("PUT YOUR CHOICE(Rock, Paper, Scissors): ")
    options = ["Rock","Paper","Scissors"]
    comp_choice = random.choice(options)
    choices = {"my":my_choice,"comp":comp_choice}
    return choices

def check_win(my,comp):
    print(f"You chose {my} , Comp chose {comp}" )
    if my == comp:
     return "It's a tie"
    elif my == "Rock":
     if comp == "Scissors":
       return "YOU WIN!!! Rock smashes Scissors"
     else:
       return "YOU LOSE!!! Paper covers Rock"
    elif my == "Paper":
      if comp == "Rock":
       return "YOU WIN!!! Paper covers Rock"
      else:
       return "YOU LOSE!!! Scissor cuts Paper"
    elif my == "Scissors":
      if comp == "Paper":
       return "YOU WIN!!! Scissor cuts Paper"
      else:
       return "YOU LOSE!!! Rock smashes Scissors"    

choices = play_game()
result = check_win(choices["my"], choices["comp"])
print(result)