import random

points = 10
void=1

while points > 0:
    rounds = 3
    win = 0
    loss = 0
    draw = 0
    print("You have %d points and %d void chance" %(points, void))
    pointsused = input("Enter the number of points to be used for next game: ")
    if pointsused.isdigit():
        pointsused=int(pointsused)

        if points >= pointsused and pointsused > 0:
            for i in range(rounds):
                if void == 1:
                    element1 = input("Enter 0(fire), 1(grass) or 2(water) or V (Void): ").upper()
                    element2 = random.randint(0, 2)
                    if element1.isdigit():
                        element1=int(element1)
                else:
                    element1 = input("Enter 0(fire), 1(grass) or 2(water): ")
                    element2 = random.randint(0, 2)
                    if element1.isdigit():
                        element1=int(element1)

                if element1 == element2:
                    print("Draw!")
                    draw = draw + 1

                elif element1 == 0:
                    if element2 == 1:
                        print("You are fire and computer is grass, you won!")
                        win = win + 1
                    else:
                        print("You are fire and computer is water, you lost!")
                        loss = loss + 1

                elif element1 == 1:
                    if element2 == 0:
                        print("You are grass and computer is fire, you lost!")
                        loss = loss + 1
                    else:
                        print("You are grass and computer is water, you won!")
                        win = win + 1

                elif element1 == 2:
                    if element2 ==0:
                        print("You are water and computer is fire, you won!")
                        win = win + 1
                    else:
                        print("You are water and computer is grass, you lost!")
                        loss = loss + 1

                elif element1 == 'V':
                    void=0
                    win=0
                    loss=0
                    draw=0
                    break

                else:
                    print("You entered an invalid option, you lost!")
                    loss = loss + 1

            if win == 0 and loss == 0 and draw == 0:
                print("Your game is void.\n")
            else:
                print("You have %d win, %d loss and %d draw " % (win, loss, draw))
                if win > loss:
                     print("You won the game with %d points added.\n" % pointsused)
                     points = points + pointsused
                elif loss > win:
                     print("You lost the game with %d points deducted.\n" % pointsused)
                     points = points - pointsused
                else:
                    print("Tie! Your points remain unchanged.\n")


        elif pointsused > points and pointsused > 0:
            print("You do not have enough points.")


        elif pointsused == -1:
            quit()

        else:
            print("Invalid number of points.")

    else:
        print("Invalid Input")

else:
    print("You have no more points. End of game!")
