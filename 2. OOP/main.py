from random import randint, choice
import time


class Character:
    __DIFFICULTY: int = 1
    __slots__ = ['_race_stat', 'race', 'hp', 'dmg', 'crit', 'inventory']

    def __init__(self, race, hp=100):
        self._race_stat = Character.races().get(race)
        self.race = race
        self.hp = hp * Character.__DIFFICULTY
        self.dmg = self._race_stat.get('dmg') * Character.__DIFFICULTY
        self.crit = self._race_stat.get('crit')
        self.inventory = self._race_stat.get('inventory')

    def __str__(self):
        info: str = f"\nРаса: {self.race}" \
                    f"\nЗдоровье: {self.hp}" \
                    f"\nУрон: {self.dmg}" \
                    f"\nКрит. шанс: {self.crit * 100}%" \
                    f"\nИнвентарь: {self.inventory}" \
                    f"\n"
        return info

    # Изменение множителя характеристик
    @classmethod
    def change_difficulty(cls):
        print('Выбор сложности\n1 Обычная\n2 Сложная\n3 Ад')
        value = input('введи номер сложности : ')
        cls.__DIFFICULTY = int(value)
        print(f'Установлен уровень сложности: [>>{value}<<]')
        time.sleep(3)

    @staticmethod
    def heropick():
        heroes = Character.races().keys()
        print(heroes)
        print('Выбор Героя')

        for index, hero in enumerate(heroes):
            print(index, hero)

        choice_hero = input('Введи номер героя : ').strip()
        race = list(heroes)[int(choice_hero)]
        Player = Character(race=race)
        print(f'***********************\n'
              f'Игрок создан\n {Player}'
              f'***********************')
        return Player

    # Словарь доступных пресетов персонажей/монстров
    @staticmethod
    def races():
        return {
            'Orc': {
                'inventory': ('blunt', 'Tooth Amulet'),
                'dmg': 50,
                'crit': 0.1
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


class EnemiesGenerate:
    def __init__(self):
        self.enemies = []
        self.create_enemies()

    def create_enemies(self):
        enemies = list(Character.races().keys())
        for item in range(1, randint(1,20)):
            enemy = choice(enemies)
            print(f'Создан враг {enemy}')
            self.enemies.append(
                Character(race=enemy)
            )
            time.sleep(2)


class Game:
    def __init__(self):
        self.Player = Character.heropick()
        Character.change_difficulty()
        self.enemy = EnemiesGenerate()


if __name__ == '__main__':
    game = Game()
