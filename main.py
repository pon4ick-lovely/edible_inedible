

class Animal:
    """
    A class representing an animal.
    Attributes
    ----------
    alive : bool
        Indicates whether the animal is alive. Default is True.
    fed : bool
        Indicates whether the animal has been fed. Default is False.
    Methods
    -------
    __init__(self, name: str)
        Initializes an animal with a given name.
    """
    alive = True    # (живой)
    fed = False     # (накормленный)

    def __init__(self, name: str):
        """
        Initializes an animal with a given name.
        Parameters
        ----------
        name : str
            The name of the animal.
        """
        self.name = name


class Plant:
    """
    A class representing a plant.

    Attributes
    ----------
    edible : bool
        Indicates whether the plant is edible. Default is False.
    name : str
        The name of the plant.

    Methods
    -------
    __init__(self, name: str)
        Initializes a plant with a given name.
    """

    edible = False  # (съедобность)

    def __init__(self, name: str):
        """
        Initializes a plant with a given name.

        Parameters
        ----------
        name : str
            The name of the plant.
        """
        self.name = name

class Mammal(Animal):
    """
    A class representing a mammal, inheriting from the Animal class.
    """

    def eat(self, food):
        """
        Simulates the mammal eating food.

        This method checks if the given food is edible. If it is, the mammal eats it
        and becomes fed. If not, the mammal refuses to eat it and dies.

        Parameters
        ----------
        food : Plant
            The food object that the mammal attempts to eat.

        Returns
        -------
        None

        Side Effects
        ------------
        - If the food is edible:
            - Prints a message indicating the mammal ate the food.
            - Sets the 'fed' attribute to True.
        - If the food is not edible:
            - Prints a message indicating the mammal refused to eat the food.
            - Sets the 'alive' attribute to False.
        """
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
class Predator(Animal):
    """
    A class representing a predator, inheriting from the Animal class.
    """

    def eat(self, food):
        """
        Simulates the predator eating food.

        This method checks if the given food is edible. If it is, the predator eats it
        and becomes fed. If not, the predator refuses to eat it and dies.

        Parameters
        ----------
        food : Plant
            The food object that the predator attempts to eat.

        Returns
        -------
        None

        Side Effects
        ------------
        - If the food is edible:
            - Prints a message indicating the predator ate the food.
            - Sets the 'fed' attribute to True.
        - If the food is not edible:
            - Prints a message indicating the predator refused to eat the food.
            - Sets the 'alive' attribute to False.
        """
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Flower(Plant):
    pass
 #   edible = True

class Fruit(Plant):
    edible = True



animal1 = Predator('Tiger')
animal2 = Mammal('Bull')
plant1 = Plant('Rose')
plant2 = Fruit('Apple')

print(animal1.name)
print(plant1.name)

print(animal1.alive, f'- {animal1.name} живой')
print(animal2.fed, f'- {animal2.name} голоден')

animal1.eat(plant1)
animal2.eat(plant2)
print(animal1.alive, f'- {animal1.name} помер')
print(animal2.fed, f'- {animal2.name} сыт')