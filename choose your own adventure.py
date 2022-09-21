name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("Choose a setting. Forest, Desert, Sea or City ").lower()
# Desert World
if answer == "desert":
    answer = input("You are in the Desert and come a across a Desert Temple. Type enter to enter the desert temple or walk to walk around it?" ).lower()

    if answer == "enter":
            answer = input("You hear spooky noises from a door ahead. It has unknown hyroglifics on it. Enter the door or turn right? Type enter to enter or right to turn right. ").lower()

            if answer == "enter":
                answer = input("You step on a trap and knives fall down from the ceiling. Attempt to run forward and dodge the knives or exit the room. Type run to run and exit to exit the room. ").lower()

                if answer == "run":
                    answer = input("Some knives cut you in your arms and legs. But a large knife lands on your toe as you run to the middle of the room. Around you, there are mummys and the only thing you can do is unrap a mummy and use it to bandage your foot. Type unrap to unrap the mummy or bleed to let your foot bleed. ").lower()

                    if answer == "unrap": # last desert loop
                        answer = input("You try to unrap a mummy and another trap is realeased. The mummy starts to wake up and attack you. Type knife to use the a knife to defend yourself or run to run away. ").lower()

                elif answer == "exit":
                    answer = input("You run out of the room and wonder deeper into the temple. You see a bright light to your left and a dark, scary room to your right. Type left or right. ").lower()
                
                else:
                    print("Not a valid option")

            elif answer == "right":
                answer = input("You turn left and hear voices in the distance. Type follow to follow the voices or turn to turn around?  ").lower()
                
                if answer == "folllow":
                    answer = input("You follow the voices deeper into the temple and find a group of people arguing over a map, which is suppoed to lead to burried tresure. Type stay to find out more about the map, or leave to leave. ").lower()
            else:
                print("Not a valid option")


    elif answer == "walk":
        answer = input("You see a man on a cammel in the distance. Type Approach to approach the man. Type walk to walk away. ").lower()

        if answer == "approach":
            answer = input("The man turns out to be a bandit. He threatens to steal all your valuables. Type run to run away or give to give him all your possesions. ").lower()

            if answer == "run":
                answer = input("You trip on the sand...  ")

    else:
        print("Not a valid option. You lose.")
# Forest World
elif answer == "forest":
    answer = input("You are walking in a forest and hear a scream from ahead. Type left walk toward the scream or turn to right to go in a different direction. ").lower()
    
    if answer == "left":
        answer = input("You see a girl crying on the floor as she just fell out of a tree. She dosn't see you, but you can see she has a bag of resources.Type steal to take her stuff or help to help her up." ).lower()
    
        if answer == "steal":
            answer = input("You try and steal her stuff but she pulls out a knife and scraches you accros the face. Type fight to fight back or run to run away. ").lower()

            if answer == "fight":
                answer = input("She tries cut you again, but you block her hand. You hit her across the face, then she stabs you in the leg. She takes her bag and runs into the distance. Type follow to get up and follow her or heal to try and find something to bandage your leg. ").lower()

                if answer == "follow":
                    answer = input("You follow the girl, but she is running too fast. Your leg is loosing too much blood. Type shout to call for help, or type bandage to find something to bandage your leg. ").lower()

                    if answer == "shout":
                        answer = input("")

                    elif answer == "bandage":
                        answer = input("")

                elif answer == "heal":
                    answer = input("")

            elif answer == "run":
                answer = input("")

            else:
                print("Not a valid option. You lose.")

        elif answer == "help":
            answer = input("You help her up and she thanks you. She offers you some of her food, but asks if you want to accompnay her on her journey to find 'antient treasure.' Type stay to stay with the girl or leave to leave her. ").lower()

        else:
            print("Not a valid option. You lose.")

    elif answer == "right":
        answer = input("You keep walking and it's getting dark. You need food and shelter. Type food to focus on gettign food, or shelter to focus on finding shelter. ").lower()

    else:
        print("Not a valid option. You lose.")


    
# Sea world
elif answer == "sea":
    answer = input("You are on a boat in the middle of the sea. There is an island in the distance. The waves are powerful. You can swim or row to the island. Type swim to swim to the island or row to row to the isand. ").lower()

    if answer == "swim":
        answer = input("You jump into the sea and try to swim through the waves. The waves are too powerful, you boat is smashed and you are crushed underwater. You black out. You wake up on the island. The island is massive. Type explore to explore the island or shelter to find shelter. ").lower()

        if answer == "explore":
            answer = input("")
    
    elif answer == "row":
        answer = input("You try to row the boat to the island ")



# City world
elif answer == "city":
    answer = input("You are in an abandoned city, with little people. You are hungry and about to eat the last fo your fruit bar. You see a stray, starving dog who can't even walk. Type help to give the dog some of your food or eat to eat it all yourself. ").lower()

else: 
    print("Not a valid option. You lose.")