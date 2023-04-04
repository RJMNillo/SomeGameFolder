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
        if self.Team1HP == 0:
            print("Team 2 Wins!")
        elif self.Team2HP == 0:
            print("Team 1 Wins!")
        else:
            # Check if teams are ready to attack
            if (self.Team1Ready() or self.Team2Ready()):
                # Both Teams are ready
                if (self.Team1Ready() and self.Team2Ready()):
                    pass
                # Someone from Team 1 is ready
                elif (self.Team1Ready()):
                    pass
                # Someone from Team 2 is ready
                elif(self.Team2Ready()):
                    pass
                # If nobody is ready, increase intervals
                else:
                    for someunit in self.Team1:
                        someunit.Interval = someunit.Interval + someunit.SPD
                    for someunit in self.Team2:
                        someunit.Interval = someunit.Interval + someunit.SPD



    # Helper Functions
    # Team 1 Ready
    def Team1Ready(self):
        for someunit in self.Team1:
            if someunit.Interval >= self.totalInterval:
                return True
            return False
    
    # Team 2 Ready
    def Team2Ready(self):
        for someunit in self.Team2:
            if someunit.Interval >= self.totalInterval:
                return True
            return False