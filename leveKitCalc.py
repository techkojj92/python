import datetime
import os
jobs = ['ALC', 'ARM', 'BSM', 'CRP', 'CUL', 'GSM', 'LTW', 'WVR']
levels = [0, 300, 900, 2000, 3700,
          6000, 10200, 16200, 23550, 33480,
          45280, 60880, 80480, 104180, 130580,
          161080, 196480, 236980, 282680, 333680,
          390280, 454180, 525580, 604680, 691780,
          786980, 896780, 1021580, 1161780, 1317680,
          1480180, 1656080, 1845680, 2049180, 2267080,
          2499400, 2749300, 3017100, 3303300, 3608200,
          3932200, 4272400,4629200, 5002900, 5393700,
          5801900, 6239500, 6707000, 7205000, 7734000,
          8598000, 9656400, 10923600, 12478800, 14350800,
          16568400, 19160400, 22155600, 25582800, 29470800]

youFuckedUp = 'Fuck you Tom -_- wtf man??? why???'

def getInput():
    def getUsername():
        return input("Enter clients username:\n".center(64, " "))
    def getPrice():
        try:
            price = int(input("Enter agreed price:\n".center(64, " ")))
            if price < 0:
                print(youFuckedUp)
                return None
            else:
                return price
        except:
            print(youFuckedUp)
            return None
    def getExp():
        try:
            exp = int(input("Enter your current experience:\n".center(64, " ")))
            if exp < 0:
                print(youFuckedUp)
                return None
            else:
                return exp
        except:
            print(youFuckedUp)
            return None

    def getJob():
        job = input("Choose from the following jobs:".center(64, " ") + "\n" + "ALC, ARM, BSM, CRP, CUL, GSM, LTW, WVR".center(64, " ") + "\n")
        if job.upper() not in jobs:
            print(youFuckedUp)
            return None
        else:
            return job

    def getEndLevel():
        try:
            endLevel = int(input("Enter the level you'd like to be:\n".center(64, " ")))
            if endLevel < 16:
                print(youFuckedUp)
                return None
            else:
                return endLevel
        except:
            print(youFuckedUp)
            return None

    username = getUsername()

    price = None
    while price == None:
        price = getPrice()
    
    exp = None
    while exp == None:
        exp = getExp()

    job = None
    while job == None:
        job = getJob()

    endLevel = None
    while endLevel == None:
        endLevel = getEndLevel()

    return [endLevel, job, exp, username, price]      

class Leve(object):
    def __init__(self, name, location, item, number, experience, levelReq):
        self.name = name
        self.location = location
        self.item = item
        self.number = number
        self.experience = experience
        self.levelReq = levelReq
    def addLeve(self):
        if self in leves:
            leves[self] += 1
        else:
            leves[self] = 1

jobLeveLists = {"ALC":[Leve("Devil Take the Foremost", "Camp Drybone > Ul'dah", "HQ Potion of Strength", 8, 27132, 15),
                       Leve("The Writing is Not on the Wall", "Ul'dah > Quarrymill", "HQ Enchanted Silver Ink", 27, 41156, 20),
                       Leve("Glazed and Confused", "Ul'dah > Quarrymill", "HQ Clear Glass Lens", 10, 66200, 25),
                       Leve("Just Give Him a Serum", "Ul'dah > Costa del Sol", "HQ Hi-Potion of Strength", 30, 95648, 30),
                       Leve("Alive and Unwell", "Ul'dah > Observatorium", "HQ Budding Oak Wand", 11, 129584, 35),
                       Leve("A Patch-up Place", "Ul'dah > Whitebrim", "HQ Mega-Potion", 33, 167324, 40),
                       Leve("Sleepless in Silvertear", "Ul'dah > Mor Dhona", "HQ Potent Sleeping Potion", 33, 213120, 45),
                       Leve("The Moustache Suits Him", "Foundation", "HQ Enchanted Mythrite Ink", 11, 190080, 50),
                       Leve("Steeling the Knife, Steeling the Mind", "Foundation", "HQ Grade 1 Mind Dissolvent", 9, 314496, 52),
                       Leve("Adhesive of Antipathy", "Foundation", "HQ Wing Glue", 12, 343728, 54),
                       Leve("Cleansing the Wicked Humours", "Foundation", "HQ Hallowed Water", 15, 368064, 56),
                       Leve("Filling in the Blanks", "Foundation", "HQ Enchanted Aurum Regis Ink", 19, 397556, 58),],
                "ARM":[],
                "BSM":[],
                "CRP":[],
                "CUL":[],
                "GSM":[],
                "LTW":[],
                "WVR":[]
                }

def findLevel(exp):
    for i, level in enumerate(levels):
        if level == exp:
            return i+1
        elif exp < levels[i+1]:
            return i+1
        elif exp > levels[len(levels)-1]:
            return len(levels)

def expToLevel(exp, lvl):
    nextLvl = levels[lvl-1] - exp
    if nextLvl >= 0:
        return nextLvl
    else:
        return 0

def bestLeve(lvl, job):
    tempLeve = Leve("", "", "", 0, 0, 0)
    for x in jobLeveLists[job]:
        if x.levelReq <= lvl:
            if x.experience > tempLeve.experience:
                tempLeve = x
    if tempLeve == Leve("", "", "", 0, 0, 0):
        return None
    else:
        return tempLeve

def levesNeeded(endLevel, job, currentExp):
    tempExp = currentExp

    expNeeded = expToLevel(tempExp, endLevel)

    outputLeves = {}

    while expNeeded > 0:
        if bestLeve(findLevel(tempExp), job) in outputLeves:
            outputLeves[bestLeve(findLevel(tempExp), job)] += 1
        else:
            outputLeves[bestLeve(findLevel(tempExp), job)] = 1
        tempExp = tempExp + bestLeve(findLevel(tempExp), job).experience
        expNeeded = expToLevel(tempExp, endLevel)
    return outputLeves
    
def main():
    inputs = getInput()
    f = levesNeeded(inputs[0], inputs[1], inputs[2])

    finalOutput = "\n----------------------------------------------------------------\n" + ("Order for " + str(inputs[3]) + ": Levels " + str(findLevel(inputs[2])) + " - " + str(inputs[0]) + " for " + str(inputs[4]) + " gil").center(64, " ") + "\n"
    for key in f:
        finalOutput += "Complete " + key.name + " " + str(f[key]) + " times" + "\n\t- craft total of " + str(f[key] * key.number) + " " + str(key.item) + "\n"

    finalOutput += str(datetime.date.today()) + "\n"
    print(finalOutput)

    if not os.path.exists("orders"):
        os.makedirs("orders")

    file = open(str("orders/" + inputs[3]) + ".txt", "w+")
    file.write(finalOutput)
    file.close()

while True:
    main()
