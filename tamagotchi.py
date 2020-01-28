import random

class pet:
    happiness_level_max = 0 
    hunger_level_max = 10 
    def __init__ (self, name):
        self.name = name
        self.happiness_level = self.happiness_level_max
        self.hunger_level = self.hunger_level_max


    def mood(self):
        if self.happiness_level < 5:
            return "bleh"
        elif 5 < self.happiness_level < 7: 
            return "hanging in there"
        elif self.happiness_level > 7: 
            return "happy"
    
    def hunger(self):
        if self.hunger_level < 5: 
            return "I'm full"
        elif 5 < self.hunger_level < 7: 
            return "Give me some food"
        elif self.hunger_level > 7:
            return "I'M VERY HUNGRY, HUMAN"


name = str(input("What would you like your Tamagotchi to be called?"))

instance = pet(name)

playing = True

while playing is True:
    print('What would you like to do with ' + instance.name + '?')
    print("1: Feed your pet")
    print("2: Play with your pet")
    print("3: Check your pet's levels")
    print("4: Exit game")
    inp = int(input("Enter a number: "))
    if inp == 1:
        instance.hunger_level -= 1
        print("Your pet's hunger level is now:", instance.hunger_level)
    elif inp == 2: 
        instance.happiness_level += 1
        print("Your pet's mood is now:", instance.happiness_level)
    elif inp == 3: 
        print("Hunger:", instance.hunger(), "Mood:", instance.mood())
    elif inp == 4:
        break
