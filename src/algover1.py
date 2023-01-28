# don't touch this pls

# teams = ((<team number>, <number of members>, <list of preferred teams>, <list of tolerated teams>, <list of blacklisted teams>), ...)
# floors = ((<floor number>, <capacity>), ...)

def sort_teams(teams, floors):
    # Create a dictionary to store the teams and their preferences
    team_prefs = {}
    for team in teams:
        team_num, team_size, preferred, tolerated, blacklisted = team
        team_prefs[team_num] = {
            'size': team_size,
            'preferred': set(preferred),
            'tolerated': set(tolerated),
            'blacklisted': set(blacklisted)
        }
    # Create a list to store the final team assignments
    assignments = []
    # Sort the floors by capacity
    floors = sorted(floors, key=lambda x: x[1])
    # Iterate through each floor
    for floor in floors:
        floor_name, floor_capacity = floor
        # Keep track of the remaining capacity for the current floor
        remaining_capacity = floor_capacity
        # Create a list to store the teams assigned to the current floor
        assigned_teams = []
        # Iterate through each team
        for team_num, team_info in team_prefs.items():
            # Check if the team has already been assigned
            if team_num in [team[0] for team in assignments]:
                continue
            # Check if the team fits within the remaining capacity
            if team_info['size'] > remaining_capacity:
                continue
            # Check if the team has any preferred teams assigned to the current floor
            preferred_teams = [
                team for team in assigned_teams if team[0] in team_info['preferred']
            ]
            if preferred_teams:
                # Assign the team to the current floor
                assigned_teams.append((team_num, team_info['size']))
                remaining_capacity -= team_info['size']
                continue
            # Check if the team has any tolerated teams assigned to the current floor
            tolerated_teams = [
                team for team in assigned_teams if team[0] in team_info['tolerated']
            ]
            if tolerated_teams and remaining_capacity >= floor_capacity * 0.25:
                # Assign the team to the current floor
                assigned_teams.append((team_num, team_info['size']))
                remaining_capacity -= team_info['size']
                continue
            # Check if the team has any blacklisted teams assigned to the current floor
            blacklisted_teams = [
                team for team in assigned_teams if team[0] in team_info['blacklisted']
            ]
            if not blacklisted_teams:
                # Assign the team to the current floor
                assigned_teams.append((team_num, team_info['size']))
                remaining_capacity -= team_info['size']
                continue
        # Add the assigned teams to the final list of assignments
        if assigned_teams:
            assignments.append((floor_name, assigned_teams))
    return assignments
