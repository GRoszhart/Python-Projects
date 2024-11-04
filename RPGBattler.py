import random

# Define character class
class Character:
    def __init__(self, name, health, attack, defense, xp=0, level=1):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.xp = xp
        self.level = level

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def is_alive(self):
        return self.health > 0

    def gain_exp(self, amount):
        self.xp += amount
        if self.xp >= self.level * 20:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.attack += 5
        self.defense += 5
        self.health += 25
        print(f"{self.name} leveled up! Now at level {self.level}. Attack, defense, and health are now {self.attack},{self.defense}, and {self.health}, respectively.")

    def __str__(self):
        return f"{self.name} - Level {self.level} - Health: {self.health}"

# Calculation to determine damage dealt and received
def calculate_damage(attacker, defender):
    base_damage = max(1, attacker.attack - defender.defense)
    random_factor = random.randint(-2, 5)
    return max(0, base_damage + random_factor)

# Define NPC class for quests and dialogue
class NPC:
    def __init__(self, name, dialogue, quest=None):
        self.name = name
        self.dialogue = dialogue
        self.quest = quest

    def interact(self):
        print(f"{self.name}: {self.dialogue}")
        if self.quest:
            print(f"Quest: {self.quest}")

# Sample quest and NPC interaction
def village_scene(player):
    print("\nYou arrive at the village.")
    village_elder = NPC("Village Elder", "Welcome, traveler! A monster lurks in the forest. Can you help us?", "Defeat the Goblin in the forest.")
    village_elder.interact()

    choice = input("Do you want to take the quest? (yes/no): ").lower()
    if choice == "yes":
        print("You accepted the quest! Head to the forest to find the Goblin.")
        return "forest"
    else:
        print("You decide to explore the village more.")
        return "village"

# Main game loop with storyline
def main_game():
    player = Character(name="Hero", health=100, attack=20, defense=10)
    location = "village"  # Starting location

    while player.is_alive():
        if location == "village":
            location = village_scene(player)

        elif location == "forest":
            print("\nEntering the forest, you encounter a Goblin!")
            goblin = Character(name="Goblin", health=50, attack=15, defense=5)

            # Battle loop
            while player.is_alive() and goblin.is_alive():
                print(f"\n--- {player.name}'s Turn ---")
                damage = calculate_damage(player, goblin)
                goblin.take_damage(damage)
                print(f"{player.name} deals {damage} damage to {goblin.name}!")
                print(goblin)

                if not goblin.is_alive():
                    print(f"{goblin.name} has been defeated! You gain 15 XP.")
                    player.gain_exp(15)
                    location = "village"  # Return to village after battle
                    break

                print(f"\n--- {goblin.name}'s Turn ---")
                damage = calculate_damage(goblin, player)
                player.take_damage(damage)
                print(f"{goblin.name} deals {damage} damage to {player.name}!")
                print(player)

                if not player.is_alive():
                    print("You have been defeated! Game Over.")
                    break

# Start the game
main_game()