

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import os


# SAMPLE IPL DATA 

ipl_data = {
    "Match_No": [1, 2, 3, 4, 5, 6],
    "Team1": ["CSK", "MI", "RCB", "KKR", "CSK", "MI"],
    "Team2": ["MI", "RCB", "KKR", "CSK", "RCB", "KKR"],
    "HomeGround": [
        "Chepauk",
        "Wankhede",
        "Chinnaswamy",
        "Eden Gardens",
        "Chepauk",
        "Wankhede"
    ],
    "Winner": ["CSK", "MI", "RCB", "KKR", "CSK", "MI"],
    "Top_Player": [
        "Dhoni",
        "Rohit",
        "Virat",
        "Russell",
        "Gaikwad",
        "Sky"
    ]
}

df = pd.DataFrame(ipl_data)


# OOPS CLASS

class IPLModel:

    def __init__(self, dataframe):

        self.df = dataframe

        self.team_encoder = LabelEncoder()
        self.ground_encoder = LabelEncoder()

        self.model = DecisionTreeClassifier()

    #  DATA PREPROCESSING

    def preprocess(self):

        self.df["Team1_Encoded"] = self.team_encoder.fit_transform(
            self.df["Team1"]
        )

        self.df["Team2_Encoded"] = self.team_encoder.fit_transform(
            self.df["Team2"]
        )

        self.df["Ground_Encoded"] = self.ground_encoder.fit_transform(
            self.df["HomeGround"]
        )

    #  MODEL TRAINING

    def train_model(self):

        X = self.df[["Team1_Encoded", "Team2_Encoded"]]

        y = self.df["Ground_Encoded"]

        self.model.fit(X, y)

        print("\nModel Trained Successfully")

    #  PREDICTION

    def predict_stadium(self, team1, team2):

        try:

            t1 = self.team_encoder.transform([team1])[0]
            t2 = self.team_encoder.transform([team2])[0]

            prediction = self.model.predict([[t1, t2]])

            stadium = self.ground_encoder.inverse_transform(prediction)

            return stadium[0]

        except Exception as e:

            print("Prediction Error:", e)

    #  SEQUENTIAL MATCHES

    def print_match_sequence(self):

        print("\n---------------- IPL MATCH SEQUENCE ----------------")

        sorted_df = self.df.sort_values("Match_No")

        for _, row in sorted_df.iterrows():

            print(
                "Match",
                row["Match_No"],
                ":",
                row["Team1"],
                "vs",
                row["Team2"]
            )

            print("Home Ground:", row["HomeGround"])

            print("Top Player:", row["Top_Player"])

            print("-------------------------------------")

    #  GROUPING 

    def group_by_stadium(self):

        print("\n---------------- GROUPED STADIUM DATA ----------------")

        grouped = self.df.groupby("HomeGround")

        for stadium, data in grouped:

            print("\nStadium:", stadium)

            for _, row in data.iterrows():

                print(row["Team1"], "vs", row["Team2"])

   

    def save_player_files(self):

        try:

            folder = "ipl_players"

            if not os.path.exists(folder):

                os.makedirs(folder)

            for _, row in self.df.iterrows():

                filename = row["Top_Player"] + ".txt"

                path = os.path.join(folder, filename)

                with open(path, "w") as file:

                    file.write("Player: " + row["Top_Player"] + "\n")

                    file.write(
                        "Match: "
                        + row["Team1"]
                        + " vs "
                        + row["Team2"]
                    )

            print("\nPlayer Files Created Successfully")

        except Exception as e:

            print("File Error:", e)




try:

    ipl = IPLModel(df)

   
    ipl.preprocess()

  
    ipl.train_model()

  
    ipl.print_match_sequence()

   
    ipl.group_by_stadium()

  
    ipl.save_player_files()

    print("\n---------------- NEXT MATCH PREDICTION ----------------")

    next_match_stadium = ipl.predict_stadium("CSK", "KKR")

    print("Predicted Stadium for CSK vs KKR:")

    print(next_match_stadium)

except Exception as error:

    print("Main Error:", error)