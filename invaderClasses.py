from time import sleep
from invaderImages import*
import random


class Alien:
  def __init__(self, a_type, picture, attraction = random.randint(1,7), strength = random.randint(2,8), intimidation = random.randint(3,8), status = "alive"):
    self.a_type = a_type
    self.attraction = attraction
    self.strength = strength
    self.intimidation = intimidation
    self.picture = picture
    self.status = status

  def __repr__(self):
    print(self.picture)
    alien_description = "You are {a_type} alien.\n".format(a_type=self.a_type)
    if self.attraction >= 5:
      alien_description += "You are attractive.\n"
    else:
      alien_description += "You're not exactly...nice to look at.\n"
    if self.strength >= 5:
      alien_description += "You are pretty strong."
    else:
      alien_description += "You're not a beef cake, but beef brains."
    return alien_description

  def fight(self, human):
    if human.armed == True and human.strength >= self.strength:
      self.status = "dead"
    elif human.armed == True and self.strength > human.strength:
      self.status = "alive"
      print(human_dead)
      sleep(2)
      print("\nYou killed {human}!".format(human=human.per_type))
    elif human.armed == False and human.strength > self.strength:
      self.status = "dead"
    else:
      print(human_dead)
      print("You killed {person}!".format(person=human.per_type))
      self.status = "alive"

  def check_status(self, human):
    if self.status == "dead":
      sleep(3)
      print("\n{person} killed you! Game over.".format(person=human.per_type))
      sleep(3)
      print(death)
    else:
      sleep(3)
      print("\nYou succeeded!")

  def seduce(self, human, copper):
    if self.attraction < human.attraction and human.armed == False:
      sleep(3)
      print("\n{person} is not attracted to you. They scream and a cop comes!\nGet ready to fight!".format(person=human.per_type))
      sleep(1)
      print(trooper)
      self.fight(copper)
    elif self.attraction < human.attraction and human.armed == True:
      print("\n{person} is not attracted to you. Get ready to fight!".format(person=human.per_type))
      sleep(3)
      self.fight(human)
    else:
      sleep(3)
      print("\nThey blush and faint.")

  def intimidate(self, human):
    if human.fear > self.intimidation:
      sleep(3)
      print("\n{person} screams and runs away.".format(person=human.per_type))
    else:
      sleep(3)
      print("\n{person} is not intimidated!\nGet ready to fight!".format(person=human.per_type))
      self.fight(human)




class Human:
  def __init__(self, per_type, armed, picture, fear = random.randint(1,9), strength = random.randint(1,9), attraction = random.randint(1,9)):
    self.per_type = per_type
    self.armed = armed
    self.fear = fear
    self.strength = strength
    self.attraction = attraction
    self.picture = picture
    


  def __repr__(self):
    print(self.picture)
    profile = "{per_type} is approaching!\n".format(per_type=self.per_type)
    if self.strength >= 5:
      profile += "They are strong.\n"
    else:
      profile += "They are weak.\n"
    if self.armed == True:
      profile += "They are armed."
    else:
      profile += "They are unarmed."
    return profile



class Cop(Human):
  pass