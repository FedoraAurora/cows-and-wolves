import random

def main():
    #base game variables
    turn = 0
    turnEnd = 0 #0 - false, 1 - true
    actionDone = 0 #same as above

    #animals
    cows = 5
    breedCows = 0 #cows that sex with each other to make more cows next day
    wolf = 2

    #resources
    wheat = 5
    wheatCollect = 0
    wheatGrowing = 3
    meat = 1

    while cows > 0 or breedCows > 0:
        actionDone = 0
        turnEnd = 0
        if breedCows > 0:
            cows = cows + (breedCows * 2) #sex-ing the cows together
            breedCows = 0 #resetting the amount
        turn = turn + 1
        print("\nDay:", turn)

        if turn % 4 == 0: #Every 4 days, a single wheat crop starts growing
            wheatGrowing = wheatGrowing + 1

        if wheatGrowing > 0 and turn % 2 == 0: #Every 2 days a wheat crop grows up and a new wolf appears
            wheatCollect = wheatCollect + 1
            wheatGrowing = wheatGrowing - 1
            wolf = wolf + 1

        print("\nYou have", cows, "cows,", wheat, "wheat and", meat, "meat")
        print("\nWhat do you wanna do? (Type help for actions)")

        while turnEnd == 0:
            action = input()

            if action == "help":
                print("\nhelp - see all commands \n"

                "\nShort Actions: These can be used as much as you want within a single day\n"
                "check (field, wolves) - check how much wheat is growing and can be collected, check how many wolves there are\n"
                "dayinf - print the start of day info again\n"

                "\nDay Actions: These take an entire day\n"
                "feed (cows, wolves) - feed cows or wolves\n"
                "harvest (wheat, meat) - wheat grows every 2 days, meat can be harvested by killing a cow\n"
                "skip - in case if you ever need to skip a day\n")

            #Short Actions
            if action == "check field":
                print("You can harvest", wheatCollect, "wheat. You currently have", wheatGrowing, "wheat growing")
            if action == "check wolves":
                print("There are currently", wolf, "wolves ready to kill your cows")
            
            if action == "dayinf":
                print("Day:", turn)
                print("You have", cows, "cows,", wheat, "wheat and", meat, "meat")
                print("What do you wanna do? (Type help for actions)")

            #Day Actions
            if action == "skip":
                turnEnd = 1
            if action == "harvest wheat":
                if wheatCollect > 0:
                    wheat = wheat + wheatCollect
                    wheatCollect = 0
                    turnEnd = 1
                else:
                    print("There is no wheat to collect! Try again tomorrow")

            if action == "harvest meat":
                while actionDone == 0:

                    print("How many cows do you wanna turn into meat?")
                    killCows = int(input())

                    if killCows != cows:
                            if cows > killCows and killCows > 0:
                                cows = cows - killCows
                                meat = meat + killCows
                                actionDone = 1
                                turnEnd = 1
                            else:
                                print("Insufficient amount of cows!")
                    else:
                        print("You can not kill all of your cows!")

            if action == "feed cows":
                if wheat > 0:
                    while actionDone == 0:
                        
                        print("How many cows do you wanna feed?")
                        feedCows = int(input())

                        if wheat >= feedCows and feedCows > 0:
                            if cows >= feedCows:
                                cows = cows - feedCows
                                breedCows = breedCows + feedCows
                                wheat = wheat - feedCows
                                actionDone = 1
                                turnEnd = 1
                            else:
                                print("You don't have that many cows!")
                        else:
                            print("You don't have enough wheat!")
                else:
                    print("No wheat!")

            if action == "feed wolves":
                if meat > 0:
                    if wolf > 0:
                        while actionDone == 0:

                            print("How many wolves do you wanna feed?")
                            feedWolf = int(input())

                            if meat >= feedWolf and feedWolf > 0:
                                if wolf >= feedWolf:
                                    wolf = wolf - feedWolf
                                    meat = meat - feedWolf
                                    actionDone = 1
                                    turnEnd = 1
                                else:
                                    print("There are not that many wolves out there!")
                            else:
                                print("Insufficient amount of meat!")

                    else:
                        print("No wolves to feed!")            
                else:
                    print("No meat!")
        else:
            #Wolf hunt
            if turn != 0:
                hunt = random.randrange(1,wolf + 3)
                if wolf > hunt:
                    cows = cows - wolf
    else:
        print("You lost all your cows! Your score is", turn, "!")

if __name__ == '__main__':
    main()