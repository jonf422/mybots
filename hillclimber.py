import solution
import constants as c
import copy

class HILL_CLIMBER:

    def __init__(self):
        self.parent = solution.SOLUTION()

    def Evolve(self, mode):
        self.parent.Evaluate(mode)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation("DIRECT")

    def Evolve_For_One_Generation(self, mode):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(mode)
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print(f"\nparent: {self.parent.fitness} child: {self.child.fitness}\n")

    def Show_Best(self):
        self.parent.Evaluate("GUI")
        