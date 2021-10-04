from enum import auto

class Character:
    def __init__(self, race, inventory, hp=100, dmg=10, crit=0.1,):
        self.race = race
        self.hp = hp
        self.dmg = dmg
        self.crit = crit
        self.inventory = inventory

    def __str__(self):
        info: str = f"\nРаса: {self.race}" \
                    f"\nЗдоровье: {self.hp}" \
                    f"\nУрон: {self.dmg}" \
                    f"\nКрит. шанс: {self.crit*100}%" \
                    f"\nИнвентарь: {self.inventory}" \
                    f"\n"
        return info


class Human(Character):
    def __init__(self, race="Human", inventory=('sword', 'shield'), dmg=30, crit=0.5, **kwargs):
        super().__init__(race=race, inventory=inventory, dmg=dmg, crit=crit, **kwargs)


pers_dict = {
    'Orc': {
        'inventory': ('blunt', 'Tooth Amulet'),
        'dmg': 50,
        'crit':0.1
    },
    'Human': {
        'inventory': ('sword', 'shield'),
        'crit': 0.5,
        'dmg': 30,
    },
    'Elves': {
        'inventory': ('bow', 'quiver'),
        'crit': 0.85,
        'dmg': 20,
    },
    'Dwarf': {
        'inventory': ('Hummer', 'Seal'),
        'crit': 0.35,
        'dmg': 40,
    }
}


if __name__ == '__main__':
 pass
