import random
Rock= '''
          _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)

'''
Paper='''
          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)
'''
Scissors='''
          _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)
'''
game_image =[Rock, Paper, Scissors, "NO again"]

while True:
    user_choice= int(input("what do you choose? type 0 for rock, 1 for paper, 2 for scissors, 3 for NO again\n"))
    
    if user_choice == 3:
        print("Thank you for play with me")
        break
    elif user_choice >=4 or user_choice<0:
        print("you typed an invalid number, You lose!")
    else:
        print(game_image[user_choice])
        computer_choice= random.randint(0,2)
        print("computer chose:")
        print(game_image[computer_choice])
        if user_choice==0 and computer_choice==2:
            print("you win!")
        elif computer_choice==0 and user_choice==2:
            print("you lose!")
        elif computer_choice> user_choice:
            print("you lose!")
        elif user_choice> computer_choice:
            print("you win!")
        elif computer_choice== user_choice:
            print(" it's a draw")
            
            
        
        