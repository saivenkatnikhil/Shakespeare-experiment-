import random
# function based genetic algorithm

target_text = 'andromeda'
population_size = 501
mutation_rate = 0.01


# DNA object

def DNA():
    return None

def gene(length):

    genes = []

    for i in range(length):
        genes.append(chr(random.randint(0,150)))

    return genes

def fitness(target,length):
    score = 0
    fitness_val = 0
    genes_arr = gene(length)

    target_val = target

    for i in range(len(genes_arr)):

        if genes_arr[i] == target_val[i]:
            score += 1

    fitness_val = score / len(target_val)

    return fitness_val

    
def crossover(partner,partner2,length):

    dummy_child = []
    #midpoint = random.randint(0,len())
    gene_arr = gene(length)
    midpoint = random.randint(0,len(gene_arr)-1)

    dummy_child[0:midpoint] = partner[0:midpoint]
    dummy_child[midpoint:] = partner2[midpoint:]

    return dummy_child

def mutate(mutationrate,partner,partner2,length):

    child = crossover(partner,partner2,length)

    for i in range(len(partner)):

        if random.random() < mutationrate:

            child[i] = chr(random.randint(0,150))

    return child

def get_phrase(gene_arr,length):

    gene_arr = gene(length)

    return ''.join(gene_arr)

# ----------------------------------------------------------------------------------------

#testing functions

# genes = gene(len(target_text))
# #print(genes)
# fit_val = fitness(target_text,len(genes))

# #print(fit_val)

# crossed_child = crossover(target_text,len(genes))

# #print(crossed_child)

    
# mutated_child = mutate(mutation_rate,target_text,len(genes))

# #print(mutated_child)

# final_phrase = get_phrase(genes,len(genes))

# print(final_phrase)

'''
tested all the genetic operators of the DNA operators, now it's time for population object to apply all the 
genetic operators on the problem

'''
# population object

def population_creation(target):

    # create the population

    population_arr = []
    length = len(target)

    for i in range(15):

        population_arr.append(gene(length))

    return population_arr


#print(population_creation(target_text))

def fit_pop(target,length):

    population = population_creation(target)

    target = target

    length = len(target)
    fitness_arr = []
    for i in range(len(population)):

        fitness_arr.append( fitness(population[i],length) )

    return fitness_arr

#print(fit_pop(target_text,len(target_text)))

def select_pop(fitness_array,sucess_population,target):

    mating_pool = []

    fitness_values = fitness_array

    population = sucess_population(target)

    for i in range(len(fitness_array)):

        n = int(fitness_array[i] * 100)

        for i in range(n):

            mating_pool.append(population[i])

    return mating_pool 

mating = select_pop(
    fit_pop(target_text,len(target_text)),
    population_creation,
    target_text
)

#print(mating)
 
def generation(sucess_population,mutationrate,target):

    generation_val = 0
    pop = sucess_population(target)
    rate = mutationrate
    for i in range(len(pop)-1):

        parents = random.choices(mating,k=2)

        #assert len(parents[0]) == len(parents[1])
        
        crossed_child = crossover(parents[0],parents[1],len(target))

        mutated_child = mutate(rate,parents[0],parents[1],len(target))
        
        pop[i] = mutated_child
     
    generation_val += 1 

    print(generation_val)
    
finished = True

def get_best_phrase(sucess_population,fit_func,target):
    global finished
    threshold_fitness = 0
    best_index = 0
    pop = sucess_population(target)
    for i in range(len(pop)):

        if fit_func(target,len(pop[i]))[i] > threshold_fitness:

            threshold_fitness = fit_func(target,len(pop[i]))[i]
            best_index = i
    
    print(''.join(pop[best_index]))

    if ''.join(pop[best_index]) == target:
        finished = True


pop = population_creation(target_text)

while finished:
    fit_pop(target_text,len(target_text))
    select_pop(
        #d
        fit_pop(target_text,len(target_text)),
        population_creation,
        target_text
    )
    generation(population_creation,mutation_rate,target_text) 
    get_best_phrase(population_creation,fit_pop,target_text)

    

