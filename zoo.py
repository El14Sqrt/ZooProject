#Sistema di gestione dello zoo virtuale

class Animal:
    def __init__(self, name:str, species:str, age:float, height:float, width:float, preferred_habitat:str):
        self.name=name
        self.species=species
        self.age=age
        self.height=height
        self.width=width
        self.preferred_habitat=preferred_habitat
        self.healt=round(100 * (1 / age), 3) 
        self.area_animal: float = self.height * self.width
        self.gabbia = None



class Fence:
    def __init__(self, area:float, temperature:float, habitat:str):
        self.area=area #diminuisce ogni volta che faccio add_animal
        self.temperature=temperature
        self.habitat=habitat
        self.animals: list = []
        self.total_area: float = area #perchè dopo in clean mi serve l'area iniziale
        


class ZooKeeper:
    def __init__(self, name:str, surname:str, id:str):
        self.name=name
        self.surname=surname
        self.id=id
    

    def add_animal(self, animal: Animal, fence: Fence):   #controllo habitat -> controllo area animale
        if animal.preferred_habitat == fence.habitat and animal.area_animal <= fence.area: 
            fence.animals.append(animal)
            fence.area -= animal.area_animal
            animal.gabbia = fence



    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area += animal.area_animal



    def clean(self, fence: Fence):
        clean_time: float =  (fence.total_area - fence.area) / fence.area
        if  fence.area == 0:
            return fence.total_area
        else:
            return clean_time



    def feed(self, animal: Animal):
        if animal.gabbia.area + animal.area_animal >= (animal.height + (animal.height * 0.02)) * (animal.width + (animal.width * 0.02)):
            animal.healt += (animal.healt*1/100)
            animal.height += (animal.height*2/100)
            animal.width += (animal.width*2/100)
            animal.area_animal = animal.width * animal.height
    


class Zoo:
    def __init__(self, fences:list[Fence], zoo_keepers:list[ZooKeeper]):
        self.fences=fences
        self.zoo_keepers=zoo_keepers
    
    
    def describe_zoo(self):
        print("Guardians:")
        for zk in self.zoo_keepers:
            print(f"ZooKeeper(name={zk.name}, surname={zk.surname}, id={zk.id})")
        print("\nFences:")
        for f in self.fences:
            if f.animals != []:
                print(f"Fence(area={f.area}, temperature={f.temperature}, habitat={f.habitat})")
                print("\nwith animals:")
                for a in f.animals:
                    print(f"Animal(name={a.name}, species={a.species}, age={a.age})\n")
                print("#" * 30)






#TEST CASE 1: Aggiunta di un Animale a un Recinto Adeguato

zoo_keeper = ZooKeeper(name="Mario", surname="Rossi", id="001")
fence = Fence(area=50.0, temperature=20.0, habitat="Savana")
animal = Animal(name="Simba", species="Leone", age=3, height=1.2, width=2.0, preferred_habitat="Savana")
zoo_keeper.add_animal(animal, fence)

#TEST CASE 2: Aggiunta di un Animale a un Recinto Inadeguato (Habitat)

zoo_keeper = ZooKeeper(name="Mario", surname="Rossi", id="001")
fence = Fence(area=50.0, temperature=20.0, habitat="Foresta")
animal = Animal(name="Simba", species="Leone", age=3, height=1.2, width=2.0, preferred_habitat="Savana")
zoo_keeper.add_animal(animal, fence)

#TEST CASE 3: Rimozione di un Animale da un Recinto

zoo_keeper = ZooKeeper(name="Mario", surname="Rossi", id="001")
fence = Fence(area=50.0, temperature=20.0, habitat="Savana")
animal = Animal(name="Simba", species="Leone", age=3, height=1.2, width=2.0, preferred_habitat="Savana")
zoo_keeper.add_animal(animal, fence)
zoo_keeper.remove_animal(animal, fence)

#TEST CASE 4: Pulizia di un Recinto con Animali

zoo_keeper = ZooKeeper(name="Mario", surname="Rossi", id="001")
fence = Fence(area=50.0, temperature=20.0, habitat="Savana")
animal = Animal(name="Simba", species="Leone", age=3, height=1.2, width=2.0, preferred_habitat="Savana")
zoo_keeper.add_animal(animal, fence)
clean_time = zoo_keeper.clean(fence)

#TEST CASE 5: Alimentazione di un Animale (Crescita e Salute)

zoo_keeper = ZooKeeper(name="Mario", surname="Rossi", id="001")
fence = Fence(area=50.0, temperature=20.0, habitat="Savana")
animal = Animal(name="Simba", species="Leone", age=3, height=1.2, width=2.0, preferred_habitat="Savana")
zoo_keeper.add_animal(animal, fence)
zoo_keeper.feed(animal)

#TEST CASE 6: Descrizione dello Zoo

zoo_keeper = ZooKeeper(name="Mario", surname="Rossi", id="001")
fence = Fence(area=50.0, temperature=20.0, habitat="Savana")
animal = Animal(name="Simba", species="Leone", age=3, height=1.2, width=2.0, preferred_habitat="Savana")
zoo_keeper.add_animal(animal, fence)
zoo = Zoo(fences=[fence], zoo_keepers=[zoo_keeper])
zoo.describe_zoo()

#TEST CASE 7: Aggiunta di Animali Multipli allo Stesso Recinto

zoo_keeper = ZooKeeper(name="Mario", surname="Rossi", id="001")
fence = Fence(area=50.0, temperature=20.0, habitat="Savana")
animal1 = Animal(name="Simba", species="Leone", age=3, height=1.2, width=2.0, preferred_habitat="Savana")
animal2 = Animal(name="Nala", species="Leone", age=4, height=1.1, width=1.8, preferred_habitat="Savana")
zoo_keeper.add_animal(animal1, fence)
zoo_keeper.add_animal(animal2, fence)

#TEST CASE 8: Pulizia di un Recinto Vuoto

zoo_keeper = ZooKeeper(name="Mario", surname="Rossi", id="001")
fence = Fence(area=50.0, temperature=20.0, habitat="Savana")
clean_time = zoo_keeper.clean(fence)

#TEST CASE 9: Rimozione di un Animale da un Recinto Vuoto

zoo_keeper = ZooKeeper(name="Mario", surname="Rossi", id="001")
fence = Fence(area=50.0, temperature=20.0, habitat="Savana")
animal = Animal(name="Simba", species="Leone", age=3, height=1.2, width=2.0, preferred_habitat="Savana")
zoo_keeper.remove_animal(animal, fence)

#TEST CASE 10: Alimentazione di un Animale Senza Spazio Sufficiente

zoo_keeper = ZooKeeper(name="Mario", surname="Rossi", id="001")
fence = Fence(area=4.8, temperature=20.0, habitat="Savana")
animal = Animal(name="Simba", species="Leone", age=3, height=2.0, width=2.0, preferred_habitat="Savana")
zoo_keeper.add_animal(animal, fence)
zoo_keeper.feed(animal)

