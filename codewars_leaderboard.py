import requests
import json
from tabulate import tabulate


print("  ############# Live Services Code Wars Leaderboard #############  ")

storedprofile = []
#please replace ${insertUsername} with the username needed
usernames = ["Katesagay","${insertUsername}","${insertUsername}","${insertUsername}","${insertUsername}"]
for username in usernames :
    response = requests.get(f"https://www.codewars.com/api/v1/users/{username}")
    data = response.json()
    totalCompleted = data.get('codeChallenges').get('totalCompleted')
    if data.get('ranks').get('languages').get('python') != None :
        score = data.get('ranks').get('languages').get('python').get('score')
        name = data.get('ranks').get('languages').get('python').get('name')
    else:
        score = 0
        name = 'Player has not started a python kata'
    profile = [username, name, score, totalCompleted]
    storedprofile.append(profile)
# sort list from descending score
storedprofile.sort(key=lambda  x: x[1])
print(tabulate(storedprofile
,["Username", "Rank", "Score", "Total Challenges Completed "], tablefmt="grid"))

      

