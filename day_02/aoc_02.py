def rock_paper_scissors1():
    with open("input_02.txt", "r") as rock_paper_scissors_tournament:
        total_score = 0
        #Part 1
        for rounds in rock_paper_scissors_tournament:
            rounds = rounds.rstrip()
            if rounds[0] == 'A':
                if rounds[2] == 'X':
                    total_score += 4
                elif rounds[2] == 'Y':
                    total_score += 8
                elif rounds[2] == 'Z':
                    total_score += 3

            elif rounds[0] == 'B':
                if rounds[2] == 'X':
                    total_score += 1
                elif rounds[2] == 'Y':
                    total_score += 5
                elif rounds[2] == 'Z':
                    total_score += 9
                        
            else:
                if rounds[2] == 'X':
                    total_score += 7
                elif rounds[2] == 'Y':
                    total_score += 2
                elif rounds [2] == 'Z':
                    total_score += 6

        print(f"Total score for part 1 is {total_score}.")
    
    
def rock_paper_scissors2():
     with open("input_02.txt", "r") as rock_paper_scissors_tournament:
        total_score = 0
        #Part 2
        for rounds in rock_paper_scissors_tournament:
            rounds = rounds.rstrip()
            if rounds[2] == 'X':
                #we need to lose
                if rounds[0] == 'A':
                    total_score += 3 #we use scissors
                elif rounds[0] == 'B': 
                    total_score += 1 #we use rock
                elif rounds[0] == 'C':
                    total_score += 2 #we use paper

            elif rounds[2] == 'Y':
                #we need to draw
                if rounds[0] == 'A': 
                    total_score += 4 #we use rock
                elif rounds[0] == 'B':
                    total_score += 5 #we use paper
                elif rounds[0] == 'C': 
                    total_score += 6  #we use scissors
                        
            else:
                #we need to WIN!
                if rounds[0] == 'A':
                    total_score += 8 #we use paper
                elif rounds[0] == 'B':
                    total_score += 9 #we use scissors
                elif rounds[0] == 'C':
                    total_score += 7 #we use rock
                
        print(f"Total score for part 2 is {total_score}.")
    
rock_paper_scissors1()
rock_paper_scissors2()


                    
