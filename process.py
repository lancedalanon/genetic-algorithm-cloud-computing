import random
import time
from deap import base, creator, tools

# Define the problem (maximization of a simple objective function)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Initialize genetic algorithm parameters
NGEN = 10  # Number of generations
POP_SIZE = 50  # Population size
MUTPB = 0.2  # Mutation probability
CXPB = 0.5  # Crossover probability

def eval_function(individual):
    """Objective function to maximize."""
    return sum(individual),  # The tuple is required for DEAP

def run_genetic_algorithm():
    """Run the genetic algorithm and return performance metrics."""
    # Initialize the toolbox
    toolbox = base.Toolbox()
    toolbox.register("attr_float", random.uniform, 0, 10)  # Attributes are floats between 0 and 10
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, 5)  # 5 genes
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", eval_function)
    toolbox.register("mate", tools.cxBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    # Create the population
    population = toolbox.population(n=POP_SIZE)

    # Run the GA
    for gen in range(NGEN):
        # Select the next generation individuals
        offspring = toolbox.select(population, len(population))
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover and mutation
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # Replace the old population by the offspring
        population[:] = offspring

    # Get the best individual
    best_ind = tools.selBest(population, 1)[0]
    
    performance_metrics = {
        "best_solution": best_ind,
        "fitness_value": best_ind.fitness.values[0],
        "generations": NGEN
    }
    return performance_metrics
