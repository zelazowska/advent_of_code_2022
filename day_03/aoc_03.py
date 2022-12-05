#function for getting ASCII priority
def get_priority(character):
    if character.islower():
        return ord(character) - 96 #ASCII for 'a' is 97, but for us it's 1
    else:
        return ord(character) - 38 #ASCII for 'A' is 65, but for us it's 27


with open("day_03\input_03.txt") as rucksack:
        global rucksack_contents
        rucksack_contents = rucksack.readlines()
        
#PART 1
def get_priority_sum():
    priority_sum = 0
    for rucksack_content_compartment in rucksack_contents:
        rucksack_middle_index = int(len(rucksack_content_compartment)/2)
        compartment_1 = rucksack_content_compartment[:rucksack_middle_index]
        compartment_2 = rucksack_content_compartment[rucksack_middle_index:]
                
        for letter in compartment_1:
            if letter in compartment_2:
                priority_sum += get_priority(letter)
                break #initially had problems, because I didn't include break!
                        
    print(f"Sum of priorites is {priority_sum}.")
    
#PART 2
def get_badge_priority_sum():
    badge_sum = 0
    for i in range(0, len(rucksack_contents), 3):
        for character in rucksack_contents[i]:
            if character in rucksack_contents[i+1] and character in rucksack_contents[i+2]:
                badge_sum += get_priority(character)
                break
        
        
    print(f"Sum of badge priorities is {badge_sum}.")
    
            
get_priority_sum()
get_badge_priority_sum()
