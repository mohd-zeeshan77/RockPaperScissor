import random

print("winning rules of the rock,paper,scissor,game,as follows:\n" + "rock vs paper\t\t=>\t\tpaper wins\n" + "rock vs "
                                                                                                             "scissor"
                                                                                                             "\t\t"
                                                                                                             "=>\t"
                                                                                                             "\trock"
                                                                                                             "wins\n" + "paper vs scissor\t=>\t\tscissor wins\n")
while True:
    print("\nenter the choice\n1. rock\n2. paper\n3. scissor\n")
    choice = int(input("user turn:"))
    while (choice > 3) or (choice < 1):
        choice = int(input("enter the valid input:"))
    if choice == 1:
        choice_name = 'rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
    print(f"\nuser choice is {choice_name}")
    print("\nNow computer turn..........")
    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
    print(f"computer choice is {comp_choice_name}")
    print(f"{choice_name} V/s {comp_choice_name}")
    if (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        print("paper wins=>", end="")
        result = "paper"
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print("rock wins=>", end="")
        result = "rock"
    else:
        print("scissor wins=>", end="")
        result = "scissor"
    if result == choice_name:
        print("\n\n<==user wims==>")
    else:
        print("<==\n\ncomputer wins==>")
    print("do you want to play again?(Y/N")
    ans = input()
    ans = str(ans)
    if ans == 'n' or ans == 'N':
        break
print("\n\n Thanks for playing")
