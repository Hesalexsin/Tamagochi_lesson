class Tamagochi:
    def __init__(self, name="Красавчик", health=80, hunger=10, energy=70, happiness=20, existence = 'alive'):
        self.name = name
        self.health = health
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.existence = existence

        pass

    def eat():
        pass

    def die():
        pass

    def sleep():
        pass

    def ability():
        pass

    def walk():
        pass


class Real(Tamagochi):
    pass


class Unreal(Tamagochi):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        mana = 100

    def dO_MaGiC(self):
        pass


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


def acquaintance():
    print("Привет. Это Тамагочи, твой виртцальный питомец.")
    name = input("Как ты назовёшь своего друга?")
    t = 1
    while t:
        chose = input("Кого ты выбираешь? Кошку или собаку? ")
        if chose == "Кошку":
            t = 0
            return Cats(name)
        elif chose == "Собаку":
            t = 0
            return Dogs(name)
        elif chose == "Дракона":
            t = 0
            return Dragons(name)
        else:
            t = 1
            print(f"Извини не расслышал :) Давай попробуем ещё раз. Просто напиши 'Кошку' или 'Собаку'.")

def life():
  pass

def play():
    print(1)
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

#print(cat)
play()
#start()