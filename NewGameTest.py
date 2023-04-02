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
        self.taglist = []

class ActiveUnit(unit):
    def __init__(self, UName, ULevel, UBHP, UBATK, UBSPD, UBDEF, UGHP, UGATK, UGSPD, UGDEF):
        # Inheriting the unit class
        super.__init__(self, UName, ULevel, UBHP, UBATK, UBSPD, UBDEF, UGHP, UGATK, UGSPD, UGDEF)
        # Unit's stats
        self.HP = round((self.Level - 1) * self.GHP,0) + self.BHP
        self.ATK = round((self.Level - 1) * self.GATK,0) + self.BATK
        self.SPD = round((self.Level - 1) * self.GSPD,0) + self.BSPD
        self.DEF = round((self.Level - 1) * self.GDEF,0) + self.BDEF

