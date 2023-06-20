def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissor): ")
    computer_choice = "paper" #declares comp choice is paper
    #5:50 in vid teaches functions, come back later

    choices = {"player": player_choice, "computer": computer_choice}
    return choices

choices = get_choices()
print(choices)
#stopped 6/14 at 12:33, dictionaries