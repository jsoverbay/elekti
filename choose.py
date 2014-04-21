#!/usr/bin/python
#choose.py
#A choose your own adventure audio game.
#Jeremy Overbay
#energyresearchlabs.com
#2013
#Pygame programming by Jeremy Overbay
#Story by Albert Sweigart. Edits and some addtions by Jeremy Overbay
#with thanks to Albert Sweigart and his book Invent Your Own Computer Games with Python
from __future__ import print_function

import random
import pygame
from pygame.locals import *
import os
import time


pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lagu
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Choose')
#pygame.mouse.set_visible(1)






##load sounds
#pygame.mixer.music.load(os.path.join('data', 'an-turr.ogg'))#load music
introa = pygame.mixer.Sound(os.path.join("./res/introa.wav"))  #load sound
standing = pygame.mixer.Sound(os.path.join("./res/standing.wav"))
welcome = pygame.mixer.Sound(os.path.join("./res/welcome.wav"))
skulls2 = pygame.mixer.Sound(os.path.join("./res/skulls.wav"))
what = pygame.mixer.Sound(os.path.join("./res/whatwillyoudo.wav"))
cfront = pygame.mixer.Sound(os.path.join("./res/cfront.wav"))
topofcavea = pygame.mixer.Sound(os.path.join("./res/topofcavea.wav"))
smokehole = pygame.mixer.Sound(os.path.join("./res/smokehole.wav"))
ctopofcave = pygame.mixer.Sound(os.path.join("./res/ctopofcave.wav"))
insideofcavea = pygame.mixer.Sound(os.path.join("./res/insideofcavea.wav"))
cinsideofcave = pygame.mixer.Sound(os.path.join("./res/cinsideofcave.wav"))
chimneysmokey = pygame.mixer.Sound(os.path.join("./res/chimneysmokey.wav"))
chimney = pygame.mixer.Sound(os.path.join("./res/chimney.wav"))
upperareaa = pygame.mixer.Sound(os.path.join("./res/upperareaa.wav"))
cupperarea = pygame.mixer.Sound(os.path.join("./res/cupperarea.wav"))
lowerareaa = pygame.mixer.Sound(os.path.join("./res/lowerareaa.wav"))
rockpresent = pygame.mixer.Sound(os.path.join("./res/rockpresent.wav"))
rocksunk = pygame.mixer.Sound(os.path.join("./res/rocksunk.wav"))
rockholding = pygame.mixer.Sound(os.path.join("./res/rockholding.wav"))
clowerarea = pygame.mixer.Sound(os.path.join("./res/clowerarea.wav"))
pickuprock = pygame.mixer.Sound(os.path.join("./res/pickuprock.wav"))
boatsunk = pygame.mixer.Sound(os.path.join("./res/boatsunk.wav"))
rockpickup = pygame.mixer.Sound(os.path.join("./res/rockpickup.wav"))
rockboat = pygame.mixer.Sound(os.path.join("./res/rockboat.wav"))
rocktheboat = pygame.mixer.Sound(os.path.join("./res/rocktheboat.wav"))
rockboatsink = pygame.mixer.Sound(os.path.join("./res/rockboatsink.wav"))
putrockboat = pygame.mixer.Sound(os.path.join("./res/putrockboat.wav"))
boatfloats = pygame.mixer.Sound(os.path.join("./res/boatfloats.wav"))
swimrock = pygame.mixer.Sound(os.path.join("./res/swimrock.wav"))
swimcold = pygame.mixer.Sound(os.path.join("./res/swimcold.wav"))
again = pygame.mixer.Sound(os.path.join("./res/again.wav"))
cend = pygame.mixer.Sound(os.path.join("./res/cend.wav"))
swimmadeit = pygame.mixer.Sound(os.path.join("./res/swimmadeit.wav"))
islanda = pygame.mixer.Sound(os.path.join("./res/islanda.wav"))
islandwin = pygame.mixer.Sound(os.path.join("./res/islandwin.wav"))
islanddragon = pygame.mixer.Sound(os.path.join("./res/islanddragon.wav"))
dragona = pygame.mixer.Sound(os.path.join("./res/dragona.wav"))
givesword = pygame.mixer.Sound(os.path.join("./res/givesword.wav"))
dragonwin1 = pygame.mixer.Sound(os.path.join("./res/dragonwin1.wav"))
dragondeath1 = pygame.mixer.Sound(os.path.join("./res/dragondeath1.wav"))
nogivesword = pygame.mixer.Sound(os.path.join("./res/nogivesword.wav"))
killdragonwin = pygame.mixer.Sound(os.path.join("./res/killdragonwin.wav"))
killdragonlose = pygame.mixer.Sound(os.path.join("./res/killdragonlose.wav"))
boatride = pygame.mixer.Sound(os.path.join("./res/boatride.wav"))
boatridedie = pygame.mixer.Sound(os.path.join("./res/boatridedie.wav"))
boatridelive = pygame.mixer.Sound(os.path.join("./res/boatridelive.wav"))
cswordgive = pygame.mixer.Sound(os.path.join("./res/cswordgive.wav"))
dragonupper = pygame.mixer.Sound(os.path.join("./res/dragonupper.wav"))
bumper = pygame.mixer.Sound(os.path.join("./res/bumper.wav"))
homeward = pygame.mixer.Sound(os.path.join("./res/homeward.wav"))


# play music non-stop
#pygame.mixer.music.play(-1)   


def choosePath(numberOfPaths):
    choice = 0
#    print(choice)
    while choice < 1 or choice > numberOfPaths:
        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                if (event.key != K_1 and event.key != K_2 and event.key != K_3 and event.key != K_4 and event.key != K_5):
                    choice = 0
#                    print(choice)
                if (event.key == K_1):
                    choice = 1
                    choice = int(choice)
#                   print(choice)
                if (event.key == K_2):
                    choice = 2
#                    print(choice)
                if (event.key == K_3):
                    choice = 3
#                    print(choice)
                if (event.key == K_4):
                    choice = 4
#                    print(choice)
                if (event.key == K_5):
                    choice = 5
#                    print(choice)
#        print('1 to ' + str(numberOfPaths) + '> ', end='')
#        choice = raw_input()
#        if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
#            choice = 0
#        if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5':
#            choice = int(choice)
#    print()
    return choice

def pause():
    raw_input()
    pygame.mixer.stop()   #stops playback in case someone is impatient and skips past the audio
	
def impatient():
    while pygame.mixer.get_busy():  #stops imput until sound is not playing
        time.sleep(0.01)
    return

def intro():
#    print('You have ventured to the realm of dragons, and have finally arrived at the Dragon Cave.')
#    print('With your trusty sword at your side and trust backpack on your back, you look upon the fearsome entrance to the cave.')
#    print()
#    print('Listen carefully. The adventure changes each time you play.')
#    print('Treasure or certain death await!')
#    print()
    introa.play()
    impatient()
    bumper.play()
    impatient()
    front()

def front():
    standing.play()
    impatient()
    if skulls == 'present':
#        print('There are a bunch of human skulls and bones lying around.')
        skulls2.play()
        impatient()
    if skulls == 'absent':
#        print('There is a sign here that reads, "Welcome, visitors!"')
        welcome.play()
        impatient()
#    print()
    what.play() #print('What will you do?')
    impatient()
    cfront.play() #print('  1 Go into the cave.')
    impatient() #print('  2 Climb on top of the cave.')
    path = choosePath(3)
    if path == 1:
        insideOfCave()
    if path == 2:
        topOfCave()
    if path == 3:
        goHome()

def goHome():
    homeward.play()
    impatient()
    return

def topOfCave():
    topofcavea.play() #print('After climbing up, you are standing on top of the cave.')
    impatient() #print('There is a small hole that seems to be a chimney nearby.')
    if dragonLocation == 'upper':
#        print('A considerable amount of smoke is coming out of the hole.')
        smokehole.play()
        impatient()
#    print()
    what.play() #print('What will you do?')
    impatient()
    ctopofcave.play() #print('  1 Climb down the hole.')
    impatient() #print('  2 Climb back down to the front entrance.')
    path = choosePath(2)
    if path == 1:
        goDownChimney()
    if path == 2:
        front()

def insideOfCave():
    insideofcavea.play() #print('You are inside front chamber of the cave. You can see the exit of the cave which would take you outside.')
    impatient() #print('There are two paths that lead deeper into the cave, one that goes up and the other that goes down.')
#    print()
    what.play() #print('What will you do?')
    impatient()
    cinsideofcave.play() #print('  1 Go outside of the cave.')
    impatient() #print('  2 Take the upper path deeper into the cave.')
#    print('  3 Take the lower path deeper into the cave.')
    path = choosePath(3)
    if path == 1:
        front()
    if path == 2:
        upperArea()
    if path == 3:
        lowerArea()

def goDownChimney():   # make it possible to climb out?
    if dragonLocation == 'upper':
        chimneysmokey.play() #print('You climb down into the smokey chimney. The smoke is really thick!... (press enter)')
        impatient() #input()
#        print('The smoke keeps getting thicker. It is getting hard to breathe... (press enter)')
#        input()
#        print('You have become lost in the smoke, and start coughing. You cannot get any air!... (press enter)')
#        input()
#        print('ACK! You have suffocated to death! It was kind of dumb to climb into that smokey chimney.')
        return
    if dragonLocation == 'lower':
        chimney.play() #print('You climb down the chimney. It seems to lead you somewhere inside the cave.')
        impatient()
        upperArea()

def upperArea():
    upperareaa.play() #print('You are standing in a chamber near the top of the cave. There is a rope ladder to a chimney hole in the ceiling that leads outside.')
    impatient()
    if dragonLocation == 'upper':
        dragonupper.play() #print('The dragon is standing in the chamber! Smoke comes out of his nostrils and floats up and out the hole in the ceiling.')
        impatient()
        faceDragon()
    if dragonLocation == 'lower':
        print()
        what.play() #print('What will you do?')
        impatient() #print('  1 Climb up and out of the hole.')
        cupperarea.play() #print('  2 Go down to the front of the cave.')
        impatient()
        path = choosePath(2)
        if path == 1:
            topOfCave()
        if path == 2:
            insideOfCave()


def lowerArea():
    lowerareaa.play() #print('You are in the lower chamber of the cave.')
    impatient() #print('This chamber is very large, and has an underground lake. The water is dark')
#    print('and murky. It is difficult to tell how deep it is or what may be in it. In the middle of the lake,')
#    print('you dimly see a small island. Something shiny on the island glimmers in the murk. ')
#    print('There is also a path leading back to the front of the cave.')
#    print()
    if rock == 'present':
        rockpresent.play() #print('Near the shore there is a large rock.')
        impatient() #print('An old boat has also been left here.')
    if rock == 'sunk':
        rocksunk.play() #print('There is a submerged boat at the bottom of the water near the shore.')
        impatient()
    if rock == 'holding':
        rockholding.play() #print('An old boat has also been left here.')
        impatient()
    if rock == 'boat':
        rockboat.play() #print('An old boat has also been left here. You can see a large rock in it.')
        impatient()
#    print()
    what.play() #print('What will you do?')
    impatient()
    clowerarea.play() #print('  1 Go to back to the front of the cave.')
    impatient() #print('  2 Swim the lake to the island.')
#    print('  3 Take the creaky old boat to the island.')
    if rock == 'present':
        pickuprock.play() #print('  4 Pick up the large rock.')
        impatient()
    if rock == 'holding':
        putrockboat.play() #print('  4 Put the large rock in the boat.')
        impatient()
#    print()
    path = choosePath(4)
    if path == 1:
        front()
        return
    if path == 2:
        swim()
        return
    if path == 3 and rock == 'sunk':
        boatsunk.play() #print('That boat does not look like it is going anywhere.')
        impatient() #print()
#        pause()
        lowerArea()
        return
    if path == 3 and rock != 'sunk':
        rideBoat()
        return
    if path == 4 and rock == 'present':
        takeRock()
        return
    if path == 4 and rock == 'holding':
        putRockInBoat()
        return

def takeRock():
    global rock
    rockpickup.play() #print('You pick up the large rock and put it in your trusty backpack. Ooof! It sure is heavy.')
    impatient() #print()
#    pause()
    rock = 'holding'
    lowerArea()

def putRockInBoat():
    global rock
    rocktheboat.play() #print('You put the large rock down in the creaky old boat. The boat rocks from side to side, no pun intended.')
    impatient() #print()
#    pause()
    if boat == 'sinks':
        rockboatsink.play() #print('The creaky old boat begins to sink under the weight of the rock!')
        impatient() #print('Whew! It is a good thing you did not try to take that boat to the island.')
#        print()
        rock = 'sunk'
#        pause()
        lowerArea()
        return
    if boat == 'floats':
        boatfloats.play() #print('The creaky old boat seems to be holding up under the weight of the rock.')
        impatient() #print()
        rock = 'boat'
#        pause()
        lowerArea()
        return

def swim():
    swimcold.play() #print('You dive into the water. Yipes! It is icy cold!')
    impatient() #pause()
    if rock == 'holding':
        swimrock.play() #print('You begin to swim to the island, but the heavy rock you are holding begins to drag you down!... (press enter)')
        impatient() #input()
#        print('ACK! You cannot get the straps off of your backpack!... (press enter)')
#        input()
#        print('You begin to drown in the murky, dark waters of the underground lake... (press enter)')
#        input()
#        print('You have drowned! It was kind of dumb to swim the lake with that heavy rock in your backpack.')
#        pause()
        return
    if rock != 'holding':
        swimmadeit.play() #print('You begin to swim to the island. The island is further away than you thought... (press enter)')
        impatient() #input()
#        print('You are getting tired from all that swiming. You are not sure you can make it... (press enter)')
#        input()
#        print('You finally get to the shore of the island. Whew! You do not think it is a good idea to try that swim again!')
#        pause()
        island()

def rideBoat():
    boatride.play() #print('You get into the creaky old boat and begin to row towards the island... (press enter)')
    impatient() #input()
#    print('Half way to the island, you notice that the boat has a small leak!... (press enter)')
#    input()
#    print('You row faster and faster as the boat slowly begins to sink.... (press enter)')
#    input()
#
    if boat == 'sinks':
        boatridedie.play() #print('The boat is sinking, and your shoe is stuck to some gum on the bottom of the boat!... (press enter)')
        impatient() #input()
#        print('You try to get your shoe off, but not before your head sinks under the murky water... (press enter)')
#        input()
#        print('What a dumb way to die. Your adventuring skills were no match for the gum. You have died.')
#        pause()
        return
    if boat == 'floats':
        boatridelive.play() #print('The boat sinks, but it floated long enough for you to get close to the shore of the island. After a short swim in the icey waters, you climb onto the island.')
        impatient() #pause()
        island()
        return


def island():
    islanda.play()
    impatient()
#   print('You are standing on the island in the middle of the underground lake. The shiny glint comes from a large pile of gold and jewels!')
#   print('You see there is a rope ladder from the ceiling above the island.')
#    pause()
    if dragonLocation == 'upper':
        islandwin.play() #print('You start putting as much treasure as your backpack can hold.')
        impatient() #print('You climb the rope ladder, and you see that it leads to a hole in the ceiling that goes outside of the cave.')
#        print()
#        print('You have escaped from the Dragon Cave with the treasure! Congratulations! You have won the game!')
#        pause()
        return
    if dragonLocation == 'lower':
        islanddragon.play() #print('But in front of the treasure is the dragon!')
        impatient()#pause()
        faceDragon()
        return

def faceDragon():
    dragona.play() #print()
    impatient()
#   The dragon is huge! He stands ten feet tall, and has tough green scales and giant claws.
#   His leathery wings are folded back over his massive body, and he smiles at you with giant teeth as whisps of smoke come out of his nostrils.
#   Your trusty sword is at your side, but the dragon is so scary you think you might soil your trusty trousers.
#   The dragon smiles at you, and then speaks.
#   "Welcome adventurer. You have come a long way to my cave. Seeking treasure and fortune, are you? Well, I have plenty of it myself."
#   "All this gold and jewels is cluttering up my place, and I would like to get rid of it. Why not trade me that fancy sword for as much treasure as you can put into your backpack?"
#    "You can climb this rope ladder to exit the cave. You can trust me. I do not want to eat you. I am a friendly vegetarian dragon. What do you say?"
    what.play() #print('What will you do?')
    impatient()
    cswordgive.play() #print('  1 Trust the dragon, and give him your sword in exchange for treasure.')
    impatient() #print('  2 Attack the dragon with your trusty sword.')
    path = choosePath(2)
    if path == 1:
        givesword.play() #print()
        impatient() #print('You hand over your trusty sword to the dragon. With all that treasure, you could buy a hundred trusty swords!... (press enter)')
#        raw_input()
#        print('The dragon takes the sword and places it on a rack high on the wall, out of your reach... (press enter)')
#        raw_input()
#        print('He turns to you and smiles. This dragon sure does smile a lot... (press enter)')
#        raw_input()
#        print('The dragon begins to open his mouth... (press enter)')
#        raw_input()
#        print()
        if skulls == 'present':
            dragondeath1.play() #print('Giant waves of flame come from the dragons mouth! You are incinerated instantly!')
            impatient() #print()
#            print('The dragon pours barbecue sauce on your well-done corpse. Guess he was\'nt a vegetarian after all.')
#            print('After gnawing the meat from your skeleton, he tosses your skull and bones outside the front of his cave.')
#            print()
#            print('You have died.')
#            pause()
            return
        if skulls == 'absent':
            dragonwin1.play() #print('"Thanks a lot!", the dragon says. "I have started a trusty sword collecting hobby, and yours is the first!"')
            impatient() #print('"Take as much treasure as you want!"')
#            print()
#            print('You stuff as much gold and jewels as your trusty backpack can carry, and climb the rope ladder up to a hole in the ceiling that leads outside.')
#            print('The dragon waves goodbye as you leave. You have survived the Dragon Cave with enough treasure to retire. Congratulations!')
#            print()
#            pause()
            return
    if path == 2:
        nogivesword.play() #print()
        impatient() #print('You are no fool. You pretend to hand over your sword... (press enter)')
#        raw_input()
#        print('But at the last minute, you swing it at the dragon\'s neck!... (press enter)')
#        raw_input()
        if skulls == 'present':
            killdragonwin.play() #print('In one quick swipe, you cut off the dragon\'s head!')
#            pause()
            impatient() #print()
#            print('With the dragon slayed, you stuff as much gold and jewels into your trusty backpack as it can hold.')
#            print('The rope ladder leads up to a hole in the ceiling that goes outside of the cave.')
#            print('You have survived the Dragon Cave with enough treasure to retire. Congratulations!')
#            print()
#            pause()
            return
        if skulls == 'absent':
            killdragonlose.play() #print('But the dragon dodges your blade!')
#            pause()
            impatient #print('"Fiend!", the dragon shouts. He is really angry at you, and breathes a wave of flame onto you.')
#            print('You are incinerated instantly!')
#            pause()
#            print('The dragon pours barbecue sauce on your well-done corpse, and then wraps you in foil and puts you in his refrigerator.')
#            print('It is a little known fact that dragons also have refrigerators in their caves, along with gold and jewels.')
#            pause()
#            print('The dragon doesn\'t eat you, because he is a vegetarian after all. But he will bring you to the next dragon pot luck dinner.')
#            pause()
#            print()
#            print('You have died.')
            return

while True:
    # Randomly generate the game variables
    if random.randint(1,2) == 1:
        dragonLocation = 'upper'
    else:
        dragonLocation = 'lower'

    if random.randint(1,2) == 1:
        skulls = 'present'
    else:
        skulls = 'absent'

    if random.randint(1,2) == 1:
        boat = 'sinks'
    else:
        boat = 'floats'

    rock = 'present'

    # Start the game
    intro()

#    print()
    bumper.play()
    impatient()
    again.play() #print('Would you like to play again? Y/N')
    impatient()
    cend.play()
    impatient()
    playAgain = 0
    while playAgain < 1 or playAgain > 2: #    playAgain = raw_input()
        for event in pygame.event.get(): #if playAgain == 'Y' or playAgain == 'y':
            if (event.type == KEYDOWN):
                if (event.key != K_1 and event.key != K_2):
                    playAgain = 0
                if (event.key == K_1): #continue
                    playAgain = 1                 
                if (event.key == K_2):
                    playAgain = 2
                    print(playAgain)
                    pygame.quit()
                    quit()
    if playAgain == 1:
        continue
#    if playAgain == 'N' or playAgain == 'n':
#       break
    break
