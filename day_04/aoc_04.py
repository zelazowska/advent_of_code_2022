def camp_cleanup1():
    with open("day_04\input_04.txt", "r") as file:
        overlapping_ranges = 0
        fully_overlapping_ranges = 0
        for lines in file:
            first_elf_range, second_elf_range = lines.rstrip().split(",")  #get rid of blank lines, divide into two lists
            a, b = [int(number) for number in first_elf_range.split("-")]  #split each list into two integers
            c, d = [int(number) for number in second_elf_range.split("-")]
            if (a<=c and b>=d) or (a>=c and b<=d): #two ways in which one range will contain another
                fully_overlapping_ranges += 1
            if max(a,c) <= min(b,d): #If biggest starting point is smaller than smallest ending point, ranges will overlap
                overlapping_ranges += 1
        
        print(f"PART 1: Amount of fully overlapping pairs: {fully_overlapping_ranges}.")
        print(f"PART 2: Amount of overlapping ranges: {overlapping_ranges}.")
        
camp_cleanup1()
