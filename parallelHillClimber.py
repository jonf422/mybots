import solution
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self, mode):
        for parent in self.parents:
            self.parents[parent].Start_Simulation(mode)
        
        for parent in self.parents:
            self.parents[parent].Wait_For_Simulation_To_End()

            #for currentGeneration in range(c.numberOfGenerations):
                #self.Evolve_For_One_Generation("DIRECT")

    def Evolve_For_One_Generation(self, mode):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(mode)
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print(f"\nparent: {self.parent.fitness} child: {self.child.fitness}\n")

    def Show_Best(self):
        self.parent.Evaluate("GUI")
        