# Solution file
class Character:
    def attack(self):
        print("Basic Attack")

class Warrior(Character):
    def attack(self):
        print("Sword Attack")

class Mage(Character):
    def attack(self):
        print("Magic Attack")

w = Warrior()
m = Mage()

w.attack()
m.attack()