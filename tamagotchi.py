class pet:
    happiness_level_max = 10 
    hunger_level_max = 10 
    def __init__ (self, name = "Spencer"):
        self.name = name
        self.happiness_level = randrange(self.happiness_level_max)
        self.hunger_level = randrange(self.hunger_level_max)

    def mood():
        if self.happiness_level < 5:
            return "bleh"
        elif 5 < self.happiness_level < 7: 
            return "hanging in there"
        elif self.happiness_level > 7: 
            return "happy"
    
    def hunger():
        if self.hunger_level < 5: 
            return "I'm full"
        elif 5 < self.hunger_level < 7: 
            return "Give me some food"
        elif self.hunger_level > 7:
            return "I'M VERY HUNGRY, HUMAN"




print("1: Feed your pet")
print("2: Play with your pet")
print("3: Check your pet's levels")
inp = int(input("Enter a number: "))

if inp == 1:
    pet.hunger_level -= 1 
elif inp == 2: 
    pet.happiness_level += 1
elif inp == 3: 
    print("Hunger:", hunger(), "Mood:", mood())


# def happiness():
#     pet.happiness_level -= 1  
    
# print ('What is the name of your pet?')
# name = input()
# Spencer = pet(name)
# print ("Do you want to play with your pet?")
# # input = yes or no
# print ("Press to check happiness and hunger")
# # if pressed
# # return happines and hunger