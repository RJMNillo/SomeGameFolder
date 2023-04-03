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
        for someunit in TeamA:
            self.totalInterval = self.totalInterval + someunit.SPD
        for someunit in TeamB:
            self.totalInterval = self.totalInterval + someunit.SPD
        
        self.totalInterval = int(self.totalInterval/AvgOfPlayers)
