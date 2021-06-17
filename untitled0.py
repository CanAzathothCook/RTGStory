import random
IsThisCheating = 0
RequestedFunction = input("What would you like?\n\nList of archived traits? (archive)\n\nTo add a new trait? (new)\n\nA random trait (randtrait)\n").lower()
while IsThisCheating == 0:
  if RequestedFunction == "randtrait":
    #RTGSelectionPt1 
    TraitZoneNumber = random.randint(1,100)
    TraitProperties = ""
    if TraitZoneNumber < 25:
     print("Unconsealable trait")
     TraitProperties = "Unconsealable"
     IsThisCheating = 1
    elif TraitZoneNumber < 50:
      print("Basic Trait")
      TraitProperties = "Basic"
      IsThisCheating = 1
    elif TraitZoneNumber < 75:
      print("Supernatral Trait")
      TraitProperties = "SuoerTrait"
      IsThisCheating = 1
    elif TraitZoneNumber < 100:
      print("Tree Skill")
      TraitProperties = "Treeskill"
      IsThisCheating = 1
    else:
      print("New Tree")
      TraitProperties = "NewTree"
      IsThisCheating = 1
  else:
    RequestedFunction = input("\nWhat would you like?\n\nList of archived traits? (archive)\n\nTo add a new trait? (new)\n\nA random trait (randtrait)\n").lower()
