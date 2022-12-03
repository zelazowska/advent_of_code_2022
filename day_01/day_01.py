def get_elve_calories():
    
    file = open(r"day_01\input_01.txt", "r")
    current_elf_calories = 0
    elves_calorie_sum = []
    
    for line in file:
        if line != f'\n':
            current_elf_calories += int(line) #do until crossing a blank line
        else:
            elves_calorie_sum.append(current_elf_calories)
            current_elf_calories = 0
        
    #For Part 1: which elf is carrying the most calories, and how many
    max_calorie_sum = max(elves_calorie_sum)
    elf_with_max_calories = elves_calorie_sum.index(max_calorie_sum)
    #For Part 2: sum of calories carried by top 3 elves on the calorie sum ladder
    max_calorie_sum_list = sorted(elves_calorie_sum) 
    elves_with_max_calories = sum(max_calorie_sum_list[-3:]) #get last 3 records (3 highest numbers)
        
    print(f"Part one: Elf number {elf_with_max_calories} is carrying {max_calorie_sum} calories.")
    print(f"Part two: Top three elves are carrying together {elves_with_max_calories} calories.")
    
    
get_elve_calories()