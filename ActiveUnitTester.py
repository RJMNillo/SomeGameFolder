# Reggie Jan Marc Nillo
from NewGameTest import unit, ActiveUnit
from GameActionPhase import ActionPhase

if __name__ == "__main__":
    JohnUnit = ActiveUnit("John", 30, 20, 10, 15, 14, 1, 0.8, 1.2, 0.9)
    JohnUnit.printStats()

    JackUnit = ActiveUnit("Jack", 27, 18, 25, 9, 14, 0.9, 1.2, 2, 0.4)
    JackUnit.printStats()

    TeamA = []
    TeamB = []
    TeamA.append(JohnUnit)
    TeamB.append(JackUnit)
    GameAction = ActionPhase(TeamA, TeamB)

    print("Get Ready for the next BATTLE")
    print("**************************************")
    while(GameAction.Team1HP > 0 and GameAction.Team2HP > 0):
        GameAction.DoTurn()