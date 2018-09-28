from Algorithms import BoardHandler, Checker
from IO import Printer, Parser
from random import randint
import copy


maxPopulation = 100

class Chromosome() :

	def __init__(self) :
		self.board = []
		self.piecesLocation = []
		self.fitness = 0


def initialize_population(chessList): #initialize the population
	population = []
	for i in range(100) :
		chromosome = Chromosome()
		chromosome.board = []
		chromosome.piecesLocation = BoardHandler.random_genetic(chromosome.board, chessList)
		chromosome.fitness = Checker.conflictChecker(chromosome.board)[0]
		
		population.append(chromosome)

	Printer.printChessBoard(population[0].board)
	print(population[0].piecesLocation)
	print(population[0].fitness)

	return population

def getFitness(chromosome) : #function to help sort
	return chromosome.fitness

def populationSort(population) : #sort population from best fit to least fit
	population.sort(key=getFitness)

def getParents(population, index) : #get parents from the surviving population
	parent1 = population[index]
	i = index + 1
	parent2 = population[i]
	while (i < len(population) - 1) and samePosition(parent1,parent2) :
		i = i + 1
		parent2 = population[i]

	return parent1, parent2


def samePosition(chromosome1 , chromosome2) : # check whether there are pieces with same position in chromosome 1 and 2
	for i in range(len(chromosome1.piecesLocation)) :
		for j in range(len(chromosome1.piecesLocation)) :
			if (chromosome1.piecesLocation[i][0] == chromosome2.piecesLocation[j][0]) :
				return True
	
	return False 

def deleteLeastFit(population) : # remove the  least fit chromosome from population so that only half of the population remaining
	del population[int(maxPopulation/2):]

def crossOver(population, parent1, parent2) : #reproduce new chromosome 
	mutationConstant = randint(1,10) 


	crossBorder = randint(1, len(parent1.piecesLocation) - 1)

	child1 = copy.deepcopy(parent1)
	child2 = copy.deepcopy(parent2)
	for i in range(crossBorder) :
		temp = child1.piecesLocation[i]
		child1.piecesLocation[i] = child2.piecesLocation[i]
		child2.piecesLocation[i] = temp

	if (mutationConstant > 3) : #have 70% chance of mutation
		if (randint(1,2) == 0) :
			mutation(child1)
		else :
			mutation(child2)

		# print("mutation")


	updateBoardandFitness(child1)
	updateBoardandFitness(child2)
	population.append(child1)
	population.append(child2)



def mutation(child) : #mutation function 
		BoardHandler.updateBoard(child.board, child.piecesLocation)
		member = randint(0,len(child.piecesLocation)-1)
		row = randint(0,7)
		col = randint(0,7)
		while child.board[row][col] != ('.',".") :
			row = randint(0,7)
			col = randint(0,7)
		
		child.piecesLocation[member][0][0] = row
		child.piecesLocation[member][0][1] = col


def updateBoardandFitness(child) : #update chromosome board and fitness score after cross over
	BoardHandler.updateBoard(child.board, child.piecesLocation)
	child.fitness = Checker.conflictChecker(child.board)[0]

def GeneticAlgorithm(chessList): #the process of genetic algorithm
	population = initialize_population(chessList)

	# for chromosome in population :
	# 	print(chromosome.fitness)
	i = 1
	while (population[0].fitness != 0) :
		
		print("Generation :",i)
		
		populationSort(population)
		deleteLeastFit(population)
		
		# for chromosome in population :
		# 	print(chromosome.fitness)
		# 	print("===============")
		# 	print("PieceList")
		# 	print(chromosome.piecesLocation)

		# print("Crossover")
		# print("===============")
		
		index = 0
		while index < maxPopulation/2 :
			parent1 , parent2 = getParents(population, index)
			if not(samePosition(parent1, parent2)) :
				crossOver(population, parent1, parent2)

			index = index + 2

		# index = 0
		# parent1 , parent2 = getParents(population, index)
		# crossOver(population, parent1, parent2)

		populationSort(population)
		print("Fittest : ", population[0].fitness)
		# for chromosome in population :
		# 	print(chromosome.fitness)
		# for chromosome in population :
		# 	Printer.printChessBoard(chromosome.board)
		# 	

		# populationSort(population)
		i = i + 1


	print (population[0].piecesLocation)
	# BoardHandler.updateBoard(population[0].board, population[0].piecesLocation)
	Printer.printChessBoard(population[0].board)


chessList = Parser.readPiecesFile("Inputs/" + input(">> Enter filename: "))

GeneticAlgorithm(chessList)