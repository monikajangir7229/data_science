

import json
import os
from collections import defaultdict

# IPL DATA

ipl_data = [
    {
        "match_id": 1,
        "team1": "CSK",
        "team2": "MI",
        "stadium": "Wankhede Stadium",
        "winner": "CSK",
        "score": {
            "CSK": 198,
            "MI": 190
        },
        "players": {
            "Dhoni": 45,
            "Rohit": 70,
            "Gaikwad": 60
        }
    },

    {
        "match_id": 2,
        "team1": "RCB",
        "team2": "KKR",
        "stadium": "Chinnaswamy Stadium",
        "winner": "RCB",
        "score": {
            "RCB": 210,
            "KKR": 180
        },
        "players": {
            "Virat": 85,
            "Maxwell": 55,
            "Russell": 40
        }
    }
]


#  OBJECT FORMAT

class Match:

    def __init__(self, match_id, team1, team2, stadium, winner, score, players):

        self.match_id = match_id
        self.team1 = team1
        self.team2 = team2
        self.stadium = stadium
        self.winner = winner
        self.score = score
        self.players = players

    def display_match(self):

        print("\n---------------- MATCH DETAILS ----------------")

        print("Match ID:", self.match_id)
        print("Teams:", self.team1, "vs", self.team2)
        print("Stadium:", self.stadium)
        print("Winner:", self.winner)

        print("\nScores:")

        for team, runs in self.score.items():
            print(team, ":", runs)

        print("\nPlayer Scores:")

        for player, runs in self.players.items():
            print(player, ":", runs)


# GROUPING

def group_by_stadium(data):

    stadium_group = defaultdict(list)

    for match in data:

        stadium_group[match["stadium"]].append(match)

    return stadium_group


# FILE HANDLING

def save_player_scores(match):

    try:

        # Create folder
        folder_name = "player_scores"

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Save every player in separate file
        for player, runs in match.players.items():

            file_path = os.path.join(folder_name, player + ".txt")

            with open(file_path, "w") as file:

                file.write("Player Name: " + player + "\n")
                file.write("Runs: " + str(runs))

        print("\nPlayer files created successfully.")

    except Exception as e:

        print("Error while saving files:", e)


# JSON STORAGE

def save_match_json(data):

    try:

        with open("ipl_matches.json", "w") as file:

            json.dump(data, file, indent=4)

        print("\nIPL data stored locally in JSON file.")

    except Exception as e:

        print("Error storing JSON:", e)


#  MAIN PROCESS LAYER

def process_ipl_data(data):

    matches = []

    # Layer 1: Convert into objects
    for item in data:

        match_obj = Match(
            item["match_id"],
            item["team1"],
            item["team2"],
            item["stadium"],
            item["winner"],
            item["score"],
            item["players"]
        )

        matches.append(match_obj)

    # Layer 2: Print Sequential Data
    for match in matches:

        match.display_match()

        # Layer 3: Store player data
        save_player_scores(match)

    # Layer 4: Grouping
    grouped_data = group_by_stadium(data)

    print("\n---------------- GROUPED BY STADIUM ----------------")

    for stadium, matches in grouped_data.items():

        print("\nStadium:", stadium)

        for m in matches:

            print(m["team1"], "vs", m["team2"])

    # Layer 5: Store JSON
    save_match_json(data)


#EXECUTION

try:

    process_ipl_data(ipl_data)

except Exception as error:

    print("Main Error:", error)