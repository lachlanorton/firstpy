# Exercises
# Written by Lachlan Orton
# Date: 14/02/2023
# TAFE St Leonard's Campus

# Input names for Team 1 and Team 2
team1 = input("Team 1's name: ")
team2 = input("Team 2's name: ")

print('')
print(team1 + " vs " + team2)
print('')

# Input score amounts for each team
team1Score = int(input("How many goals did " + team1 + " score?: "))
team2Score = int(input("How many goals did " + team2 + " score?: "))

# Print a "final match scores" screen
print('')
print("FINAL MATCH SCORES:")
print(team1 + "-" + str(team1Score))
print(team2 + "-" + str(team2Score))
print('')

# Compare scores and check for tie, print result
if team1Score > team2Score:
    print(team1 + " won with a score of " + str(team1Score))
elif team1Score == team2Score:
    print("It's a tie!")
else:
    print(team2 + " won with a score of " + str(team2Score))




