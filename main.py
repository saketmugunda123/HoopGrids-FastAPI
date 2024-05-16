import json
from fastapi import FastAPI

app = FastAPI()

with open('superList.json') as fp:
    superList = json.load(fp)


def findAllTeam (teamName: str ):
    ret = []
    for year in superList:
        yearInfo = superList[year]
        for player in yearInfo:
            attrs = yearInfo[player]
            if attrs[4] == teamName:
                ret.append(player)
    return ret

def common_member(a: list[str], b: list[str]):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        answerSet = a_set & b_set
        return answerSet
    else:
        return None

@app.get("/match-teams/")
def matchTeams (team1: str, team2: str):
    team1Players = findAllTeam(team1)
    team2Players = findAllTeam(team2)
    answerList = common_member(team1Players, team2Players)
    if len(answerList) > 0:
        return list(answerList)
    else:
        return {"Answer: not found"}



