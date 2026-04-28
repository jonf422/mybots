import solutionA
import solutionB
import constants as c
import copy
import numpy as np

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        self.Create_World() #Frozen Noise
        self.parentsA = {}
        self.parentsB = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parentsA[i] = solutionA.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        for i in range(c.populationSize):
            self.parentsB[i] = solutionB.SOLUTION(self.nextAvailableID)
            self.nextAvailableID +=1
        
        self.fitnessMatrixA = np.zeros((c.populationSize, c.numberOfGenerations))
        self.fitnessMatrixB = np.zeros((c.populationSize, c.numberOfGenerations))
    
    def Create_World(self):
        import pyrosim.pyrosim as ps
        import random
        ps.Start_SDF(f"world.sdf")

        for i in range(-10,1):
            for j in range(-5,5):
                if random.random() < .2:
                    ps.Send_Cube(name="Box", pos=[i,j,.5], size=[1,1,1])
        ps.End()

    def Evaluate(self, solutions, mode):
        for i in solutions:
            solutions[i].Start_Simulation(mode)
        
        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()

    def Evolve(self, mode):
            self.Evaluate(self.parentsA, mode)
            self.Evaluate(self.parentsB, mode)

            for currentGeneration in range(c.numberOfGenerations):
                self.Evolve_For_One_Generation("DIRECT", currentGeneration)
            
            # Save fitness matrices for both variants
            np.savetxt("fitnessMatrix_A.txt", self.fitnessMatrixA)
            np.save("fitnessMatrix_A.npy", self.fitnessMatrixA)
            np.savetxt("fitnessMatrix_B.txt", self.fitnessMatrixB)
            np.save("fitnessMatrix_B.npy", self.fitnessMatrixB)
            print("Fitness matrices saved for A and B.")

    def Evolve_For_One_Generation(self, mode, currentGeneration):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.childrenA, mode)
        self.Evaluate(self.childrenB, mode)
        self.Record_Fitness(currentGeneration)
        self.Print()
        self.Select()

    def Spawn(self):
        self.childrenA = {}
        self.childrenB = {}

        for i in self.parentsA.keys():
            self.childrenA[i] = copy.deepcopy(self.parentsA[i])
            self.childrenA[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        
        for i in self.parentsB.keys():
            self.childrenB[i] = copy.deepcopy(self.parentsB[i])
            self.childrenB[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    def Mutate(self):
        for i in self.childrenA.keys():
            self.childrenA[i].Mutate()
        for i in self.childrenB.keys():
            self.childrenB[i].Mutate()

    def Select(self):
        for key in self.parentsA.keys():
            if self.parentsA[key].fitness < self.childrenA[key].fitness:
                self.parentsA[key] = self.childrenA[key]

        for key in self.parentsB.keys():
            if self.parentsB[key].fitness < self.childrenB[key].fitness:
                self.parentsB[key] = self.childrenB[key]

    def Record_Fitness(self, currentGeneration):
        for i in self.childrenA.keys():
            self.fitnessMatrixA[i, currentGeneration] = max(self.parentsA[i].fitness, self.childrenA[i].fitness)
        for i in self.childrenB.keys():
            self.fitnessMatrixB[i, currentGeneration] = max(self.parentsB[i].fitness, self.childrenB[i].fitness)

    def Print(self):
        print("\n--- Population A ---")
        for key in self.parentsA.keys():
            print(f"Parent fitness: {self.parentsA[key].fitness:.4f} | Child fitness: {self.childrenA[key].fitness:.4f}")

        print("\n--- Population B ---")
        for key in self.parentsB.keys():
            print(f"Parent fitness: {self.parentsB[key].fitness:.4f} | Child fitness: {self.childrenB[key].fitness:.4f}")


    def Show_Best(self):
        bestA = max(self.parentsA.values(), key=lambda p: p.fitness)
        bestB = max(self.parentsB.values(), key=lambda p: p.fitness)

        print(f"\nBest A fitness: {bestA.fitness:.4f}")
        print(f"Best B fitness: {bestB.fitness:.4f}")

        print("Showing best A...")
        bestA.Start_Simulation("GUI")

        print("Showing best B...")
        bestB.Start_Simulation("GUI")
        