# Reggie Jan Marc Nillo
# Game Idea No. 1

# RPG
# Might follow the classic Megami Tensei Route

class unit():
    def __init__(self, UName, ULevel, UBHP, UBATK, UBSPD, UBDEF, UGHP, UGATK, UGSPD, UGDEF):
        self.Name = UName
        self.Level = ULevel
        self.BHP = UBHP
        self.BATK = UBATK
        self.BSPD = UBSPD
        self.BDEF = UBDEF
        self.GHP = UGHP
        self.GATK = UGATK
        self.GSPD = UGSPD
        self.GDEF = UGDEF
# End of class unit

class ActiveUnit(unit):
    def __init__(self, UName, ULevel, UBHP, UBATK, UBSPD, UBDEF, UGHP, UGATK, UGSPD, UGDEF):
        # Inheriting the unit class
        unit.__init__(self, UName, ULevel, UBHP, UBATK, UBSPD, UBDEF, UGHP, UGATK, UGSPD, UGDEF)
        # Unit's stats
        self.HP = (round((self.Level - 1) * self.GHP,0) + self.BHP) * 10
        self.ATK = (round((self.Level - 1) * self.GATK,0) + self.BATK) * 5
        self.SPD = (round((self.Level - 1) * self.GSPD,0) + self.BSPD) * 5
        self.DEF = (round((self.Level - 1) * self.GDEF,0) + self.BDEF) * 5
        # Unit's Sets
        self.skillList = []
        # Unit's Interval
        self.Interval = 0


    # Prints the Unit's Stats
    def printStats(self):
        print(f"Unit Analysis for {self.Name}")
        print(f"Level: {self.Level}")
        print(f"HP: {self.HP}")
        print(f"ATK: {self.ATK}")
        print(f"SPD: {self.SPD}")
        print(f"DEF: {self.DEF}")
# End of class ActiveUnit
