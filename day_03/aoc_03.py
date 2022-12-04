
def get_priority(character):
    if character.islower():
        return ord(character) - 96 #ASCII for 'a' is 97, but for us it's 1
    else:
        return ord(character) - 38 #ASCII for 'A' is 65, but for us it's 27

#PART 1
def rucksack_reorganization1():
    with open("day_03\input_03.txt") as rucksack:
        priority_sum = 0
        for rucksack_contents in rucksack:
            rucksack_contents = rucksack_contents.rstrip()
            rucksack_middle_index = int(len(rucksack_contents)/2)
            compartment_1 = rucksack_contents[:rucksack_middle_index]
            compartment_2 = rucksack_contents[rucksack_middle_index:]
            
            for letter in compartment_1:
                if letter in compartment_2:
                    priority_sum += get_priority(letter)
                    break #initially had problems, because I didn't include break!
                    
    print(f"Sum of priorites is {priority_sum}.")
    
#PART 2
def rucksack_reorganization2():
    with open("day_03\input_03.txt") as rucksack:
        badge_sum = 0
        for rucksack_contents in rucksack:
            rucksack_contents = rucksack_contents.rstrip()
            print(len(rucksack_contents))
            for i in range(0, len(rucksack_contents), 3):
                print(i)
                for character in rucksack_contents[i]:
                    if character in rucksack_contents[i+1] and character in rucksack_contents[i+2]:
                        badge_sum += get_priority(character)
                        break
        
        
    print(f"Sum of badge priorities is {badge_sum}.")
    
            
rucksack_reorganization1()
rucksack_reorganization2()
