#using random chance, so need to import the random library
import random

#core gameplay loop
def playGame(adventurer, enemies_list, moveCount = 5):
    for move in range(1, moveCount+1):
        if (stillAlive(adventurer) == False):
            break
        promptMove(adventurer)
        print()
        currentEnemy = getEnemy(enemies_list)
        lootValue = getLootValue(currentEnemy)
        adventurerAction = getActionOption()
        showActionOutcome(adventurerAction,adventurer,currentEnemy,lootValue)
        
    showGameOutcome(adventurer)
    
#defining if the character has more than 0 hp    
def stillAlive(adventurer):
    if (adventurer["healthPoints"] > 0):
        return True
    else:
        return False

#defining when the user is ready to tackle another enemy, as well as keep track of total encounters
def promptMove(adventurer):
    input("Press ENTER to make a move.")
    adventurer["position"] = adventurer["position"] + 1

#define how the enemy is chosen for the adventurer to fight
def getEnemy(enemies_list):
    currentEnemy = random.choice(enemies_list)
    print("You encountered the enemy: ")
    showEnemy(currentEnemy)
    return currentEnemy

#defining the enemy descriptions
def showEnemy(enemy):
    enemyDescription = "<>--<>--<>--<>--<>--<>--<>--<>--<>\n"
    enemyDescription += "Enemy: " + enemy[0] + "\n"
    enemyDescription += "Details: " + enemy[1] + "\n"
    enemyDescription += "Max Damage: " + str(enemy[2]) + "\n"
    enemyDescription += "<>--<>--<>--<>--<>--<>--<>--<>--<>\n"
    print(enemyDescription)
    
#defining how the loot point values are chosen based on the enemies max damage
def getLootValue(enemy):
    lootValue = random.randint(1, enemy[2]*2)
    print("The enemy holds loot worth " + str(lootValue) + " points.\n")
    return lootValue

#defining the 2 options the player has when they encounter an enemy
def getActionOption():
    adventurerAction = -1
    while True:
        adventurerAction = int(input("Will you attack (1), or dodge (2)? "))
        print()
        if (adventurerAction == 1 or adventurerAction == 2):
            break
    return adventurerAction

#showing how to display the result of the encounter
def showActionOutcome(adventurer_action,adventurer,current_enemy,loot_value):
    if (adventurer_action == 1):
        damagePoints = random.randint(1,current_enemy[2])
        subtractHealthPoints(adventurer,damagePoints)
        addLootPoints(adventurer,loot_value)
        print("You got the loot, but the " + current_enemy[0] + " did " + str(damagePoints) + " damage to your health points.")
    else:
        print("You evaded the enemy, but got no loot for doing so.")
    print()
    print(adventurer["name"] + "'s status:")
    showAdventurerStatus(adventurer)
    
#adding on the loot point gains onto my current inventory of loot points
def addLootPoints(adventurer, new_loot_points):
    adventurer["lootPoints"] = adventurer["lootPoints"] + new_loot_points
    
#the adventurer takes damage based on the health points lost in the previous encounter
def subtractHealthPoints(adventurer,health_points):
    adventurer["healthPoints"] = adventurer["healthPoints"] - health_points
    if (adventurer["healthPoints"] < 0):
        adventurer["healthPoints"] = 0
        
#defines what the status display looks like after each encounter
def showAdventurerStatus(adventurer):
    adventurerStatus = "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n"
    adventurerStatus += "Adventurer: " + adventurer["name"] + "\n"
    adventurerStatus += "Completed Encounters: " + str(adventurer["position"]) + "\n"
    adventurerStatus += "Health Points: " + str(adventurer["healthPoints"]) + "\n"
    adventurerStatus += "Loot Points: " + str(adventurer["lootPoints"]) + "\n"
    adventurerStatus += "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n"
    print(adventurerStatus)
    
#what the game will show at the end; either dead, or gg you got some awesome loot
def showGameOutcome(adventurer):
    print("Game is over.\n")
    print(adventurer["name"] + "'s final status:")
    showAdventurerStatus(adventurer)
    if (stillAlive(adventurer) == True):
        print("Congratulations! You have emerged victourious over your foes, \nand have acquired some valuable loot! \nYou completed the game with " + str(adventurer["lootPoints"]) + " loot points!")
    else:
        print("You sadly did not survive the game. RIP.")
    
#main method with different enemy types and adventurer list descriptions
def main():
    moveCount = 5
    enemiesList = []
    enemiesList.append(("Zombie", "A hulking, smelly creature.", 25))
    enemiesList.append(("Skeleton","Not really sure how this thing can walk...", 30))
    enemiesList.append(("Undead Miner","Poor guy just wants to do his job.", 35))
    enemiesList.append(("Angry Ghost","You can see right through its schemes.",40))
    
    adventurerName = input("Please enter the name of your adventurer: ")
    print("Oh brave " + str(adventurerName) + ", your goal is to survive 5 encounters against various enemies, \nwhile collecting as many loot points as possible. \nEach enemy will have a certain number of loot points that they are holding, \nand you can choose to attack to get the loot,\nor evade them if you don't feel it's worth the effort. You have 100 health points total, so be cautious when attacking.\nGood luck!")
    
    theAdventurer = {"name":adventurerName, "position":0, "healthPoints":100, "lootPoints":0}
    print()
    playGame (theAdventurer, enemiesList, moveCount)

#invoking main method
main()