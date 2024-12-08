#Part 1------------------------------------
# Create a Genetic Algorithm that given the following chromosome:Pi=[10010111001010010011000000011010] (32 bits long) 

import random

# Given initial chromosome and target solution
initial_chromosome = "10010111001010010011000000011010"
target_solution = "11111111111111111111111111111111"

# Set population size and mutation rate
population_size = 200
mutation_rate = 0.01

# Function to generate random initial population
def generate_population(size, chromosome_length):
    return [''.join([str(random.randint(0, 1)) for _ in range(chromosome_length)]) for _ in range(size)]

# Function to calculate fitness (number of matching genes)
def calculate_fitness(chromosome):
    return sum(1 for a, b in zip(chromosome, target_solution) if a == b)

# Function for single-point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Function for mutation
def mutate(chromosome, mutation_rate):
    mutated_chromosome = ''
    for bit in chromosome:
        if random.random() < mutation_rate:
            mutated_chromosome += '1' if bit == '0' else '0'
        else:
            mutated_chromosome += bit
    return mutated_chromosome

# Genetic Algorithm
def genetic_algorithm(initial_chromosome, target_solution, population_size, mutation_rate):
    generation = 1
    population = generate_population(population_size, len(initial_chromosome))
    
    while True:
        # Calculate fitness scores for each individual in the population
        fitness_scores = [calculate_fitness(chromosome) for chromosome in population]
        max_fitness = max(fitness_scores)
        best_solution = population[fitness_scores.index(max_fitness)]

        # Termination condition if target solution is found
        if max_fitness == len(target_solution):
            print(f"Solution found in generation {generation}: {best_solution}")
            break
        
        # Selection, crossover, and mutation
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = random.choices(population, weights=fitness_scores, k=2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population
        generation += 1


# Run the Genetic Algorithm
genetic_algorithm(initial_chromosome, target_solution, population_size, mutation_rate)
