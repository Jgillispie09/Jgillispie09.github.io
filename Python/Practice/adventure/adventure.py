import time
import random
name = input("Enter your name: ")
print("Welcome, " + name + "!" + " Adventure awaits!")
time.sleep(1)
print("You awake in a dark, damp cave. Darkness surrounds all sides of you except ahead you can see a small pinhole of light.")
time.sleep(1)
print("What would you like to do?\n 1. Go towards the light \n 2. Search the darkness")
time.sleep(1)
answer = input("Choose an option: \n")
if answer == "1":
    print("You cautiously approach the light source. As you get closer, the light begins to grow and grow until you find yourself in a vast open meadow.\nThe verdant grass that surrounds you puts your mind at ease, as if to tell you this place is safe, this place is sacred.")
    time.sleep(1)
    print("To your left you see a vast forest rich with folliage. The sound of birds chirping can be heard coming from deep within the forest.")
    time.sleep(1)
    print("To your right, a cobblestone trail leads somewhere unseen.")
    time.sleep(1)
    print("In front of you rests a large white house with a red roof and brick chimney. Smoke bellows out of the chimney. I wonder if anyone is home?")
    time.sleep(1)
    print("Behind you is the cave you awoke in.")
    time.sleep(1)
    print("Where would you like to go?\n 1. Forest\n 2. Cobblestone trail\n 3. Large white house\n 4. Check the cave")
    answer = input("Choose an option: \n")
    if answer == "1":
        print("As you approach the forest, the calm, tranquil feeling of the meadow is still present. However, as you head deeper into the forest, the tranquil feeling begins to fade.")
        time.sleep(1)
        print("The trees around you tower over you. The wind causes them to sway is if they are alive. In some way, you feel the forest is guiding you somewhere.")
        time.sleep(1)
        print("You reach a tree in the middle causing your path to fork. From there, the path branches left and right.")
        time.sleep(1)
        print("The left path is bright and sunny and more birds can be heard chirping from that direction. The right path heads through a forest of dead, decaying trees, the sky ahead somehow seems darker than the area surrounding it as if to emphasize the ominous nature of this path.")
        time.sleep(1)
        print("Birds can be heard chirping above you in the tree.")
        time.sleep(1)
        print("There is a strange whistling sound coming from the base of the tree. I wonder what that could be.")
        time.sleep(1)
        print("What would you like to do?\n 1. Return to the meadow\n 2. Head down the left path\n 3. Head down the right path\n 4. Look up\n 5. Examine the tree")
        answer = input("Choose an option: \n")
        if answer == "1":
            print("You return back to the meadow.")
            time.sleep(1)
            print("To your left you see a vast forest rich with folliage. The sound of birds chirping can be heard coming from deep within the forest.")
            time.sleep(1)
            print("To your right, a cobblestone trail leads somewhere unseen.")
            time.sleep(1)
            print("In front of you rests a large white house with a red roof and brick chimney. Smoke bellows out of the chimney. I wonder if anyone is home?")
            time.sleep(1)
            print("Behind you is the cave you awoke in.")
            time.sleep(1)
            print("Where would you like to go?\n 1. Forest\n 2. Cobblestone trail\n 3. Large white house\n 4. Check the cave")
            answer = input()
        elif answer == "2":
            print("You head down the path to the left.")
            time.sleep(1)
            print("As you venture down the path, you can hear the chirping of the birds getting louder and louder.")
            time.sleep(1)
            print("A pleasant aroma begins to fill the air. A smell of baked goods, cookies, pies, cakes, and more begins to permeate all around you.")
            time.sleep(1)
            print("What would you like to do?\n 1. Follow the aroma and birds\n 2. Go back to the fork in the road")
            answer = input("Choose an option: \n")
            if answer == "1":
                print("You continue down the path, following your nose and the songs of nature.")
                time.sleep(1)
                print("As you continue down the path, you reach a clearing surrounded by trees.")
                time.sleep(1)
                print("There is something in the center of the clearing, you can't quite see it from back here.")
                time.sleep(1)
                print("The aroma is heavier now, almost intoxicating. You can smell the sweet air wafting towards you.")
                time.sleep(1)
                print("What would you like to do?\n 1. Continue into the clearing\n 2. Head back")
                answer = input("Choose an option: \n")
                if answer == "1":
                    print("You enter the clearing.")
                    time.sleep(1)
                    print("The object in the clearing becomes less and less obscure as you reach the center of the clearing.")
                    time.sleep(1)
                    print("It's a picnic table!")
                    time.sleep(1)
                    print("The object you saw was a picnic table adorned with all sorts of cakes, sweets, and other goodies. The aroma has reached its zenith, it is almost too much to handle, the word 'sickening' crosses your mind.")
                    time.sleep(1)
                    print("Of all the treats on the table, three specific ones catch your eye:\nA beautiful chocolate ganache cake adorned with floral patterns of icing and shaved chocolate\nA golden brownie with a single chocolate chip nearly the size of your hand\nA granola bar. A seemingly insignificant granola bar, but something about it makes it feel more than 'just a granola bar'")
                    time.sleep(1)
                    print("What would you like to do? \n 1. Eat some sweets\n 2. Investigate the table\n 3. Leave the clearing and return to the previous area")
                    answer = input("Choose an option: \n")
                    if answer == "1":
                        print("The aroma is too much, beckoning you, you cannot resist the call.")
                        time.sleep(1)
                        print("The sweets glisten with glazed sugar, the sight brings a tear to your eye.")
                        time.sleep(1)
                        print("What would you like to do?\n 1. Investigate the sweets\n 2. ")
elif answer == "2":
    print("Maybe?")