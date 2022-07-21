import random
from time import sleep
from invaderClasses import*
from invaderImages import*


######### characters ##########
human_1 = Human("Donut Dan the frosting thirsty cop", True, cop)
human_2 = Human("Marty the mailman, a.k.a. Dog Bait", False, mailman)
human_3 = Human("Babbling Betty the bored housewife", True, betty)
human_4 = Human("Meaty Mabel the malignant nurse", False, nurse)
human_5 = Human("Piers the pimple pizza boy", False, pizza)

alien_1 = Alien("Vytron the half cyborg half badass", cyborg)
alien_2 = Alien("Yuvolti the little child colonizer", lit_alien)
alien_3 = Alien("Woovilgoovildool the brainy scientist", brainiac)




###### functions start here #########
def intro():
  print("""
  Welcome to Alien Invasion!\n\n
  You have landed on earth and plan on total destruction!\n
  Do you have what it takes?\n
  """)  
  sleep(4)
  print("Please choose your alien invader:\n")

def confrontation(next_enemy):
  copper = Cop("Cooper the Super Trooper", True, trooper)
  move = input("Do you want to fight, seduce, or intimidate?\n\n")
  if move == "fight":
    player.fight(next_enemy)
  elif move == "seduce":
    player.seduce(next_enemy, copper)
  elif move == "intimidate":
    player.intimidate(next_enemy)
  else:
    print("Invalid choice. Try again.")
    confrontation(next_enemy)

def choose_character():
  print(alien_1, "\n")
  sleep(5)
  print(alien_2, "\n")
  sleep(5)
  print(alien_3, "\n")
  sleep(5)
  char_choice = input("\nEnter 1, 2, or 3\n")
  return char_choice



    
############ Main start here ########

intro()
sleep(3)

choice = choose_character()

if choice == "1":
  player = alien_1
  
elif choice == "2":
  player = alien_2
  
elif choice == "3":
  player = alien_3
  
else:
  print("\nInvalid choice. Try again.")
  choice = choose_character()



print("\nOkay, good luck invader!\n")
sleep(3)

enemy_list = [human_1, human_2, human_3, human_4, human_5]

for num in range(5):
  if player.status == "alive":
    next_enemy = random.choice(enemy_list)
    print(next_enemy, "\n")
    sleep(3)
    confrontation(next_enemy)
    player.check_status(next_enemy)
    sleep(3)
    
if player.status == "alive":
  sleep(3)
  print("\nEarth is yours!!!\nGood job Invader!")
  sleep(3)
  print(win)