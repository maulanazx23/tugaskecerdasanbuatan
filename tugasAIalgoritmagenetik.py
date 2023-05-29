import random

a_lower_bound = 0
a_upper_bound = 30
bcd_lower_bound = 0
bcd_upper_bound = 10

population_size = 6
chromosome_length = 4
crossover_rate = 0.8
mutation_rate = 0.1
max_generations = 100

def generate_chromosome():
    chromosome = [random.randint(a_lower_bound, a_upper_bound)]
    for _ in range(chromosome_length - 1):
        chromosome.append(random.randint(bcd_lower_bound, bcd_upper_bound))
    return chromosome

def evaluate_chromosome(chromosome):
    equation_result = chromosome[0] + 4 * chromosome[1] + 2 * chromosome[2] + 3 * chromosome[3]
    fitness = abs(equation_result - 30)
    return fitness

def selection(population):
    fitness_values = [1 / (1 + evaluate_chromosome(chromosome)) for chromosome in population]
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    
    selected_parents = []
    for _ in range(len(population)):
        random_number = random.random()
        for i in range(len(cumulative_probabilities)):
            if random_number < cumulative_probabilities[i]:
                selected_parents.append(population[i])
                break
    
    return selected_parents

def crossover(parent1, parent2):
    crossover_point = random.randint(1, chromosome_length - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(chromosome):
    mutated_chromosome = chromosome[:]
    gene_to_mutate = random.randint(0, chromosome_length - 1)
    if gene_to_mutate == 0:
        mutated_chromosome[gene_to_mutate] = random.randint(a_lower_bound, a_upper_bound)
    else:
        mutated_chromosome[gene_to_mutate] = random.randint(bcd_lower_bound, bcd_upper_bound)
    return mutated_chromosome

def genetic_algorithm():
    population = [generate_chromosome() for _ in range(population_size)]

    for generation in range(max_generations):

        fitness_values = [evaluate_chromosome(chromosome) for chromosome in population]
        

        if 0 in fitness_values:
            index = fitness_values.index(0)
            solution = population[index]
            print("Solution found in generation", generation)
            print("Chromosome:", solution)
            return solution
        
        parents = selection(population)
        
        offspring = []
        for i in range(0, len(parents), 2):
            if random.random() < crossover_rate:
                child1, child2 = crossover(parents[i], parents[i+1])
                offspring.extend([child1, child2])
                
        for i in range(len(offspring)):
            if random.random() < mutation_rate:
                offspring[i] = mutation(offspring[i])
        
        population = parents + offspring

    print("Solution not found")
    return None

genetic_algorithm()