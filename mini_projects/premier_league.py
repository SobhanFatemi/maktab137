import random

raw_teams = [
    "Arsenal",
    "Aston Villa",
    "Bournemouth",
    "Brentford",
    "Brighton & Hove Albion",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Liverpool",
    "Luton Town",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Nottingham Forest",
    "Sheffield United",
    "Tottenham Hotspur",
    "West Ham United",
    "Wolverhampton Wanderers",
    "Burnley"
]

times = [
 '2025-10-14-09:00',
 '2025-10-14-10:00',
 '2025-10-14-11:00',
 '2025-10-14-12:00',
 '2025-10-14-13:00',
 '2025-10-14-14:00',
 '2025-10-14-15:00',
 '2025-10-14-16:00',
 '2025-10-14-17:00',
 '2025-10-14-18:00'
]

teams = []
played = []
raw_scores = [0, 1, 2, 3, 4, 5, 6, 7]
weights = [0.17, 0.22, 0.22, 0.17, 0.10, 0.08, 0.02, 0.01]

for team in raw_teams:
    teams.append({"name": team, "points": 0, "s_goals": 0, "r_goals": 0, "goal_diff": 0, "matches_played": 0})

def sort(teams, based="points", reverse=True):
    teams = sorted(teams, key=lambda team: (team[based], team["goal_diff"], team["s_goals"]), reverse=reverse)
    return teams

def show_table(teams):
    print("-------\nTable\n-------")
    for i, team in enumerate(teams):
        print(f"\n{i+1}- {team['name']}\nMatches played: {team['matches_played']}\nScored Goals: {team["s_goals"]}\nRecieved Goals: {team["r_goals"]}\nGoal Difference: {team["goal_diff"]}\nPoints:{team["points"]}\n")


def match_making(teams):
    round_matches = []
    used = set()

    for i in range(len(teams)):
        if teams[i]['name'] in used:
            continue
        for j in range(i + 1, len(teams)):
            if teams[j]['name'] in used:
                continue
            pair = tuple(sorted([teams[i]['name'], teams[j]['name']]))
            if pair not in played:
                round_matches.append(pair)
                used.add(teams[i]['name'])
                used.add(teams[j]['name'])
                break
    return round_matches


def play(teams):
    round_matches = []
    used = set()
    
    for i in range(len(teams)):
        if teams[i]['name'] in used:
            continue
        if teams[i]['matches_played'] == 19:
            continue
        for j in range(i + 1, len(teams)):
            if teams[j]['name'] in used:
                continue
            if teams[j]['matches_played'] == 19:
                continue
            pair = tuple(sorted([teams[i]['name'], teams[j]['name']]))
            if pair not in played:
                played.append(pair)
                round_matches.append(pair)
                used.add(teams[i]['name'])
                used.add(teams[j]['name'])

                first_team_score = random.choices(raw_scores, weights=weights, k=1)[0]
                second_team_score = random.choices(raw_scores, weights=weights, k=1)[0]

                print(f"{teams[i]['name']} - {first_team_score} | {teams[j]['name']} - {second_team_score}\n")

                teams[i]['s_goals'] += first_team_score
                teams[i]['r_goals'] += second_team_score
                teams[i]['goal_diff'] += (first_team_score - second_team_score)
                teams[i]['matches_played'] += 1

                teams[j]['s_goals'] += second_team_score
                teams[j]['r_goals'] += first_team_score
                teams[j]['goal_diff'] += (second_team_score - first_team_score)
                teams[j]['matches_played'] += 1

                if first_team_score > second_team_score:
                    teams[i]['points'] += 3
                elif second_team_score > first_team_score:
                    teams[j]['points'] += 3
                else:
                    teams[i]['points'] += 1
                    teams[j]['points'] += 1
                break

    new_times = []
    for time in times:
        splited_time = time.split('-')
        year = int(splited_time[0])
        month = int(splited_time[1])
        day = int(splited_time[2])

        if day <= 23:
                day += 7
        else:
            if month != 12:
                month += 1
                day -= 23
            else:
                year += 1
                month = 1
                day -= 23

        new_time = f"{year:04d}-{month:02d}-{day:02d}-{splited_time[3]}"
        new_times.append(new_time)
    return new_times
            


while True:
    first_action = input("Please enter your desired action:\n1- Show table\n2- Show upcoming matches\n3- Play\n4- Quit\nYour choice: ")

    if first_action == '1':
        while True:
            second_action = input("Sort table based on:\n1- Points\n2- Team name\nYour choice: ")
            if second_action == '1':
                teams = sort(teams, based="points", reverse=True)
            elif second_action == '2':
                teams = sort(teams, based="name", reverse=False)
            else:
                print("Invalid input!")
                continue
            show_table(teams)
            break

    elif first_action == '2':
        if len(played) >= 190:
            print("---------------------------------------\nAll possible matches have been played.\n---------------------------------------")
        else:
            print("-----------------\nUpcoming matches\n-----------------")
            for i, (first_team, second_team) in enumerate(match_making(teams)):
                print(f"Match #{i+1}: '{first_team}' vs '{second_team}' at '{times[i]}'\n")
    
    elif first_action == '3':
        if len(played) >= 190:
            print("---------------------------------------\nAll possible matches have been played.\n---------------------------------------")
        else:
            times = play(teams)
            teams = sort(teams, based="points", reverse=True)
            show_table(teams)

    elif first_action == '4':
        break

    else:
        print("Invalid input!")
        continue