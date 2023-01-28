# don't touch this pls

# teams = ((<team number>, <number of members>, <list of preferred teams>, <list of tolerated teams>, <list of blacklisted teams>), ...)
# floors = ((<floor number>, <capacity>), ...)

def sort_teams(teams, floors):
    # Create a list for each floor to hold the assigned teams
    floor_assignments = {floor[0]: [] for floor in floors}
    # Sort teams by number of members in descending order
    teams = sorted(teams, key=lambda x: x[1], reverse=True)

    for team in teams:
        team_number, team_size, preferred, tolerated, blacklisted = team
        assigned = False
        # Iterate through floors in descending order of capacity
        for floor in sorted(floors, key=lambda x: x[1], reverse=True):
            floor_name, floor_capacity = floor
            # Check if floor has enough capacity for current team
            if floor_capacity >= team_size:
                # Check if any blacklisted teams are already assigned to floor
                if not any(b in floor_assignments[floor_name] for b in blacklisted):
                    floor_assignments[floor_name].append(team_number)
                    assigned = True
                    # Try to add preferred teams to the same floor
                    for p in preferred:
                        if p in teams:
                            p_team = [t for t in teams if t[0] == p][0]
                            p_team_number, p_team_size, _, _, _ = p_team
                            if floor_capacity >= team_size + p_team_size:
                                floor_assignments[floor_name].append(p_team_number)
                                teams.remove(p_team)
                    break
        # If team was not assigned to any floor, try to add them to tolerated teams floor
        if not assigned:
            for floor in floors:
                floor_name, floor_capacity = floor
                if any(t in floor_assignments[floor_name] for t in tolerated):
                    if floor_capacity >= team_size:
                        floor_assignments[floor_name].append(team_number)
                        break

    # Check if any floor is less than 25% full and try to move teams to underfilled floors
    for floor in floors:
        floor_name, floor_capacity = floor
        while len(floor_assignments[floor_name]) / floor_capacity < 0.25:
            for other_floor in floors:
                if other_floor[0] != floor_name and len(floor_assignments[other_floor[0]]) / other_floor[1] > 0.25:
                    team_to_move = floor_assignments[other_floor[0]][-1]
                    floor_assignments[other_floor[0]].remove(team_to_move)
                    floor_assignments[floor_name].append(team_to_move)
                    break

    return floor_assignments
