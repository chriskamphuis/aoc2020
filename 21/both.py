from collections import defaultdict

allergen_ingredients_map = defaultdict(list)
ingredients_allergen_map = defaultdict(set)
all_ingredients = set()
all_ingredients_list = list()

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()[:-1]
        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split(' ')
        allergens = allergens.split(', ')
        all_ingredients |= set(ingredients)
        for allergen in allergens:
            allergen_ingredients_map[allergen].append(ingredients)
        all_ingredients_list.append(ingredients)

invalid = set()
for allergen, ingredients in allergen_ingredients_map.items():
    start = set(ingredients[0])
    for ingredient in ingredients[1:]:
        start &= set(ingredient) 
    for ingredient in start:    
        ingredients_allergen_map[ingredient].add(allergen) 
    invalid |= start

valid = all_ingredients ^ invalid
count = 0
for all_ingredients in all_ingredients_list:
    for ingredient in all_ingredients:
        if ingredient in valid:
            count += 1
# Part 1
print(count)

done = []
while True:
    for k, v in ingredients_allergen_map.items():
        if len(v) == 1:
            found = v.pop()
            done.append([k, found])
            break
    else:
        break
    del ingredients_allergen_map[k]
    for k, v in ingredients_allergen_map.items():
        v.discard(found)

# Part 2
print(','.join([e[0] for e in sorted(done, key=lambda x: x[1])]))
