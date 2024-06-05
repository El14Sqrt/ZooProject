import unittest
from unittest import TestCase
from src.zoo import Zoo, ZooKeeper, Animal, Fence

class TestZoo(TestCase):

    def test_animal_dimension(self):
        #controllo che animali troppo grandi non vengono aggiunti alla fence

        zookeeper_1: ZooKeeper = ZooKeeper (name= "Claudia", surname="Micci", id="456")
        fence_1: Fence = Fence(area=150, temperature=23.1, habitat="giungla")
        animal_1: Animal = Animal(name="Giò", species="drago", age=15, height=90.0, width=10.0, preferred_habitat="giungla")

        zookeeper_1.add_animal(animal_1, fence_1)
        result: int = len(fence_1.animals)
        message: str = f"Squarti: Error: the funcion add_animal should not add self.animal_1 into self.fence_1"

        self.assertEqual(result, 0, message)
    
    def test_animal_habitat(self):
        #controllo che animali troppo con habitat diversi da quello della fence non vengono aggiunti alla fence

        zookeeper_1: ZooKeeper = ZooKeeper (name= "Claudia", surname="Micci", id="456")
        fence_1: Fence = Fence(area=150, temperature=16.1, habitat="lago")
        animal_1: Animal = Animal(name="Giò", species="drago", age=15, height=3.0, width=2.0, preferred_habitat="giungla")

        zookeeper_1.add_animal(animal_1, fence_1)
        result: int = len(fence_1.animals)
        message: str = f"Squarti: Error: the funcion add_animal should not add self.animal_1 into self.fence_1"

        self.assertEqual(result, 0, message)

    def test_animal_add(self):

        zookeeper_1: ZooKeeper = ZooKeeper (name= "Claudia", surname="Micci", id="456")
        fence_1: Fence = Fence(area=150, temperature=23.1, habitat="giungla")
        animal_1: Animal = Animal(name="Giò", species="drago", age=15, height=3.0, width=2.0, preferred_habitat="giungla")

        zookeeper_1.add_animal(animal_1, fence_1)
        result: int = len(fence_1.animals)
        message: str = f"Squarti: Error: the funcion add_animal do not add self.animal_1 into self.fence_1"

        self.assertEqual(result, 0, message)

    def test_animal_remove(self):

        zookeeper_1: ZooKeeper = ZooKeeper (name= "Claudia", surname="Micci", id="456")
        fence_1: Fence = Fence(area=150, temperature=23.1, habitat="giungla")
        animal_1: Animal = Animal(name="Giò", species="drago", age=15, height=3.0, width=2.0, preferred_habitat="giungla")

        zookeeper_1.add_animal(animal_1, fence_1)
        result_A: int = len(fence_1.animals)

        zookeeper_1.remove_animal(animal_1, fence_1)
        result_B: int = len(fence_1.animals)
        message: str = f"Squarti: Error: the funcion remove_animal do not remove self.animal_1 from self.fence_1"

        if self.assertEqual(result_A, result_B, message) == False: 
            return "Animal removed"
        
        
