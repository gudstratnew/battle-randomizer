import random as rand
import numpy as np
import string

numRules = 3
rules = [
    ("Only mons starting with @", 10, True),
    ("Only moves starting with @", 10, True),
    ("Only items starting with @", 5, True),
    ("Only mons that have 1 type", 10, True),
    ("Only mons that are part & type", 15, True),
    ("Damaging moves can only be up to # base power", 15, True)
]

types = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", 
         "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
tiers = ["LC", "ZU", "NU", "PU", "RU", "UU", "OU", "Ubers"]


#### CLAUSES ####

def getRandom(n):
    return np.random.randint(n)

print("3 MONS, 7 MINUTE TIME LIMIT")
print("NATIONAL DEX")         if getRandom(100) <= 50 else print("SV POKEDEX")            # Dex Picker
print("Only", rand.choice(tiers), "pokemon or below")                                # Tier Picker
print("TERASTALLIZE ON") if getRandom(100) <= 50 else print("TERASTALLIZE OFF")
print()

print("Species Clause ON")    if getRandom(100) <= 90 else print("Species Clause OFF")    # Species Clause
print("Moody Clause ON")      if getRandom(100) <= 70 else print("Moody Clause OFF")    # Moody Clause
print("OHKO Clause ON")       if getRandom(100) <= 85 else print("OHKO Clause OFF")    # OHKO Clause
print("Evasion Clause ON")    if getRandom(100) <= 85 else print("Evasion Clause OFF")    # Evasion Clause

print()

#### RULES ####

for i in range(numRules):
    selectedRules = [(rule, weight, selected) for rule, weight, selected in rules if selected == True]
    randNum = np.random.randint(np.sum([t[1] for t in selectedRules]))

    selectedRule = 0
    for t in selectedRules:
        selectedRule = selectedRule + t[1]
        if selectedRule >= randNum:
            selectedRule = t
            break
    delInd = rules.index(selectedRule)
    del rules[delInd]
    selectedRuleString = selectedRule[0].replace("@", rand.choice(string.ascii_letters).upper())
    selectedRuleString = selectedRuleString.replace("&", rand.choice(types))

    bpLowerBound = 50
    bpUpperBound = 130
    selectedRuleString = selectedRuleString.replace("#", str(np.random.randint(bpLowerBound/5, bpUpperBound/5)*5))
    print("RULE " + str(i + 1) + ": " + selectedRuleString)
