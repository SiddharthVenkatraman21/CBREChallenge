import pandas as pd

teams_raw = pd.read_csv('teams.csv')
floors_raw = pd.read_csv('floors.csv')

# make dictionary of teams
teams = {}
for i in range(len(teams_raw)):
    teams[teams_raw['team'][i]] = [teams_raw["strength"][i], [int(pref) for pref in teams_raw["preferred"][i].split(",")], [int(tol) for tol in teams_raw["tolerated"][i].split(",")], [int(no) for no in teams_raw["no_way"][i].split(",")]]
# format is {team: [strength, [preferred], [tolerated], [no_way]]}
# sort teams in descending order of strength
teams = {k: v for k, v in sorted(teams.items(), key=lambda item: item[1][0], reverse=True)}

# make dictionary of floors
floors = {}
for i in range(len(floors_raw)):
    floors[floors_raw['floor'][i]] = int(floors_raw['max_capacity'][i])
# sort floors in descending order of capacity
floors = {k: v for k, v in sorted(floors.items(), key=lambda item: item[1], reverse=True)}

# make set of the teams that mutually prefer each other
mutual_prefs = []
for team in teams:
    for pref in teams[team][1]:
        if team in teams[pref][1]:
            tempset = set()
            tempset.add(team)
            tempset.add(pref)
            if tempset not in mutual_prefs:
                mutual_prefs.append(tempset)

# make list of the teams that mutually prefer each other
mutual_prefs_list = []
for x in mutual_prefs:
    mutual_prefs_list.append(sorted(x))

# print(mutual_prefs_list)

# make dictionary of the pairs and their added strengths
mutual_prefs_strengths = {}
for pair in mutual_prefs_list:
    mutual_prefs_strengths[str(pair)] = teams[pair[0]][0] + teams[pair[1]][0]
#sort the dictionary in descending order of added strengths
mutual_prefs_strengths = {k: v for k, v in sorted(mutual_prefs_strengths.items(), key=lambda item: item[1], reverse=True)}
# print(mutual_prefs_strengths)

# print(mutual_prefs_strengths)

# make pandas dataframe of the floors, with the teams on each floor, their occupancy, their total capacity, and the percentage of capacity used
floors_df = pd.DataFrame(columns = ['floor', 'capacity', 'teams', 'occupancy', 'percent_occupancy'])
floors_df['floor'] = floors.keys()
floors_df['capacity'] = floors.values()

# print(floors_df.head())

# print capacity when floor is A as an int
# print(floors_df['capacity'][floors_df['floor'] == 'A'].values[0])

# print(mutual_prefs_strengths['[1, 2]'])


# print(floors_df['teams'][floors_df['floor'] == 'A'])

occupancy = []
p_occupancy = []
floor_teams = []
# sort teams into floors

remaining_teams = list(teams.keys())
remaining_floors = list(floors.keys())

# array from sorted dictionary of mutual_prefs_strengths
pair_bystrengths = list(mutual_prefs_strengths.keys())
for pair in pair_bystrengths:
    # print("pair: " + str(pair))

    for floor in floors_df['floor']:
        # if the capacity of the floor is greater than or equal to the strength of the pair, and the strength of the pair is greater than or equal to 90% of the capacity of the floor
        # then set the respective floor teams to the pair
        # print("strength: ", mutual_prefs_strengths[str(pair)])
        if ((floors[floor] >= mutual_prefs_strengths[pair]) and (mutual_prefs_strengths[pair] >= (floors[floor]*0.9))):
            # set the respective floor teams to the pair
            floor_teams.append(pair)

            for team in [int(p3) for p3 in pair[1:-1].split(",")]:
                if team in remaining_teams:
                    remaining_teams.remove(team)
            if floor in remaining_floors:
                remaining_floors.remove(floor)

            # set the respective floor occupancy to the strength of the pair
            occupancy.append(mutual_prefs_strengths[pair])
            # print(floors_df['capacity'][floors_df['floor'] == floor].values[0] - mutual_prefs_strengths[str(pair)])
            p_occupancy.append((mutual_prefs_strengths[str(pair)] / floors[floor])*100)
            # delete all other pairs that contain the same as either of the teams in the pair by comparing after converting to ints
            pair_set = [int(p1) for p1 in pair[1:-1].split(",")]
            # print("pbs",pair_bystrengths)
            for key in pair_bystrengths:
                # print("key:",key)
                key_set = [int(k1) for k1 in key[1:-1].split(",")]
                if (pair_set[0] in key_set) and (pair_set[1] in key_set):
                    continue
                if (pair_set[0] in key_set) or (pair_set[1] in key_set):
                    str_key_set = str(key_set)
                    pair_bystrengths.remove(str_key_set)
            break
# print(occupancy)
# print(p_occupancy)
# print(floor_teams)

# print(remaining_teams)
# print(remaining_floors)

for team in remaining_teams:
    for floor in remaining_floors:
        if (floors[floor] >= teams[team][0]) and (teams[team][0] >= (floors[floor]*0.9)):
            floor_teams.append([team])
            occupancy.append(teams[team][0])
            p_occupancy.append((teams[team][0] / floors[floor])*100)
            break


floors_df['occupancy'] = occupancy
floors_df['percent_occupancy'] = p_occupancy
floors_df['teams'] = floor_teams


print(floors_df.head())

floors_df.to_csv('Sorted_Floorplan.csv', index=False)