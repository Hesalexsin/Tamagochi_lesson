class Tamagochi:
    def __init__(self, name="Красавчик", health=80, hunger=10, energy=70, happiness=20, existence = True):
        self.name = name
        self.health = health
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.existence = existence



    def feed(self):
        food = {meat.name: meat, fish.name : fish, sun_fruit.name: sun_fruit}
        meal = input(f"Чем кормим?{food.keys()}")
        while not (meal in food):
            meal = input(f"Не понял. Ещё раз. \n Чем кормим?{food.keys()}")
        self.hunger = self.hunger + food[meal].saturation_level
        print('ом ном ном')

    def die(self):
        self.existence = False

    def sleep():
        pass

    def ability():
        pass

    def walk():
        pass

    def life(self):
        while self.existence:
            """actions = {"Умереть":  self.die(),"Кормить":  self.feed()}
            ans = input(f"Что будем делать?\n {actions.keys()}")
            while not (ans in actions):
                ans = input(f"Не понял. Ещё раз. \n Что будем делать?\n {actions.keys()}")
            self.get"""
            ans = input(f"Что будем делать?\n Кормить \n Умереть\n")
            while True:
                if ans == "Умереть":
                    self.die()
                    break
                elif ans == "Кормить":
                    self.feed()
                    break
                else:
                    ans = input(f"Не понял. Ещё раз. \n Что будем делать?\n Кормить \n Умереть\n")





class Real(Tamagochi):
    pass


class Unreal(Tamagochi):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.mana = 100

    def dO_MaGiC(self):
        pass
    def eat(self, *args, **kwargs):
        super().eat(*args, *kwargs)
        self.mana = self.mana + up_mana


class Cats(Real):
    pass


class Dogs(Real):
    pass


class Dragons(Unreal):
    def ability():
        pass



class Food:
      def __init__(self, name="Картоха", saturation_level=5, mana_return = 0 ):
        self.name = name
        self.saturation_level = saturation_level
        self.mana_return = mana_return

fish = Food("Рыба", 5)
meat = Food("Мясо", 5)
sun_fruit = Food("Солнечный фрукт", 0, 10)


def acquaintance():
    name = input("Привет. Это Тамагочи, твой виртуальный питомец.\nКак ты назовёшь своего друга?")
    pets = {"Кошку": Cats(name), "Собаку": Dogs(name), "Дракона": Dragons(name)}
    while True:
        chose = input("Кого ты выбираешь? Кошку или собаку? ")
        if chose in pets:
            return pets[chose]
        else:
            print(f"Извини не расслышал :) Давай попробуем ещё раз. Просто напиши 'Кошку' или 'Собаку'.")





def play():
    #print(1)
    pet = acquaintance()
    if type(pet) == Cats:
        print(CAT)
    print(f"Познакомься! Это {pet.name}")
    pet.life()




CAT = r"""
      \         /\/\    
       \ ______- 0 0-
        _|_|_|_\  ^
        ||    |\
"""


play()
