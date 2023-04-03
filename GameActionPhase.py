from NewGameTest import unit, ActiveUnit
# Reggie Jan Marc Nillo

# Game Test

# Holder of the ActionPhase Class

class ActionPhase():
    def __init__(self, TeamA, TeamB):
        self.Team1 = TeamA
        
        self.Team2 = TeamB
        # Set the Total Interval
        # Total Interval will take the speeds of all characters involved
        # Divided by the average amount of players per team
        # Multiplied by the number of teams (For our case, 2)
        NumOfTeams = 2
        AvgOfPlayers = int((len(TeamA) + len(TeamB))/NumOfTeams)
        print(f"AVG: {AvgOfPlayers}")
        
        # Creating the Interval
        self.totalInterval = 0
        for someunit in self.Team1:
            self.totalInterval = self.totalInterval + someunit.SPD
        for someunit in self.Team2:
            self.totalInterval = self.totalInterval + someunit.SPD
        
        self.totalInterval = int(self.totalInterval/AvgOfPlayers)

        # Status Holders
        # Integer Variables that hold the entire team's HP
        self.Team1HP = 0
        self.Team2HP = 0

        for someunit in self.Team1:
            self.Team1HP = self.Team1HP + someunit.HP
        for someunit in self.Team2:
            self.Team2HP = self.Team2HP + someunit.HP

    # Function Definition of the Action Phase
    def DoAction(self):

        pass
