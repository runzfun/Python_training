

class Character:
    def __init__(self, race, inventory, hp=100, dmg=10, crit=0.1,):
        self.race = race
        self.hp = hp
        self.dmg = dmg
        self.crit = crit
        self.inventory = inventory

    def info(self):
        print(f"\nРаса: {self.race}"
              f"\nЗдоровье: {self.hp}"
              f"\nУрон: {self.dmg}"
              f"\nКрит. шанс: {self.crit*100}%"
              f"\nИнвентарь: {self.inventory}"
              f"\n")


class Human(Character):
    def __init__(self, race="Human", inventory=('sword', 'shield'), dmg=30, crit=0.5, **kwargs):
        super().__init__(race=race, inventory=inventory, dmg=dmg, crit=crit, **kwargs)


class Orc(Character):
    def __init__(self, race="Orc", inventory=('blunt', 'Tooth Amulet'), dmg=50, crit=0.1, **kwargs):
        super().__init__(race=race, inventory=inventory, dmg=dmg, crit=crit, **kwargs)


if __name__ == '__main__':
    human = Human()
    orc = Orc()
    human.info()
    orc.info()
