import random
import time

#----------------------------------------------------------------------------------------
                           # Toss
                        
def toss(head, tail):
    list_A = [head, tail]
    list_B = ['bat', 'bowl']
    random.shuffle(list_A)
    team = list_A[0]
    what_to_select = random.choice(list_B)
    if what_to_select == 'bat':
        team_A = team
        team_B = list_A[1]
    else:
        team_B = team
        team_A = list_A[1]
    return team, what_to_select, team_A, team_B

#------------------------------------------------------------------------------------------
                          # Read Team Names

f = open('team_names.txt', 'r')
names_of_teams = f.readlines()
f.close()
for i in range(8):
    names_of_teams[i] = names_of_teams[i][0:len(names_of_teams[i]) - 1]

#-------------------------------------------------------------------------------------------
                           # Read Plater Names

f = open('players_names.txt', 'r')
names_of_players = f.readlines()
f.close()
for i in range(88):
    names_of_players[i] = names_of_players[i][0:len(names_of_players[i]) - 1]

#-------------------------------------------------------------------------------------------
                          #create radom list to generate teams

list = [0, 1, 2, 3, 4, 5, 6, 7]
random.shuffle(list)

#-------------------------------------------------------------------------------------------
                         #Functions For The Match

def matchfunc(a, b): #(a is batting and b is bowling

    over = 1
    wicketstaken = 0
    batsmen_A = 0
    batsmen_B = 1
    bowler = 0
    all_bat_runs = [0, 0]
    all_balls_taken = [0, 0]
    wickets_by_baller = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    all_runnings = 0
    batsman_dismissal = ['', '', '', '', '', '', '', '', '', '', '']
    way_of_dismissal  = ['catch', 'run out', 'bowled out', 'lbw']
    #-----------------------------------------------
    # when batting is true, batsmen_A is playing   |
    # when batting is false, batsmen_B is playing  |
    #-----------------------------------------------
    batting  = True
    while (over < 20) and (wicketstaken < 10):
        # 6 balls in an over
        for balling in range(6):
            # random all_runs
            all_runs = random.randrange(0, 7)
            # balls score
            if batting == True:
                all_balls_taken[batsmen_A] = all_balls_taken[batsmen_A] + 1
            else:
                all_balls_taken[batsmen_B] = all_balls_taken[batsmen_B] + 1
            # 5 runs counts as a wicket
            if (all_runs == 5):
                wicketstaken = wicketstaken + 1
                if wicketstaken > 9:
                    break
                wickets_by_baller[bowler] += 1
                # new batsmen 
                if (batting == True):
                    batsman_dismissal[batsmen_A] = random.choice(way_of_dismissal)
                    batsmen_A = wicketstaken + 1
                else:
                    batsman_dismissal[batsmen_B] = random.choice(way_of_dismissal)
                    batsmen_B = wicketstaken + 1
                # append new batsman details
                all_bat_runs.append(0)
                all_balls_taken.append(0)
            else:
                # adding all_runnings
                all_runnings = all_runnings + all_runs
                if batting == True:
                    all_bat_runs[batsmen_A] = all_bat_runs[batsmen_A] + all_runs
                else:
                    all_bat_runs[batsmen_B] = all_bat_runs[batsmen_B] + all_runs
            # replace batsmen for all_runs
            if (all_runs == 1) or (all_runs == 3):
                if batting == True:
                    batting = False
                else:
                    batting = True
        # after the over
        over += 1
        bowler += 1
        if bowler > 10:
            bowler = 0
        # change the batsman after the over
        if batting == True:
            batting = False
        else:
            batting = True
    return all_bat_runs, all_balls_taken , wickets_by_baller , all_runs, wicketstaken, over, batsman_dismissal

#----------------------------------------------------------------------------------------------------------------
                                             # Main Program

print('|____________ Welcome to the T20 Cricket Game_______|')
time.sleep(2)

#Selection Menu Bar
game_exit = False
while game_exit == False:
    print(" ")
    print('-------------------  Main Menu  ------------------------')
    print(" ")
    print("1.Edit Teams")
    print("2.Start Game")
    print("3.View Groups")
    print("4.Check previous match summary")
    print("5.View tournement standings")
    print("6.Exit")
    print (" ")
    user_select = input('Enter your Selection number : ')
    print (" ")
    
    user_select = int(user_select)

    # Validate the user selection
    if (0 > user_select > 6):
        print('\n\n\nInvalid Choice.')
#------------------------------------------------------------------------------------------------------------------
                                               # Option 6 (exit)

                                            
    if user_select == 6:
        game_exit = True

        
#------------------------------------------------------------------------------------------------------------------
                                                #Option 5 (Summary)

    if user_select ==5:
        #Open store_summary File (Read)
        f = open('store_summary.txt', 'r')
        summary_of_match = f.readlines()
        f.close()
        for i in range(7):
            # Remove Space and assigned to a list
            summary_of_match[i] = summary_of_match[i][0:len(summary_of_match[i]) - 1]
            print(summary_of_match[i])
        # Return To main Menu
        input("\n\nPress Enter to go to main menu")
        print(" ")
        game_exit = False

        
#-----------------------------------------------------------------------------------------------------------------
                                                #Option 3 (View Groups)
    if user_select == 3:
        time.sleep(2)
        # Select Tournament groups from the random list, names_of_teams 
        print('----------  GROUP A  ----------\n\nFirst Match:', names_of_teams[list[0]], 'vs', names_of_teams[list[1]], '.\nSecond Match:',
              names_of_teams[list[2]], 'vs', names_of_teams[list[3]], '.\n\n----------  GROUP B  ----------\n\nFirst Match:', names_of_teams[list[4]], 'vs',
              names_of_teams[list[5]], '.\nSecond Match:', names_of_teams[list[6]], 'vs', names_of_teams[list[7]], '.')

        #Redirecting to Main Menu
        input("\nPress Enter to go back to main menu\n")
        game_exit = False

#------------------------------------------------------------------------------------------------------------------
                                          #Option 4 (Check previous match summary)


    if user_select == 4:
        #write the store_summary File
        f = open('store_summary.txt', 'r')
        summary_of_match = f.readlines()
        f.close()
        #Select All 183 Lines
        for i in range(183):
            #Remove spaces and assigned to a list
            summary_of_match[i] = summary_of_match[i][0:len(summary_of_match[i]) - 1]
            print(summary_of_match[i])
        #Redirect to Main Menu
        input("\n\nPress Enter to go to main menu")
        print(" ")
        game_exit = False

#-------------------------------------------------------------------------------------------------------------------
                                         #Option 1 (Edit Teams)

        
    if user_select == 1:
        #Start the edit
        finish_edit = False
        while finish_edit == False:
            #Display all 8 teams
            for i in range(8):
                print(i + 1, '.', names_of_teams[i])
            # Get the user input to edit
            while True:
                team_editing = int(input('\nPress 0 to go to main menu \n Choose the team number that you want to edit : '))
                print (" ")
            # Validate the user Input
                if (team_editing >= 0) and (team_editing <= 8):
                    break
                else:
                    print('Invalid Choice. Please select the relevent team number')

            team_edit = False
            if team_editing != 0:
                team_edit = True
            else:
                #Exit from the editing process
                finish_edit = True
                
            # Create loop for the user to edit many times
            while team_edit == True:
                # Display team name and players 
                print('Selected Team | ',names_of_teams[team_editing - 1], '\n---------------------')
                
                for i in range(11):
                    print(i + 1, '.', names_of_players[(team_editing - 1) * 11 + i])
                    
                #Get the user input to replace
                while True:
                    place_new = int(input('\nPress 0 to go back \n Enter player  number that you want to replace : '))

                #Validate the input
                    if (place_new > -1) and (place_new < 12):
                        break
                    else:
                        print('Invalid Choice. Please select the relevent player number.')
                        
                if place_new == 0:
                    finish_edit = True
                    team_edit = False
                    
                else:
                    
                    new_player = input('\nEnter the new player name :')    
                    finish_edit == True
                    # Include the user's player in the names_of_players list
                    names_of_players[((team_editing - 1) * 11) + place_new - 1] = new_player

                    time.sleep(2)
                    print ("\n✔️New Player Added Sucessfully\n")
                    

    #Write to the players_names document
    f = open('players_names.txt', 'w')
    f.truncate()
    for i in range(88):
        f.write(names_of_players[i] + '\n')
    f.close()

#---------------------------------------------------------------------------------------------------------------------------
                                        # Option 2 (Start Game) 


    if user_select == 2:
        # exit after the match
        game_exit = True
        time.sleep(2)
        
        # Define the round one matches
        difference = 0
        wickets_new = []
        all_runs_new = []
        wicketstaken = []
        winner_team = []
        all_runs = []
        all_balls = []
        batsman_dismissal_A = []
        batsman_dismissal_B = []
        batsman_dismissal = []
        loser_team= []
        all_summary = ''
        #Append match details for all 88 players
        for i in range(88):
            wicketstaken.append(0)
            all_runs.append(0)
            all_balls.append(0)
            batsman_dismissal.append('')
            batsman_dismissal[i] = ['', '', '']



        # Random selection to choose, what_to_select, first_team and second_team through the toss
        for i in range(4):
            while True:
                win, what_to_select, first_team, second_team = toss(list[i * 2], list[(i * 2) + 1])

                runs_bat_A, ball_taken_A, wickets_ball_B, all_runs_A, all_wickets_B, over_A, batsman_dismissal_A = matchfunc(first_team, second_team)
                runs_bat_B, ball_taken_B, wickets_ball_A, all_runs_B, all_wickets_A, over_B, batsman_dismissal_B = matchfunc(second_team, first_team)
                
                #If random is a draw
                if runs_bat_B != runs_bat_A:
                    break

            #Print the end Score Board 
            print(i + 1, ".", names_of_teams[list[i * 2]], "vs", names_of_teams[list[(i * 2) + 1]])

            print()

            print("◾ Toss win By : ",names_of_teams[win], "\n◾ Decided to  : ",what_to_select,"\n")
            
            print("\n----------",names_of_teams[first_team],"----------\n")
            
            print("Total runs           | ",all_runs_A, "\nTotal wickets        | ",all_wickets_B,"\nTotal number of overs | ",over_A)

            print("\n----------",names_of_teams[second_team],"----------\n")
            
            print("Total runs is        | ",all_runs_B, "\nTotal wickets        | ",all_wickets_A,"\nTotal number of overs is | ",over_B)
            
            all_summary = all_summary + str(i + 1) + '.' + str(names_of_teams[list[i * 2]]) + ' vs ' + str(
                names_of_teams[list[(i * 2) + 1]]) + '\n' + str(names_of_teams[win]) + ' win the toss and decided to ' + str(
                what_to_select) + '.\n' + 'Total runs of ' + str(names_of_teams[first_team]) + ' was ' + str(
                all_runs_A) + '.\nTotal wickets taken was ' + str(
                all_wickets_B) + '.\nTotal number of overs was ' + str(over_A) + '.\n\nTotal runs of ' + str(
                names_of_teams[second_team]) + ' was ' + str(all_runs_B) + '.\nTotal wickets taken was ' + str(
                all_wickets_A) + '.\nTotal number of overs was ' + str(over_B) + '.\n'
            if all_runs_A > all_runs_B:
                winner_team.append(first_team)
                difference = all_runs_A - all_runs_B
            else:
                winner_team.append(second_team)
                difference = all_runs_B - all_runs_A
            # all_runs adding
            for j in range(len(runs_bat_A)):
                all_runs[(first_team  * 11) + j] = all_runs[(first_team * 11) + j] + runs_bat_A[j]
            for j in range(len(runs_bat_B)):
                all_runs[(second_team * 11) + j] = all_runs[(second_team  * 11) + j] + runs_bat_B[j]
            for j in range(len(ball_taken_A)):
                all_balls [(first_team * 11) + j] = all_balls[(first_team * 11) + j] + ball_taken_A[j]
            for j in range(len(ball_taken_B)):
                all_balls[(second_team * 11) + j] = all_balls [(second_team * 11) + j] + ball_taken_B[j]
            for j in range(len(wickets_ball_A)):
                wicketstaken[(first_team * 11) + j] = wicketstaken[(first_team * 11) + j] + wickets_ball_A[j]
            for j in range(len(wickets_ball_B)):
                wicketstaken[(second_team * 11) + j] = wicketstaken[(second_team * 11) + j] + wickets_ball_B[j]
            # method of out
            for j in range(11):
                batsman_dismissal[(first_team * 11) + j][0] = batsman_dismissal_A[j]
            for j in range(11):
                batsman_dismissal[(second_team * 11) + j][0] = batsman_dismissal_B[j]

            print("\n✔️The winner is :",names_of_teams[winner_team[i]])
            
            all_summary = all_summary  + str(names_of_teams[winner_team[i]]) + '\n\n'
            
            print(" ")
            time.sleep(2)
            print("----------------------------------------------------------------------------------------------------------\n\n")

#-------------------------------------------------------------------------------------------------------------------------------------------------
                                             #Second Round Final

        # second rounds of matches
        print("\n---------- SEMIFINALS ----------\n")
        print("\n⏹️ First match   : ", names_of_teams[winner_team[0]], "vs", names_of_teams[winner_team[1]],
              "\n⏹️ Second match  : ", names_of_teams[winner_team[2]], "vs", names_of_teams[winner_team[3]])
        
        all_summary=all_summary + 'SEMIFINALS\n----------------------------------------------------\n'
        
        print(" ")
        time.sleep(2)
        print(" ")
        
        for i in range(2):
            while True:
                win, what_to_select , first_team, second_team = toss(winner_team[i * 2], winner_team[(i * 2) + 1])
                runs_bat_A, ball_taken_A, wickets_ball_B, all_runs_A, all_wickets_B, over_A, batsman_dismissal_A = matchfunc(first_team, second_team)
                runs_bat_B, ball_taken_B, wickets_ball_A, all_runs_B, all_wickets_A, over_B, batsman_dismissal_B = matchfunc(second_team, first_team)
                # incase of draw, rematch
                if runs_bat_B != runs_bat_A:
                    break
            print()
            print(i + 1, ".", names_of_teams[winner_team[i * 2]], "vs", names_of_teams[winner_team[(i * 2) + 1]],"\n")

            print("◾ Toss won By : ",names_of_teams[win], "\n◾ Decided to  : ",what_to_select ,"\n")
            
            print("\n----------",names_of_teams[first_team],"----------\n")
            
            print("Total all_runs of is | ",all_runs_A, "\nTotal wickets taken is | ",all_wickets_B,"\nTotal number of overs is | ",over_A)

            print("\n----------",names_of_teams[second_team],"----------\n")
            
            print("Total all_runs of is | ",all_runs_B, "\nTotal wickets taken is   | ",all_wickets_A,"\nTotal number of overs is | ",over_B)
            
            all_summary = all_summary + str(
                i + 1) + '.' + str(names_of_teams[winner_team[i * 2]]) + ' vs ' + str(
                names_of_teams[winner_team[(i * 2) + 1]]) + '\n' + str(names_of_teams[win]) + ' win the toss and decided to ' + str(
                what_to_select ) + '.\n' + 'Total runs of ' + str(names_of_teams[first_team]) + ' was ' + str(
                all_runs_A) + '.\nTotal wickets taken was ' + str(
                all_wickets_B) + '.\nTotal number of overs was ' + str(over_A) + '.\n\nTotal runs of ' + str(
                names_of_teams[second_team]) + ' was ' + str(all_runs_B) + '.\nTotal wickets taken was ' + str(
                all_wickets_A) + '.\nTotal number of overs was ' + str(over_B) + '.\n'
            
            # winner
            if all_runs_A > all_runs_B:
                winner_team.append(first_team)
                difference = all_runs_A - all_runs_B
                loser_team.append(second_team)
            else:
                winner_team.append(second_team)
                difference = all_runs_B - all_runs_A
                loser_team.append(first_team)
            # all_runs adding
            for j in range(len(runs_bat_A)):
                all_runs[(first_team * 11) + j] = all_runs[(first_team * 11) + j] + runs_bat_A[j]
            for j in range(len(runs_bat_B)):
                all_runs[(second_team * 11) + j] = all_runs[(second_team * 11) + j] + runs_bat_B[j]
            for j in range(len(ball_taken_A)):
                all_balls[(first_team * 11) + j] = all_balls[(first_team * 11) + j] + ball_taken_A[j]
            for j in range(len(ball_taken_B)):
                all_balls[(second_team * 11) + j] = all_balls[(second_team * 11) + j] + ball_taken_B[j]
            for j in range(len(wickets_ball_A)):
                wicketstaken[(first_team * 11) + j] = wicketstaken[(first_team * 11) + j] + wickets_ball_A[j]
            for j in range(len(wickets_ball_B)):
                wicketstaken[(second_team * 11) + j] = wicketstaken[(second_team * 11) + j] + wickets_ball_B[j]
            # method of out
            for j in range(11):
                batsman_dismissal[(first_team * 11) + j][1] = batsman_dismissal_A[j]
            for j in range(11):
                batsman_dismissal[(second_team * 11) + j][1] = batsman_dismissal_B[j]

            print("\n✔️The winner is :",names_of_teams[winner_team[i + 4]])
            
            all_summary = all_summary + str(names_of_teams[winner_team[i + 4]]) + '\n\n'
            
            print(" ")
            time.sleep(2)
            print("----------------------------------------------------------------------------------------------------------\n\n")
            
        # second runners up
        print("\n---------- SECOND RUNNERS UP ----------\n")
        print("\n⏹️ ", names_of_teams[loser_team[0]], "vs", names_of_teams[loser_team[1]])
        print()
        while True:
            win, what_to_select , first_team, second_team = toss(loser_team[0], loser_team[1])
            runs_bat_A, ball_taken_A, wickets_ball_B, all_runs_A, all_wickets_B, over_A, batsman_dismissal_A = matchfunc(first_team, second_team)
            runs_bat_B, ball_taken_B, wickets_ball_A, all_runs_B, all_wickets_A, over_B, batsman_dismissal_B = matchfunc(second_team, first_team)
            # Draw Situation 
            if runs_bat_B != runs_bat_A:
                break
        print()

        print("◾ Toss win By : ",names_of_teams[win], "\n◾ Decided to  : ",what_to_select ,"\n")
            
        print("\n----------",names_of_teams[first_team],"----------\n")
            
        print("Total all_runs of is         | ",all_runs_A, "\nTotal wickets taken is   | ",all_wickets_B,"\nTotal number of overs is | ",over_A)

        print("\n----------",names_of_teams[second_team],"----------\n")
            
        print("Total all_runs of is         | ",all_runs_B, "\nTotal wickets taken is   | ",all_wickets_A,"\nTotal number of overs is | ",over_B)
        
    
        all_summary = all_summary + 'SECOND RUNNERS UP\n----------------------------------------------------\n' + str(names_of_teams[loser_team[0]]) + ' vs ' + str(
                names_of_teams[loser_team[1]]) + '\n' + str(names_of_teams[win]) + ' win the toss and decided to ' + str(
                what_to_select ) + '.\n' + 'Total all_runs of ' + str(names_of_teams[first_team]) + ' was ' + str(
                all_runs_A) + '.\nTotal wickets taken was ' + str(
                all_wickets_B) + '.\nTotal number of overs was ' + str(over_A) + '.\n\nTotal all_runs of ' + str(
                names_of_teams[second_team]) + ' was ' + str(all_runs_B) + '.\nTotal wickets taken was ' + str(
                all_wickets_A) + '.\nTotal number of overs was ' + str(over_B) + '.\n'
        if all_runs_A > all_runs_B:
            loser_team.append(first_team)
            difference = all_runs_A - all_runs_B
        else:
            loser_team.append(second_team)
            difference = all_runs_A
            
        # all_runs adding
        for j in range(len(runs_bat_A)):
            all_runs[(first_team * 11) + j] = all_runs[(first_team * 11) + j] + runs_bat_A[j]
        for j in range(len(runs_bat_B)):
            all_runs[(second_team * 11) + j] = all_runs[(second_team * 11) + j] + runs_bat_B[j]
        for j in range(len(ball_taken_A)):
            all_balls[(first_team * 11) + j] = all_balls[(first_team * 11) + j] + ball_taken_A[j]
        for j in range(len(ball_taken_B)):
            all_balls[(second_team * 11) + j] = all_balls[(second_team * 11) + j] + ball_taken_B[j]
        for j in range(len(wickets_ball_A)):
            wicketstaken[(first_team * 11) + j] = wicketstaken[(first_team * 11) + j] + wickets_ball_A[j]
        for j in range(len(wickets_ball_B)):
            wicketstaken[(second_team * 11) + j] = wicketstaken[(second_team * 11) + j] + wickets_ball_B[j]
            
        # Batsman Out
        for j in range(11):
            batsman_dismissal[(first_team * 11) + j][2] = batsman_dismissal_A[j]
        for j in range(11):
            batsman_dismissal[(second_team * 11) + j][2] = batsman_dismissal_B[j]

        print("\n✔️The winner is :",names_of_teams[loser_team[2]])
        
        all_summary = all_summary + str(names_of_teams[loser_team[2]])  + '\n\n'

        print(" ")
        time.sleep(2)
        print("----------------------------------------------------------------------------------------------------------\n\n")
    

#-----------------------------------------------------------------------------------------------------------------------------------------------------
                                                   # Final Match


        print("\n---------- FINALS ----------\n")
        print("\n⏹️ ",names_of_teams[winner_team[4]], "vs", names_of_teams[winner_team[5]])
        print()
        while True:
            win, what_to_select , first_team, second_team = toss(winner_team[4], winner_team[5])
            runs_bat_A, ball_taken_A, wickets_ball_B, all_runs_A, all_wickets_B, over_A, batsman_dismissal_A = matchfunc(first_team, second_team)
            runs_bat_B, ball_taken_B, wickets_ball_A, all_runs_B, all_wickets_A, over_B, batsman_dismissal_B = matchfunc(second_team, first_team)
            # incase of draw, rematch
            if runs_bat_B != runs_bat_A:
                break

        print()

        print("◾ Toss win By : ",names_of_teams[win], "\n◾ Decided to  : ",what_to_select ,"\n")
            
        print("\n----------",names_of_teams[first_team],"----------\n")
            
        print("Total all_runs of is     | ",all_runs_A, "\nTotal wickets taken is   | ",all_wickets_B,"\nTotal number of overs is | ",over_A)

        print("\n----------",names_of_teams[second_team],"----------\n")
            
        print("Total all_runs of is     | ",all_runs_B, "\nTotal wickets taken is   | ",all_wickets_A,"\nTotal number of overs is | ",over_B)
        

        all_summary = all_summary + 'FINALS\n----------------------------------------------------\n' + str(
            names_of_teams[winner_team[4]]) + ' vs ' + str(
            names_of_teams[winner_team[5]]) + '\n' + str(names_of_teams[win]) + ' win the toss and decided to ' + str(
            what_to_select ) + '.\n' + 'Total all_runs of ' + str(names_of_teams[first_team]) + ' was ' + str(
            all_runs_A) + '.\nTotal wickets taken was ' + str(
            all_wickets_B) + '.\nTotal number of overs was ' + str(over_A) + '.\n\nTotal all_runs of ' + str(
            names_of_teams[second_team]) + ' was ' + str(all_runs_B) + '.\nTotal wickets taken was ' + str(
            all_wickets_A) + '.\nTotal number of overs was ' + str(over_B) + '.\n'
        if all_runs_A > all_runs_B:
            winner_team.append(first_team)
            loser_team.append(second_team)
            difference = all_runs_A - all_runs_B
        else:
            winner_team.append(second_team)
            loser_team.append(first_team)
            difference = all_runs_B - all_runs_A
            
        # all_runs adding
        for j in range(len(runs_bat_A)):
            all_runs[(first_team * 11) + j] = all_runs[(first_team * 11) + j] + runs_bat_A[j]
        for j in range(len(runs_bat_B)):
            all_runs[(second_team * 11) + j] = all_runs[(second_team * 11) + j] + runs_bat_B[j]
        for j in range(len(ball_taken_A)):
            all_balls[(first_team * 11) + j] = all_balls[(first_team * 11) + j] + ball_taken_A[j]
        for j in range(len(ball_taken_B)):
            all_balls[(second_team * 11) + j] = all_balls[(second_team * 11) + j] + ball_taken_B[j]
        for j in range(len(wickets_ball_A)):
            wicketstaken[(first_team * 11) + j] = wicketstaken[(first_team * 11) + j] + wickets_ball_A[j]
        for j in range(len(wickets_ball_B)):
            wicketstaken[(second_team * 11) + j] = wicketstaken[(second_team * 11) + j] + wickets_ball_B[j]
            
        # Batsman Outs
        for j in range(11):
            batsman_dismissal[(first_team * 11) + j][2] = batsman_dismissal_A[j]
        for j in range(11):
            batsman_dismissal[(second_team * 11) + j][2] = batsman_dismissal_B[j]

        print("\n✔️The winner is :",names_of_teams[winner_team[6]])
         
        all_summary = all_summary + str(names_of_teams[winner_team[6]]) + ' win by ' + str(difference) + 'runs.\n\n'

        print(" ")
        time.sleep(2)
        print("----------------------------------------------------------------------------------------------------------\n\n")

#------------------------------------------- write on the summery text ---------------------------------------------------
        
        players = []
        newplayers = []
        
        for i in range(88):
            players.append(names_of_players[i])
            newplayers.append(names_of_players[i])
            all_runs_new.append(all_runs[i])
            wickets_new.append(wicketstaken[i])
            players[i] = players[i] + "\t"
            newplayers[i] = newplayers[i] + "\t"
            
        for i in range(87, 82, -1):
            for j in range(i):
                if all_runs_new[j] > all_runs_new[j + 1]:
                    newnum = all_runs_new[j]
                    temp = players[j]
                    all_runs_new[j] = all_runs_new[j + 1]
                    players[j] = players[j + 1]
                    all_runs_new[j + 1] = newnum
                    players[j + 1] = temp
                    
        for i in range(87, 82, -1):
            for j in range(i):
                if wickets_new[j] > wickets_new[j + 1]:
                    newwickets = wickets_new[j]
                    newtemp = newplayers[j]
                    wickets_new[j] = wickets_new[j + 1]
                    newplayers[j] = newplayers[j + 1]
                    wickets_new[j + 1] = newwickets
                    newplayers[j + 1] = newtemp
        for i in range(88):
            len(names_of_players[i])

# Write on the store_summary file

        f = open('store_summary.txt', 'w')
        
        f.truncate()
        
        f.write("First Place  :" + str(names_of_teams[winner_team[6]]) + "\nSecond Place :" + str(names_of_teams[loser_team[3]]) + "\nThird Place  :" + str(names_of_teams[loser_team[2]]))
        
        f.write('\n\nBest batsmen : ' + str(players[-1]) + '(' + str(all_runs_new[-1]) + ')')

        f.write('\n\nBest bowlers : ' + str(newplayers[-1]) + '(' + str(wickets_new[-1]) + ')\n')
        
        for i in range(88):
            f.write(
                f"\n{str(names_of_players[i]):<15}" + ' | ' + 'Scored : ' + f"{str(all_runs[i]):<3}" + ' runs for ' + f"{str(all_balls[i]):<3}" + 'balls, |  Scored Wickets : ' + str(
                    wicketstaken[i])  + '\n')
        f.close()

        input("\n\nPress enter to go to main menu")
        print(" ")
        game_exit = False
