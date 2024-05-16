from bs4 import BeautifulSoup
import requests
import json

superList = {}

for i in range (1947, 2023):
    url = f"https://basketball.realgm.com/nba/players/{i}"
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    stats = soup.find('tbody').find_all('tr')
   
    playerList = {}

    for stat in stats:
        
        nameFound = False
        name = ""

        for attribute in stat.getText().split('\n'):
            if not nameFound and attribute:
                name = attribute
                playerList[name] = []
                nameFound = True
            elif name:
                playerList[name].append(attribute)

    superList[i] = playerList

with open('superList.json', 'w') as fp:
    json.dump(superList, fp)

def findAllTeam (teamName):
    ret = []
    for year in superList:
        yearInfo = superList[year]
        for player in yearInfo:
            attrs = yearInfo[player]
            if attrs[4] == teamName:
                ret.append(player)
    return ret

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No player was ever on both of these teams")

def matchTeams (team1, team2):
    team1Players = findAllTeam(team1)
    team2Players = findAllTeam(team2)
    print(common_member(team1Players, team2Players))
    
matchTeams ("CLE", "SAS")