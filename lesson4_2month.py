class GameEmtity:
    def __init__(self, name, healh, damage):
        self.__name = name
        self.__health = healh
        self.__damage = damage

        @property
        def name(self):
            return
        @property
        def health(self):
            return

        @health.setter
        def health(self, value):
            pass
        @property
        def damage(self):
            return

        @damage.setter
        def damage(self, value):
            pass

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEmtity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    @property
    def defense(self):
        return

    def choose_defense(self, heroes):
        pass

    def attack(self, heroes):
        pass

    def __str__(self):
        return f'boss: '



class Hero(GameEmtity):
    def __init__(self,name,health,damage,ability):
        super().__init__(name, health, damage)
        self.__ability = ability

