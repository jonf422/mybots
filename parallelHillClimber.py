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

    def Evaluate(self, solutions, mode):
        for i in solutions:
            solutions[i].Start_Simulation(mode)
        
        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()

    def Evolve(self, mode):
            self.Evaluate(self.parents, mode)

            for currentGeneration in range(c.numberOfGenerations):
                self.Evolve_For_One_Generation("DIRECT")

    def Evolve_For_One_Generation(self, mode):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children, mode)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children.keys():
            self.children[i].Mutate()

    def Select(self):
        for key in self.parents.keys():
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        for key in self.parents.keys():
            print(f"\nParent's fitness: {self.parents[key].fitness}, Child's fitness:, {self.children[key].fitness}\n")

    def Show_Best(self):
        lowestFitnessParent = min(self.parents.values(), key=lambda parent: parent.fitness)
        lowestFitnessParent.Start_Simulation("GUI")
        