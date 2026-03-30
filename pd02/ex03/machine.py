import random
import beverages as b

class CoffeeMachine:

    def __init__(self):
        self.broken = False
        self.drink_count = 0

    class EmptyCup(b.HotBeverage):
        name = "empty cup"
        price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"
        
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.broken = False
        self.drink_count = 0
        
    def serve(self, drink):
        if self.broken:
            raise self.BrokenMachineException()
        
        self.drink_count += 1
        if self.drink_count == 10:
            self.broken = True

        if random.choice([True, False]):
            return drink
        else:
            return self.EmptyCup()
        

if __name__ == '__main__':
    machine = CoffeeMachine()
    for i in range(23):
        try:
            drinks = [b.Coffee(), b.Tea(), b.Chocolate(), b.Cappuccino()]
            drink = random.choice(drinks)
            
            print(f"\033[35m{i + 1}. Ordered drink: {drink.name}\033[0m")
            drink_machine = machine.serve(drink)
            print(f"Picked drink:\n{drink_machine}\n")

        except CoffeeMachine.BrokenMachineException as e:
            print(f"\033[31mException: {e}")
            machine.repair()
            print(".\n.\n.\n\033[32mMachine repaired!\033[0m\n")